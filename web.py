import streamlit as st
import pandas as pd
import sqlite3
from function import Connection,price_extract,Email_communication
import time


st.title('Short Term Trade Monitoring App')
st.write('Use this app to record your trade and square off your perosnal trade')

connection=Connection()
Price=price_extract()
df=connection.show_all()
df_display=df[df['Flag']!=0][['ID','Share_name','Share_ID', 'Target', 'Stop Loss', 'Suggested By', 'Date Initiated', 'Purchase Price', 'No of Purchase']]
df_display['current_price']=[Price.current_price(x).split('₹')[1] for x in df_display['Share_ID']]
st.table(df_display)
email=Email_communication()
while True:
    time.sleep(1000)
    for index,item in df_display.iterrows():
        if float(item['Stop Loss']) > float(item['current_price']):
            message=f"{item['Share_name']} stop loss has triggered"
            print(email.send_email(message))
        if float(item['Current_price']) > float(item['Target']):
            message=f"{item['Share_name']} Target has been achieved"
            print(email.send_email(message))
    st.rerun()

