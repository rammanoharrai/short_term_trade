import streamlit as st
from function import Connection

st.header('Page to check all the closed trades')

connection=Connection()
df=connection.show_all()
st.table(df[df['Flag']==0][['Share_name','Share_ID', 'Target', 'Suggested By', 'Date Initiated', 'Purchase Price', 'No of Purchase','Sold Price','Sold Date']])
st.button(label='Add')