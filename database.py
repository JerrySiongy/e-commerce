import psycopg2

from datetime import datetime

today = datetime.now()


conn = psycopg2.connect(host="localhost", port=5432, user="postgres", password="@Lion2020",dbname="ecommerce"
)

#perform db operations

cur = conn.cursor()

def get_cartegories():
    cur.execute("select * from cartegories")
    cartegories = cur.fetchall()
    
    return cartegories

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()

    return products

products = get_products()

print(products)

def insert_products():
    cur.execute("insert into products")
