#Code to implement flask server
#!/usr/bin/python


#imports
from flask import Flask, render_template, jsonify, Response, redirect, url_for, request
import sqlite3 as sql
import json
import models as dbHandler

#globals
app = Flask(__name__)
#magic
@app.route("/")
def index():
	return render_template('index.html')

#@app.route('/button')
#def button():
#	return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		username = request.form['usr']
		password = request.form['psw']
		state = dbHandler.checklogin(username, password)
		if(state):
			print("Login Accepted")
			return redirect(url_for('index'))
		else:
			print("Login Rejected")
			error = 'Invalid Credentials. Please Try Again'
			return render_template('login.html', error=error)
	else:
		return render_template('login.html', error=error)
@app.route('/register', methods=['GET', 'POST'])
def register():
        error = None
        if request.method == 'POST':
                username = request.form['usr']
                password = request.form['psw']
		if(dbHandler.checkexist(username)):
			error = 'Username Already Exists'
			return render_template('register.html', error=error)
		else:
	                dbHandler.insertUsers(username, password)
               		return redirect(url_for('index'))
	return render_template('register.html')
@app.route('/deactivate')
def deactivate():
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port =2020, debug=True)
