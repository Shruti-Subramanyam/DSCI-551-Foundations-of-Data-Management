import streamlit as st
import pandas as pd
import requests

st.write('# All Products🥕')
res = requests.get('http://back:80/farmer/')
data = []

for e in res.json():
    if e['product_list'] is not None:
        for k, v in e['product_list'].items():
            category, product = k.split('_')[:2]
            data.append({
                'Category': category,
                'Product': product,
                'Review': f"{v['rating']:.1f}" if v['rating'] is not None else '-',
                'Price': v['price'],
                # 'Inventory': v['inventory'],
                'Farmer': e['name'],
                'Contact': e['contact'],
                'Location': e['location']
            })

df = pd.DataFrame(data).sort_values(by=['Category', 'Product'])
st.dataframe(df, hide_index=True)
