#Code to implement flask server
#!/usr/bin/python


#imports
from flask import Flask, render_template, jsonify, Response, redirect, url_for, request
import sqlite3 as sql
import json

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
		if request.form['usr'] != 'admin' or request.form['psw'] != 'admin':
			error = 'Invalid Credentials. Please Try Again'
		else:
			return redirect(url_for('deactivate'))
	return render_template('login.html', error=error)

@app.route('/deactivate')
def deactivate():
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port =2020, debug=True)
