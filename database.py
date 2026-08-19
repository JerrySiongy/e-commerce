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

def get_mensprods():
    cur.execute('select * from products where cartegory_id=1;')
    mensprods = cur.fetchall

    return mensprods
def get_shoesprods():
    cur.execute('select * from products where cartegory_id=3;')
    mensprods = cur.fetchall

    return mensprods
def get_womensprods():
    cur.execute('select * from products where cartegory_id=2;')
    mensprods = cur.fetchall

    return mensprods
def get_accessoriesprods():
    cur.execute('select * from products where cartegory_id=4;')
    mensprods = cur.fetchall

    return mensprods

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()

    return products


def insert_products(product):
    cur.execute("insert into products(cartegory_id,supplier_id,product_name,unit,buying_price,selling_price,brand,size) values(%s,%s,%s,%s,%s,%s,%s,%s)",product)
    conn.commit()


def get_suppliers():
    cur.execute('select * from suppliers')
    suppliers = cur.fetchall()

    return suppliers


def insert_suppliers(supplier):
    cur.execute('insert into suppliers(full_name,address,phone_no,city) values(%s,%s,%s,%s)', supplier)
    conn.commit()