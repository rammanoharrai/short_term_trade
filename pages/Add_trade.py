import streamlit as st
from function import Connection

def add_data():
    connection=Connection()
    new_share={}
    for key in st.session_state.keys():
        new_share[key]=st.session_state[key]
    print('values_added',new_share)
    connection.insert(new_share)
    connection.close_connection()

st.header('Add trade')

column_list=['Share_name','Share_ID','Target','Stop Loss','Suggested By','Date Initiated','Purchase Price','No of Purchase']
for list in column_list:
    if list != 'Date Initiated':
        st.text_input(list,key=list)
    else:
        st.date_input(list,key=list)
st.button(label='Add the trade',on_click=add_data,key='Record Added')
if(st.session_state['Record Added']==True):
    st.text('Record has been added')
    st.rerun()



