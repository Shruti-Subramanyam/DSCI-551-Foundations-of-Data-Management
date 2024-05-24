import streamlit as st
import requests
import pandas as pd
import json


def search_results(category, product):
    res = requests.get(url + f"find/{category}_{product}")
    product_list = res.json()
    if product_list:
        data = []
        for p in product_list:
            for k, v in p['product_list'].items():
                category, product = k.split('_')[:2]
                data.append({
                    'Category': category,
                    'Product': product,
                    'Review': f"{v['rating']:.1f}" if v['rating'] is not None else '-',
                    'Price': v['price'],
                    'Inventory': v['inventory'],
                    'id': p['_id'],
                    "Farmer's Name": p['name'],
                    'Contact': p['contact'],
                    'Location': p['location'],
                })
        st.session_state['results'] = pd.DataFrame(data)
        st.session_state.button = False
        st.session_state.disable_co = True



def dataframe_with_numbers(df):
    df_with_selections = df.copy()
    df_with_selections["Add to Cart"] = 0

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_order=("Farmer's Name", "Contact", "Review", "Price", "Inventory", "Add to Cart"),
        column_config={"Add to Cart": st.column_config.NumberColumn(step=1)},
        disabled=df.columns
    )

    return edited_df


def checkout(df):
    for i, r in df.iterrows():
        id = r.id
        product_name = f"{r.Category}_{r.Product}"
        q = r['Add to Cart']
        res = requests.patch(url + f"purchase/{id}/{product_name}", data=json.dumps({"quantity": q}))
    st.session_state.button = True
    st.session_state.disable_co = True
    st.session_state.button2 = False


def dataframe_with_review(df):
    df_with_selections = df.copy()
    df_with_selections["Your Rating"] = 3

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_order=("Category", "Product", "Farmer's Name", "Price", "Review", "Your Rating"),
        column_config={"Your Rating": st.column_config.NumberColumn(step=1, min_value=1, max_value=5, format="%d ⭐", help="How much do you like this product (1-5)?")},
        disabled=df.columns
    )

    return edited_df


def submit_review(df):
    for i, r in df.iterrows():
        id = r.id
        product_name = f"{r.Category}_{r.Product}"
        rt = r['Your Rating']
        res = requests.patch(url + f"review/{id}/{product_name}", data=json.dumps({"rating": rt}))
    st.session_state.button2 = True


url = 'http://back:80/user/'
if 'results' not in st.session_state:
    st.session_state['results'] = pd.DataFrame(columns=["Farmer's Name", "Review", "Price", "Inventory", "Add to Cart"])
if 'button' not in st.session_state:
    st.session_state.button = False
if 'button2' not in st.session_state:
    st.session_state.button2 = True
if 'disable_co' not in st.session_state:
    st.session_state.disable_co = True

st.write('# User Page🛒')

st.write("### Search Products")
category = st.selectbox("Select Category", ["", "Vegetables", "Fruits", "Frozen", "Canned"])
if category == "Vegetables":
    products = ["Tomato", "Potato", "Onion", "Carrot", "Lettuce"]
elif category == "Fruits":
    products = ["Apple", "Banana", "Orange", "Blueberry"]
elif category == "Frozen":
    products = ["Orange", "Blueberry", "Mango", "Peas", "Broccoli"]
elif category == "Canned":
    products = ["Grapefruit", "Peaches", "Mandarins", "Corn", "Tomato", "Peas"]
else:
    products = []
product = st.selectbox("Select Product", products)
st.button("Search Products", on_click=search_results, args=[category, product])
edited_df = dataframe_with_numbers(st.session_state['results'])
selected_rows = edited_df[edited_df['Add to Cart'] > 0]
total_price = 0
if (edited_df['Add to Cart'] < 0).any():
    st.error('You cannot buy products less than 0!')
    st.session_state.disable_co = True
elif (edited_df['Add to Cart'] > edited_df['Inventory']).any():
    st.error('You cannot buy more than inventory!')
    st.session_state.disable_co = True
elif len(selected_rows) > 0:
    st.session_state.disable_co = False

for i, r in edited_df.iterrows():
    q = r['Add to Cart']
    total_price += r.Price * q

with st.expander("Your Cart"):
    st.dataframe(selected_rows, hide_index=True, column_order=("Farmer's Name", "Contact", "Review", "Price", "Inventory", "Add to Cart"))
    st.write(f'**Total Price**: :blue[${total_price}]')
    st.button('Checkout', on_click=checkout, args=[selected_rows], disabled=(st.session_state.disable_co or st.session_state.button))
    if st.session_state.button:
        st.success('Thank you for your purchasing! &nbsp; You can review the products below.')
        review_df = dataframe_with_review(selected_rows)
        sr = st.button('Submit your Review', on_click=submit_review, args=[review_df], disabled=st.session_state.button2)
        if sr:
            st.success('Thank you for reviewing!')

