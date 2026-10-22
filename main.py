from flask import Flask, render_template, request, redirect, url_for,flash, session

from database import get_cartegories, get_suppliers, insert_products, insert_suppliers, get_products, get_stocks, check_existing_user, insert_user,insert_sale, check_available_stock, get_sales, get_users, insert_employee, get_shippers, insert_shippers,get_employees,get_employees_name, get_user


# to encrypt email and password
from flask_bcrypt import Bcrypt



#for the session cookies
from functools import wraps



app = Flask(__name__)


# Bcrypt instance
bcrypt = Bcrypt(app)


app.secret_key = 'asjnjkabsfkasdnfafhaiouefaoufheuafejfa230029Siongy254'


def login_required(f):
    @wraps(f) # decorator function, a superior function, checks whether the user has logged in or not
    def protected(*args,**kwargs): #*args(arguments) **kwargs(key-word arguments)
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected

@app.route('/logout')
def logout():
    session.pop('email',None) # the none is just in case there's no email in session
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


@app.route('/')  # decorator function
def home():  # view function

    return render_template('index.html')


@app.route('/checkout')
def products():
    sales_data = get_sales()
    return render_template('checkout.html',sales_data= sales_data)


@app.route('/add_products', methods=['POST', 'GET'])
def add_products():
    if request.method == 'POST':
        cartegory_id = int(request.form['cartegory_id'])
        supplier_id = int(request.form['supplier_id'])
        product_name = request.form['product_name']
        bp = request.form['buying_price']
        sp = request.form['selling_price']
        brand = request.form['brand']
        new_product = (cartegory_id, supplier_id,
                       product_name, bp, sp, brand)
        insert_products(new_product)
        print(f'new_product added')

        return redirect(url_for('dashboard'))


@app.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone_no = request.form['phone_no']
        city = request.form['city']

    new_supplier = (name, address, phone_no, city)

    insert_suppliers(new_supplier)
    print(f'new supplier added')

    return redirect(url_for('dashboard'))


@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        user_id=int(request.form['user_id'])
        id_no = request.form['id_number']
        role = request.form['role']

        new_employee = (user_id, id_no, role)

        insert_employee(new_employee)


    return render_template('shop.html')      

@app.route('/add_shipper', methods=['GET', 'POST'])
def add_shipper():
    if request.method == 'POST':
        emp_id = request.form['emp_id']

        new_shipper= (emp_id)

        insert_shippers(new_shipper)
        print(f'new shipper added')

    return render_template('dashboard.html')

@app.route('/shop')
def shop():
    stock_data = get_stocks()
    cartegories_data = get_cartegories()
    products_data = get_products()
    return render_template('shop.html', cartegories_data=cartegories_data, products_data=products_data, stock_data=stock_data)




@app.route('/dashboard')
def dashboard():
    suppliers_data = get_suppliers()
    cartegories_data = get_cartegories()
    users_data = get_users()
    products_data = get_products()
    shippers_data=get_shippers()
    employees_data = get_employees()
    emp_name = get_employees_name()
    specific_user = get_user()

    return render_template('dashboard.html', cartegories_data=cartegories_data, suppliers_data=suppliers_data, users_data=users_data, products_data=products_data, shippers_data=shippers_data, employees_data=employees_data, emp_name = emp_name, specific_user=specific_user)

@app.route('/check_user', methods=['GET', 'POST'])
def check_user():

    existing_user = check_existing_user()

    if request.method == 'POST':
        email = request.form['spec_user']


    return redirect(url_for('dashboard'))    




@app.route('/about')
def about():

    return render_template('about.html')


@app.route('/stock')
def units():
    stock_data = get_stocks()

    return render_template('shop.html', stock_data=stock_data)

@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
     if request.method == 'POST':
        pid = request.form['pid']
        stock_quantity = request.form['s_quantity']

        new_stock = (pid, stock_quantity)
        add_stock(new_stock)
        print('stock added successfully')
     return redirect(url_for('dashboard')) 


@app.route('/register',methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        phone_number = request.form['phone_number']
        password = request.form['password']

        existing_user = check_existing_user(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode(
                'utf-8')  # compares the password with the hashed password in database
            new_user = (name, email, address, phone_number,hashed_password)
            insert_user(new_user)
            print('user registered successfully')
            return redirect(url_for("login"))
        else:
            print('User with this email already exists, login instead')

    return render_template('register.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing_user = check_existing_user(email)

        if existing_user:
            # compares the password with the hashed password in database
            if bcrypt.check_password_hash(existing_user[-1], password):

                print('Login successful')

                return redirect(url_for('dashboard'))
            else:
                print('incorrect password')
        else:
            print('User not registerd')

    return render_template('login.html')


@app.route('/contact_us')
def contact_us():

    return render_template('contact_us.html')


@app.route('/sales')
def sales():  # view function

    products_data = get_products() # inorder to show products data in the sales page

    return render_template("sales.html", products_data=products_data)


@app.route('/make_sale', methods=['GET', 'POST'])
def make_sale():
    if request.method == 'POST':
        
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = (pid,quantity)
        insert_sale(new_sale)

    return redirect(url_for("sales"))




app.run(debug=True)
