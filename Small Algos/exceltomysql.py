import pandas as pd
from mysql.connector import connection

ws = pd.read_csv('/Users/ashmwalia/Documents/CAC Data/ProductInformation.csv')

cnx = connection.MySQLConnection(host="localhost", user="root",password="Garv@9031", database="appbackend")
cursor = cnx.cursor()


for i in range(ws.shape[0]):
    query = "insert into api_productinformation (name, product, packing, mrp, rate, balance, company, salt, commodity, category) VALUES (%(name)s, %(product)s, %(packing)s, %(mrp)s, %(ratea)s, %(balance)s, %(company)s, %(salt)s, %(commodity)s, %(category)s)"
    data = {
    'name':str(ws.iloc[i,0]),
    'product':str(ws.iloc[i,1]),
    'packing':str(ws.iloc[i,2]),
    'mrp':str(ws.iloc[i,3]),
    'ratea':str(ws.iloc[i,4]),
    'balance':str(ws.iloc[i,5]),
    'company':str(ws.iloc[i,6]),
    'salt':str(ws.iloc[i,7]),
    'commodity':str(ws.iloc[i,8]),
    'category':str(ws.iloc[i,9])
    }
    cursor.execute(query, data)

cnx.commit()
cnx.close()

