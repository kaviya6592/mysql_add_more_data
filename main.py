import mysql.connector
import random
from random import randint
import datetime

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="Thanku@123",
  database="shop"

)

# task 1:
# For the items1 table, can you write a loop, going from i = 2000 to a million that
# does something like INSERT INTO items1 (item_id, description) VALUES ( $i, "<random string of 7 letters>" ); ?



mycursor = mydb.cursor()
# sql="CREATE TABLE new_item(item_id INT NOT NULL ) "

#in range function u can change the limitation
for i in range(2000,3000):
  sql = "INSERT INTO new_item(item_id) VALUES (%s)"
  val = [(i)]
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

#task 2:
# The first random number will be used to create a date.
# The second random number for sales1 is going to be the item_id,
# so use random numbers between 2000 and 1 million. And the
# 3rd one is going to be the amount of sales, so use a number between 1 and 50


# sql="CREATE TABLE new_sale(date date NOT NULL ,item_id INT NOT NULL, amount INT NOT NULL) "
# mycursor.execute(sql)
item_id1=random.randint(2000,3000)
print(item_id1)

amount1=random.randint(1,50)
print(amount1)

date=datetime.date(randint(2005,2025), randint(1,12),randint(1,28))
print(date)

sql = "INSERT INTO new_sale(date,item_id,amount) VALUES (%s,%s,%s)"
val = [(date,item_id1,amount1)]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
