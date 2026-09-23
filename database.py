import psycopg2

from datetime import datetime

today = datetime.now()


conn = psycopg2.connect(host="localhost", port=5432, user="postgres", password="@Lion2020", dbname="ecommerce"
                        )

# perform db operations

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
    cur.execute("insert into products(cartegory_id,supplier_id,product_name,buying_price,selling_price,brand) values(%s,%s,%s,%s,%s,%s)", product)
    conn.commit()


def get_suppliers():
    cur.execute('select * from suppliers')
    suppliers = cur.fetchall()

    return suppliers


def insert_suppliers(supplier):
    cur.execute(
        'insert into suppliers(full_name,address,phone_no,city) values(%s,%s,%s,%s)', supplier)
    conn.commit()


def get_stocks():
    cur.execute("select * from stocks")
    unit = cur.fetchall()

    return unit

#stock = get_stocks()

#print(stock))
def check_available_stock(pid):
    cur.execute('select sum(stock_quantity) from stock where pid= %s', (pid,))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("select sum(quantity) from sales where pid = %s",(pid,))
    total_sold = cur.fetchone()[0] or 0

    return total_stock - total_sold


def add_stocks():
    cur.execute()


def check_available_stock():
    cur.execute()    


def insert_user(user_details):
    cur.execute('insert into users(name, email,address, phone_number, password) values(%s,%s,%s,%s,%s)', user_details)
    conn.commit()

def insert_sale(sale):
    cur.execute("insert into sales(pid,quantity) values(%s,%s)",sale)
    conn.commit()

#sale1 = (7,2)

#insert_sale(sale1)

def check_existing_user(email):
    cur.execute('select * from users where email = %s', (email,))
    user = cur.fetchone()

    return user
