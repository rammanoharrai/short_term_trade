import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import os
class Connection:
    def __init__(self):
        self.connection = sqlite3.connect('short_term_trade.db')
        self.cursor = self.connection.cursor()

    def insert(self,new_trade):
        """share_name,share_id,target,stop_loss,suggested_by,date_initiated,purchase_price,no_of_purchse"""
        query="""INSERT INTO trade_info(
                       Share_name,
                       Share_ID,
                       Target,
                       'Stop Loss',
                       'Suggested By',
                       'Date Initiated',
                       'Purchase Price',
                       'No of Purchase',
                       Flag)
                        VALUES(?,?,?,?,?,?,?,?,?)"""
                        
        values=(new_trade['Share_name'],new_trade['Share_ID'],
                new_trade['Target'],new_trade['Stop Loss'],
                new_trade['Suggested By'],new_trade['Date Initiated'],
                new_trade['Purchase Price'],new_trade['No of Purchase'],1)
        self.cursor.execute(query,values)
        print('executed the insert')
        self.connection.commit()

    def close_trade(self,close_trade):
        query = """UPDATE trade_info SET                
                               'Sold Date'=?,
                               'Sold Price'=?,
                                Flag=?
                                WHERE ID=?
                                """

        values = ( close_trade['Sold Date'],
                  close_trade['Sold Price'], '0',close_trade['ID'])
        self.cursor.execute(query,values)
        print('executed the update')
        self.connection.commit()
    def show_all(self):
        query="""SELECT * FROM TRADE_INFO """
        df = pd.read_sql_query("select * from trade_info", self.connection)
        return df

    def show_summary_record(self):
        query="""SELECT ID,share_name,'Purchase Price' FROM TRADE_INFO """
        self.cursor.execute(query)
        data=self.cursor.fetchall()
        return data

    def delete(self,id):
        cursor=self.connection.cursor()
        query="""DELETE FROM TRADE_INFO WHERE id=?"""
        cursor.execute(query,id)
        cursor.close()
        self.connection.commit()
        
    def edit(self,id,new_tuple):
        cursor=connection.cursor()
        query="""UPDATE TRADE_INFO SET 
                       Share_name=?,
                       Share_ID=?,
                       Target=?,
                       'Stop Loss'=?,
                       'Suggested By'=?,
                       'Date Initiated'=?,
                       'Purchase Price'=?,
                       'No of Purchase'=?
                       WHERE ID=?
                       """
        cursor.execute(query,new_tuple+(id,))
        cursor.close()
        connection.commit()



    def close_connection(self):
        self.connection.close()

class price_extract:
    def __init__(self):
        pass
    def current_price(self,ticker):
        url=f'https://www.google.com/finance/quote/{ticker}:NSE?hl=en'
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            class1 = 'YMlKec fxKbKc'
            current_price=soup.find(class_=class1).text
            return current_price
        except:
            return Null

class Email_communication:
    def __init__(self):
        pass
    def send_email(self,message):
        host = "smtp.gmail.com"
        port = 465
        username = 'rammanoharrai@gmail.com'
        password = os.getenv('PASSWORD')
        receiver = 'rammanoharrai@gmail.com'
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(host, port, context=context) as server:
                server.login(username, password)
                server.sendmail(username, receiver, message)
                return('Mail_sent')
        except Exception as e:
            return (f"eror: {e}")

