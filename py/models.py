import sqlite3 as sql

def insertUsers(username, password):
	con = sql.connect("../logs/users2.db")
	cur = con.cursor()
	cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
	con.commit()
	con.close()

def retrieveUsers():
	con = sql.connect("../logs/users2.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users

def checklogin(username, password):
	con = sql.connect("../logs/users2.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users WHERE username=? AND password=?", (username,password))
	if cur.fetchone() is not None:
		con.close()
		return True
	else:
		con.close()
		return False

def checkexist(username):
	con = sql.connect("../logs/users2.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if cur.fetchone() is  None:
		con.close()
		return False
	else:
		con.close()
		return True
