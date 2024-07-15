from function import Connection
connection=Connection()

while True:
    user_action=input("Type Add, Show, Edit,Sell, Delete, Exit")
    user_action=user_action.strip()
    match user_action:
        case 'Add':
            Share_name,Share_id,Target,Stop_Loss,Suggested_By=input('Share_name,Share_id,Target,Stop Loss,Suggested By').split()
            Date_initiated,Purchase_price,No_of_purchase=input('Date Initiated, Purchase Price, No of Purchase').split()
            connection.insert(Share_name,Share_id,Target,Stop_Loss,Suggested_By,Date_initiated,Purchase_price,No_of_purchase)
        case 'Show':
            table=connection.show_all()
            for row in table:
                print(row,'\n')

        case 'Edit':
            print('Enter the id of record you want to edit from list below')
            print(connection.show_summary_record())
            user_input = input('Enter the id to be edited')
            print('enter the new details')
            Details1 = tuple(input('Share_name,Share_id,Target,Stop Loss,Suggested By').split())
            Details2 = tuple(input('Date Initiated, Purchase Price, No of Purchase').split())
            new_tuple=Details1+Details2
            connection.edit(user_input,new_tuple)
        #
        case 'Delete':
              print('Enter the id of record you want to delete from list below')
              print(show_summary_record())
              user_input=input('Enter the id to be deleted')
              connection.delete(user_input)

        case 'Sell':
              print('Enter the id of record you want to Sell from list below')
              print(show_summary_record())
              user_input=input('Enter the id to be deleted')
              connection.delete(user_input)


        case 'Exit':
            connection.close_connection()
            break


        case _:
            print("command doesnt match")

