import streamlit as st
from app import search

st.title("search")
value = st.text_input("search")
if value:
    find = search(value)
    for d in find:
        st.image(d['picture'], width=100, caption=d['name'])
        st.write(d['amount'])
