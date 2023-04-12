import pandas as pd
import sqlite3 
import hashlib

conn = sqlite3.connect('data.db')
c = conn.cursor()

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

async def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS usertable(name TEXT,phone INTEGER PRIMARY KEY,password TEXT)')
	
async def create_smstable():
	c.execute('CREATE TABLE IF NOT EXISTS smstable(name TEXT,phone INTEGER,password TEXT,FOREIGN KEY (phone) REFERENCES usertable(phone))')
	
async def create_phonetable():
	c.execute('CREATE TABLE IF NOT EXISTS phonetable(name TEXT,phone INTEGER,password TEXT,FOREIGN KEY (phone) REFERENCES usertable(phone))')
	
async def create_emailtable():
	c.execute('CREATE TABLE IF NOT EXISTS emailtable(name TEXT,phone INTEGER,password TEXT,FOREIGN KEY (phone) REFERENCES usertable(phone))')


async def add_userdata(username,phone,password):
	c.execute('INSERT INTO userstable(username,phone,password) VALUES (?,?,?)', (username,phone,password))
	conn.commit()

async def login_user(username,phone,password):
	c.execute('SELECT * FROM userstable WHERE username = ? AND phone=? AND password = ?', (username,phone,password))
	data = c.fetchall()
	return data

async def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


conn.commit()
conn.close()