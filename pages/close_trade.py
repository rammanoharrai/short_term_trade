import streamlit as st
from function import Connection


def close_trade():
    connection = Connection()
    close_trade = {}
    for key in st.session_state.keys():
        close_trade[key] = st.session_state[key]
    connection.close_trade(close_trade)
    connection.close_connection()


st.header('This is to close the trade')

column_list=['ID','Sold Date','Sold Price']
for list in column_list:
    if list != 'Date Initiated':
        st.text_input(list,key=list)
    else:
        st.date_input(list, key=list)
st.button(label='Add the trade',on_click=close_trade)