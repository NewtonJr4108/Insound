from flask import Flask, render_template, render_template_string, url_for, request, redirect, flash
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key
client = MongoClient('localhost', 27017)
db = client['your_database_name']  # Replace with your MongoDB database name
users_collection = db['users']



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        if users_collection.find_one({'username': username}):
            flash('Username already exists. Choose a different one.', 'danger')
        else:
            users_collection.insert_one({'username': username, 'password': password})
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            flash('Login successful. welcome '+user['username'], 'success')
            # Add any additional logic, such as session management
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')
