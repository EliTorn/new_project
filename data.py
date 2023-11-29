import streamlit as st
from app import connect, show, search, update

import time

st.title("מטבחסן")


def delete(name):
    print(f"You need delete the {name}")
    page5()


def page_one() -> None:
    """
    the function do the main page on the app
    the main page get all the data into database and show on the web
    :return:
    """
    data = show()

    if data:
        key = 0
        for product in data:
            col1, col2, col3, col4 = st.columns(4)
            col1.image(product['picture'], width=50, caption=product['name'])
            col2.write(product["amount"])
            update_button = col3.button("UPDATE", key=key)
            delete_button = col4.button("DELETE", key=1000 - key)
            if update_button:
                st.session_state["update"] = product['name']
                st.session_state["page"] = 2
                st.experimental_rerun()

            if delete_button:
                st.session_state["delete"] = product['name']
                st.session_state["page"] = 3
                st.experimental_rerun()
            key += 1
            for _ in range(7):
                st.text('\n')





def page4():
    value_update = st.session_state['update']
    data = search(value_update)
    for d in data:
        st.image(d['picture'], caption=d['name'])
        st.write(d['amount'])
    value = int(st.number_input("enter a number ", 0))
    button_clicked = st.button("update")
    if button_clicked:
        st.write()
        st.write(f"you need to update the value to {value} ")
        st.success("update")
        time.sleep(3)
        st.session_state["page"] = 1
        st.experimental_rerun()


def page5():
    print('i am page 5 ')
    st.write("Hello")
    value_update = st.session_state["delete"]
    data = search(value_update)
    for d in data:
        st.image(d['picture'], caption=d['name'])
        st.write(d['amount'])
        st.write("Hello")
    st.warning("you going to delete ")
    b = st.button("are you shore Click")
    if b:
        st.write()
        st.write(f"you need to update the value to ")
        st.success("delete")
        time.sleep(1)
        st.session_state["page"] = 1
        st.experimental_rerun()


def main():
    if st.session_state.get("page") is None:
        st.session_state["page"] = 1

    # Display the content for the current page
    if st.session_state.page == 1:
        page_one()
    elif st.session_state.page == 2:
        page4()
    elif st.session_state.page == 3:
        page5()


if __name__ == '__main__':
    main()
