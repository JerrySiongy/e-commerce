from flask import Flask, render_template, request, redirect, url_for
from database import get_cartegories, get_suppliers, insert_products, insert_suppliers, get_mensprods

app = Flask(__name__)

app.secret_key = 'asjnjkabsfkasdnfafhaiouefaoufheuafejfa230029Siongy254'

@app.route('/') #decorator function
def home(): #view function

    return render_template('index.html')

@app.route('/products')
def products():
    suppliers_data = get_suppliers()

    return render_template('products.html', suppliers_data = suppliers_data)

@app.route('/add_products', methods=['POST', 'GET'])
def add_products():
    if request.method == 'POST':
        cartegory_id = int(request.form['cartegory_id'])
        supplier_id = int(request.form['supplier_id'])
        product_name = request.form['product_name']
        unit = request.form['unit']
        bp = request.form['buying_price']
        sp = request.form['selling_price']
        brand = request.form['brand']
        size = request.form['size']

        new_product = (cartegory_id,supplier_id,product_name,unit,bp,sp,brand,size)
        insert_products(new_product)
        print(f'new_product added')

        return redirect(url_for('dashboard'))
        

@app.route('/add_supplier', methods = ['GET', 'POST'])
def add_supplier():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone_no = request.form['phone_no']
        city = request.form['city']

    new_supplier = (name,address,phone_no,city)

    insert_suppliers(new_supplier)
    print(f'new supplier added')

    return redirect(url_for('dashboard'))


@app.route('/cartegories')
def cartegories():

    cartegories_data = get_cartegories()

    return render_template('cartegories.html', cartegories_data=cartegories_data)

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

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/register')
def register():

    return render_template('register.html')

@app.route('/contact_us')
def contact_us():


    return render_template('contact_us.html')

app.run(debug=True)