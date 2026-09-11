from flask import Flask, render_template, request, redirect, url_for
from database import get_cartegories, get_suppliers, insert_products, insert_suppliers, get_products, get_mensprods, get_stocks, check_existing_user, insert_user


# to encrypt email and password
from flask_bcrypt import Bcrypt


app = Flask(__name__)


# Bcrypt instance
bcrypt = Bcrypt(app)


app.secret_key = 'asjnjkabsfkasdnfafhaiouefaoufheuafejfa230029Siongy254'


@app.route('/')  # decorator function
def home():  # view function

    return render_template('index.html')


@app.route('/products')
def products():
    suppliers_data = get_suppliers()
    products_data = get_products()
    return render_template('products.html', suppliers_data=suppliers_data, products_data=products_data)


@app.route('/add_products', methods=['POST', 'GET'])
def add_products():
    if request.method == 'POST':
        cartegory_id = int(request.form['cartegory_id'])
        supplier_id = int(request.form['supplier_id'])
        product_name = request.form['product_name']
        bp = request.form['buying_price']
        sp = request.form['selling_price']
        brand = request.form['brand']
        size = request.form['size']
        new_product = (cartegory_id, supplier_id,
                       product_name, bp, sp, brand, size)
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


@app.route('/shop')
def shop():
    stock_data = get_stocks()
    cartegories_data = get_cartegories()
    products_data = get_products
    return render_template('shop.html', cartegories_data=cartegories_data, products_data=products_data, stock_data=stock_data)


@app.route('/dashboard')
def dashboard():
    suppliers_data = get_suppliers()
    cartegories_data = get_cartegories()

    return render_template('dashboard.html', cartegories_data=cartegories_data, suppliers_data=suppliers_data)

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/cart')
def cart():

    return render_template('cart.html')

@app.route('/units')
def units():
    unit_data = get_stocks()

    return render_template('shop.html', unit_data=unit_data)

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

app.run(debug=True)
