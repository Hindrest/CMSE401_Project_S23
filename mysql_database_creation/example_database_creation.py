
#!/usr/bin/python
import mysql.connector 
import pandas as pd

from mysql.connector import errorcode

uname = "########"
pwd = "#######"
hname = "#########"

#Reading in data to insert into the MySQL database; In this instance, we are using data from best buy
best_buy_data = pd.read_csv('bestbuy.csv') #15,120 entries | large

#Creating our connection (cnx) object that connrects to the database
cnx = mysql.connector.connect(user = uname, password = pwd, host = hname, database = uname)
mysql.connector.connect()

#Creating a function called "query_server" that takes in an SQL query and connects to the MySQL database
def query_server(query):
    cnx = mysql.connector.connect(user = uname, password = pwd, host = hname, database = uname)
    curs = cnx.cursor()
    execute = curs.execute(query)
    result = curs.fetchall()
    curs.close()
    cnx.close()
    return result

#A query to create a table named "best_buy" with columns user, sku, query, click_time, and query_time
query_server("""CREATE TABLE IF NOT EXISTS best_buy (user varchar(50), sku int, category varchar(50), 
    query varchar(100), click_time DATETIME, query_time DATETIME)""")

