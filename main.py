from flask import Flask,render_template
from database import get_cartegories

app = Flask(__name__)

app.secret_key = 'asjnjkabsfkasdnfafhaiouefaoufheuafejfa230029Siongy254'

@app.route('/') #decorator function
def home(): #view function

    return render_template('index.html')

@app.route('/products')
def projects():

    return render_template('products.html')

@app.route('/cartegories')
def services():

    cartegories = get_cartegories()

    return render_template('cartegories.html', cartegories=cartegories)

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