from flask import Flask, render_template, redirect, url_for, request

import os
app = Flask(__name__)


@app.route('/')
def main(methods=['POST', 'GET']):
    #option = request.form['option']
    return render_template("main.html")


@app.route('/submission', methods = ('GET', 'POST'))
def submission(methods=['POST', 'GET']):
    if(request.method == 'POST'):
        
        option = request.form.getlist('select')
        print(option)
        return option
    if(request.method == 'GET'):
        return render_template("main.html")
        
    

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/process', methods=['GET', 'POST'])
def process():
    
    data = request.form.get('data') 
    # process the data using Python code 
    #result = data.upper() 
    
    return render_template("main.html")

    

if __name__ == "__main__":
    
    app.run(debug=True)