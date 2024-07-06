from flask import Flask, render_template, redirect, url_for, request, render_template_string
from werkzeug.datastructures import ImmutableMultiDict
import os
app = Flask(__name__)


@app.route('/')
def main(methods=['POST', 'GET']):
    #option = request.form['option']
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
        
    

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)



    

if __name__ == "__main__":
    
    app.run(debug=True)