import streamlit as st
import pandas as pd
import requests
import json


def check_user_id(id):
    res = requests.get(url + id)
    if res.ok:
        st.session_state.disable_button = False or st.session_state.your_id == ''
        return True
    else:
        st.session_state.disable_button = True or st.session_state.your_id == ''
        return False


def add_product(cat, pro, qua, pri):
    bdy = {
        "product_list": {
            f'{cat}_{pro}': {
                "inventory": qua,
                "price": pri
            }
        }
    }
    res = requests.patch(url + st.session_state['your_id'], data=json.dumps(bdy))
    return res.status_code == 200


def show_products():
    res = requests.get(url + st.session_state['your_id'])
    product_list = res.json()['product_list']
    if product_list is not None:
        st.session_state['products'] = pd.DataFrame([
            {
                'Category': k.split('_')[0],
                'Product': k.split('_')[1],
                'Price': v.get('price'),
                'Inventory': v.get('inventory')
            }
            for k, v in product_list.items()
        ])
    else:
        st.session_state['products'] = pd.DataFrame(columns=['Category', 'Product', 'Price', 'Inventory'])


def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections["Select to Delete"] = False

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select to Delete": st.column_config.CheckboxColumn(required=True)},
        disabled=['Category', 'Product']
    )

    return edited_df


def update_products(df):
    if len(df) == 0:
        return
    body = {"product_list": {r.Category + "_" + r.Product: {"inventory": r.Inventory, "price": r.Price} for i, r in df.iterrows()}}
    res = requests.patch(url + st.session_state['your_id'], data=json.dumps(body))
    product_list = res.json()['product_list']
    if product_list is not None:
        st.session_state['products'] = pd.DataFrame([
            {
                'Category': k.split('_')[0],
                'Product': k.split('_')[1],
                'Price': v.get('price'),
                'Inventory': v.get('inventory')
            }
            for k, v in product_list.items()
        ])


def delete_products(df):
    if len(df) == 0:
        return
    for i, r in df.iterrows():
        res = requests.delete(f"{url}{st.session_state['your_id']}/product_list/{r.Category}_{r.Product}")
    show_products()


url = 'http://back:80/farmer/'
if 'your_id' not in st.session_state:
    st.session_state['your_id'] = ''
if 'products' not in st.session_state:
    st.session_state['products'] = pd.DataFrame(columns=['Category', 'Product', 'Price', 'Inventory'])
if 'disable_button' not in st.session_state:
    st.session_state['disable_button'] = True

st.write('# Farmer Page🌾')

st.write("### Login")
with st.expander("Clike Here to Login / Sign Up"):
    with st.popover("Set your ID here"):
        st.session_state['your_id'] = st.text_input("What's your ID?", st.session_state['your_id'])
    st.markdown('Are you a new farmer? &nbsp; Please create your ID!')
    with st.form("sign_up_form", clear_on_submit=True):
        name = st.text_input("Name")
        phone_number = st.text_input("Phone Number")
        location = st.text_input("Location")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if not name or not phone_number or not location:
                st.error("Please fill out all fields before submitting.")
            else:
                body = {'name': name, 'contact': phone_number, 'location': location}
                res = requests.post(url, data=json.dumps(body))
                if res.ok:
                    st.session_state['your_id'] = res.json()['_id']
                    st.success(f"Successfully sign up and login. Your ID is: {st.session_state['your_id']}")
                else:
                    st.error("Failed to sign up. Please try again.")
st.write("Your ID: ", f":blue[{st.session_state['your_id']}]")
if st.session_state['your_id'] == '':
    pass
elif check_user_id(st.session_state['your_id']):
    st.success('Valid ID')
else:
    st.error('Invalid ID')

st.write("### Add Products")
with st.expander("Click Here to Add Products"):
    # with st.popover("Select Category"):
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
    # st.write("Category: ", f":green[{category}]")
    # with st.form("add_products_form", clear_on_submit=True):
    product = st.selectbox("Select Product", products)
    price = st.number_input("Price per unit", min_value=0.00)
    quantity = st.number_input("Inventory", min_value=0)
    add_button = st.button("Add Product", disabled=st.session_state.disable_button)
    if add_button:
        current_product_list = requests.get(url + st.session_state['your_id']).json()['product_list']
        if not category or not product or price <= 0 or quantity < 1:
            st.error("Please fill in all fields correctly before adding a product.")
        else:
            if current_product_list is not None:
                if f'{category}_{product}' in current_product_list:
                    st.error("You are trying to add a product which you already have.")
                else:
                    res_add = add_product(category, product, quantity, price)
                    if res_add:
                        st.success(f"Product added successfully.")
                    else:
                        st.error("Error!! Product could not be added")
            else:
                res_add = add_product(category, product, quantity, price)
                if res_add:
                    st.success(f"Product added successfully.")
                else:
                    st.error("Error!! Product could not be added")

st.write("### Your Product List")
st.button('Show', on_click=show_products, disabled=st.session_state.disable_button)
st.dataframe(st.session_state['products'], hide_index=True)

with st.expander("Manage Your Products"):
    edited_df = dataframe_with_selections(st.session_state['products'])
    selected_rows = edited_df[edited_df['Select to Delete']]
    selected_rows.drop('Select to Delete', axis=1)
    col1, col2, col3 = st.columns([0.13, 0.13, 0.74])
    with col1:
        st.button('Update', on_click=update_products, args=[edited_df], disabled=st.session_state.disable_button)
    with col2:
        st.button('Delete', on_click=delete_products, args=[selected_rows], disabled=st.session_state.disable_button)
