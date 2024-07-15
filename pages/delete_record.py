import streamlit as st
from function import Connection


def delete_data():
    connection = Connection()
    connection.delete(st.session_state['delete_id'])
    connection.close_connection()


st.header('Delete erroneous records')
st.text_input("enter_id_of_record_to_delete",key='delete_id')
st.button(label='Delete the trade',on_click=delete_data,key='Deleted')
if st.session_state['Deleted']==True:
    st.text("Record has been deleted")



