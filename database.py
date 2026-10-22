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


def insert_cart(cartegory):
    cur.execute('insert into cartegories(cartegory_name, description) values(%s,%s)',cartegory)
    conn.commit()

#cart6= ('collections', 'collections from the best brands') 

#insert_cart(cart6)
cart  = get_cartegories()
#print(cart)

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
    cur.execute('select sum(stock_quantity) from stocks where pid= %s', (pid,))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("select sum(quantity) from sales where pid = %s",(pid,))
    total_sold = cur.fetchone()[0] or 0

    return total_stock - total_sold



def add_stock(stock):

    cur.execute("insert into stocks(pid,stock_quantity) values(%s,%s)", stock)
    conn.commit()




def insert_user(user_details):
    cur.execute('insert into users(name, email,address, phone_number, password) values(%s,%s,%s,%s,%s)', user_details)
    conn.commit()

def insert_sale(sale):
    cur.execute("insert into sales(pid,quantity) values(%s,%s)",sale)
    conn.commit()

#sale1 = (7,2)

#insert_sale(sale1)

def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    
    return sales

def get_orders():
    cur.execute('select * from orders')
    orders = cur.fetchall()

    return orders

def insert_orders(order):
    cur.execute("insert into orders(pid,quantity) values(%s,%s)",order)
    conn.commit()


def get_employees():
    cur.execute('select * from employees')
    employees = cur.fetchall()
    
    return employees

def get_employees_name():
    cur.execute('select employees.id as id, name from employees inner join users on employees.user_id = users.id')
    emp_name = cur.fetchall()

    return emp_name


def insert_employee(employee):
    cur.execute('insert into employees(user_id,id_no,role) values(%s,%s,%s)', employee)
    conn.commit()

def get_shippers():
    cur.execute("select * from shippers")
    shippers = cur.fetchall()

    return shippers

def insert_shippers(shipper):
    cur.execute('insert into shippers(employee_id) values(%s)', shipper)
    conn.commit()


#all_shippers = get_shippers()
#print(all_shippers)

def get_orderdetails():
    cur.execute('select * from orderdetails')
    orderdetails = cur.fetchall()
    
    return orderdetails


def get_users():
    cur.execute('select * from users')
    users = cur.fetchall()

    return users


def check_existing_user(email):
    cur.execute('select * from users where email = %s', (email,))
    user = cur.fetchone()

    return user

def get_reviews():
    cur.execute("select * from reviews")
    reviews = cur.fetchall()

    return reviews




def get_user(email):
    cur.execute('select * from users where email = %s',(email,))
    user = cur.fetchone()
    return user

#email = input('enter email: ')






