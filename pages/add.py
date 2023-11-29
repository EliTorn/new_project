import streamlit as st

#my_file = __import__("app")
from app import connect
from PIL import Image


def page2() -> None:
    """
    the function do the page 2 in the web
     the function add the new itme into the web
    :return:
    """
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image_bit = uploaded_file.read()
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', width=200)
        name = st.text_input("What the name of the product")
        amount = st.number_input('Enter a amount ', 0)

        if st.button("Save Data"):
            # Make sure the directory exists
            connect(name, image_bit, amount)

            st.success('Data Save')


page2()
