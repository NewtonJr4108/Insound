from flask import Flask, render_template, redirect, url_for, request, render_template_string, flash, session
from werkzeug.datastructures import ImmutableMultiDict
import os
from pymongo import MongoClient

app = Flask(__name__)

app.secret_key = "your_secret_key"  # Replace with a strong secret key
client = MongoClient('localhost', 27017)
db = client['your_database_name']  # Replace with your MongoDB database name
users_collection = db['users']


@app.route('/')
def main(methods=['POST', 'GET']):
    #option = request.form['option']
    
    return render_template("home.html")
    #return render_template("main.html")
    
    
    
@app.route('/notes',methods = ['GET', 'POST'])
def notes():
    return render_template("main.html")


@app.route('/process', methods=['GET', 'POST'])
def process():
    
    if(request.method == 'POST'):
        global correct
        
        correct_ans_raw = request.form.to_dict()
        #note as string will match that of radio button
        correct = (correct_ans_raw['note'])
        
        #print(correct)

        
        
        
        
    
    return render_template("main.html")




@app.route('/submission', methods = ('GET', 'POST'))
def submission(methods=['POST', 'GET']):
    if(request.method == 'POST'):
        
        option = request.form.getlist('select')
        #print(option)
        #print(correct)
        return render_template_string("The correct answer was "+str(correct)+"\nYou selected "+str(option))
    if(request.method == 'GET'):
        return render_template("main.html")
        
    
'''
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

'''


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        

        # Check if the username already exists
        if users_collection.find_one({'username': username}):
            flash('Username already exists. Choose a different one.', 'danger')
        else:
            users_collection.insert_one({'username': username, 'password': password, 'score':'0'})
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
            #flash('Login successful. welcome '+user['username']+"\nScore: "+user['score'], 'success')
            # Add any additional logic, such as session management
            
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            session['score'] = user['score']
            
            return redirect(url_for('mainpage'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/main')
def mainpage():
    return session['username']

@app.route('/correct', methods=['GET', 'POST'])
def correct():
    if request.method == 'GET':
        return session['score']
    if request.method == 'POST':
        
        #prints entire database, very useful!
        '''
        for x in users_collection.find():
            print(x)
            '''
            
        users_collection.update_one(
            #TODO
            #put update data here
        )
        
    

if __name__ == "__main__":
    
    app.run(debug=True)