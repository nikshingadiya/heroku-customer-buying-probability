#
# import mysql.connector
# import  numpy as np
# try :
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="nikhil1234?",
#         database="customer_review"
#     )
#     print("Database connection successful!")
# except:
#     print("Database connection loss!")
#
#
# def create_tabel():
#     con = mydb.cursor()
#
#     sql = "CREATE TABLE IF NOT EXISTS customers_feedback4(" \
#           "customer_id INTEGER PRIMARY KEY  NOT NULL AUTO_INCREMENT," \
#           "Age Int NOT NULL," \
#           "Ease_and_convenient VARCHAR(255) NOT NULL," \
#           "Time_saving  VARCHAR(255) NOT NULL," \
#           "More_restaurant_choices VARCHAR(255) NOT NULL," \
#           "Easy_Payment_option  VARCHAR(255) NOT NULL," \
#           "More_Offers_and_Discount VARCHAR(255) NOT NULL," \
#           "Good_Food_quality  VARCHAR(255) NOT NULL," \
#           "Good_Tracking_system VARCHAR(255) NOT NULL," \
#           "Unaffordable VARCHAR(255) NOT NULL," \
#           "Maximum_wait_time VARCHAR(255) NOT NULL," \
#           "Output FLOAT NOT NULL)"
#
#     con.execute(sql)
#
#
# def insert_values(data):
#     data = tuple(data)
#     print(data)
#     con = mydb.cursor()
#     try:
#         # sql ="insert into customers_feedback3 values(?,?,?,?,?,?,?,?,?,?)"
#         sql = "insert into customers_feedback3(" \
#               "Age,Ease_and_convenient,Time_saving," \
#               "More_restaurant_choices,Easy_Payment_option," \
#               "More_Offers_and_Discount," \
#               "Good_Food_quality," \
#               "Good_Tracking_system," \
#               "Unaffordable," \
#               "Maximum_wait_time," \
#               "Output)" \
#               "Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         con.execute(sql, data)
#         mydb.commit()
#         print("Data Entery complete")
#         con.close()
#         return 1
#     except Exception as e:
#         print(e)
#         con.close()
#         return
#
#
#
#
# def get_data():
#     try:
#         con = mydb.cursor()
#         sql = "select * from customers_feedback3;"
#         x=con.execute(sql)
#         data =con.fetchall()
#         field_names = [i[0] for i in con.description]
#
#         print(data)
#         return(field_names,data)
#     except:
#         print("Fetching data failed")
#         con.close()
#         return 0
# def get_admin_data():
#     try:
#         con = mydb.cursor()
#         sql = "select * from admin;"
#         x = con.execute(sql)
#         data = con.fetchall()
#         field_names = [i[0] for i in con.description]
#
#
#         return (data)
#     except:
#         print("Fetching data failed")
#         con.close()
#         return 0
#
