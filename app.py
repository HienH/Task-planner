#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:49:50 2019

@author: hienh
"""
import sqlite3
import random
import datetime
import requests
from flask import Flask,render_template,request,jsonify,url_for, flash, redirect
from db import *
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def addtasks():
    now = datetime.datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M")
    if now.hour < 12:
        greeting = 'good morning'
    elif now.hour > 12 and now.hour < 17:
        greeting = 'good afternoon'
    else:
        greeting = 'Hello'
    if request.method == 'GET':
        
      return render_template('index.html', title='todoss', **locals())

    if request.method == 'POST':
      id = request.form['delete']

      conn = getDb()

      cursor = conn.cursor()

      cursor.execute('delete from todos where id = ?',(id,))
      conn.commit()


      return render_template('index.html', title='All todos', **locals())



@app.route("/addtask")
def asktasks():
    return render_template("add_data.html", title = "add data")


@app.route("/complete",methods=["POST"])
def addtask():
    
    
    conn = getDb()
    cursor = conn.cursor()
    title=request.form["task_title"]
    description=request.form["description"]
    result = request.form.getlist("checkbox")
    if result != []:
        result = 'Yes'
    else:
        result= 'No'
    important = result
    status = 0
    date = request.form["date"]
    cursor.execute('INSERT INTO todos(title, description, important, status, date) VALUES(?,?,?,?,?)',( title, description, important,status,date))
    conn.commit()
    
    
    
    now = datetime.datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M")
    if now.hour < 12:
        greeting = 'good morning'
    elif now.hour > 12 and now.hour < 17:
        greeting = 'good afternoon'
    else:
        greeting = 'hello'
    return render_template('complete.html', **locals())


@app.route("/todos", methods = ["GET"])
def all_todo():
   conn = getDb()
   cursor = conn.cursor()
   query = cursor.execute("SELECT * FROM todos")
   results = query.fetchall()
   jsondict = []
   for row in results:
       todo = {
            'id' : row[0],
            'title' : row[1],
            'description' : row[2],
            'important' : row[3],
            'status' : row[4],
            'data' : row[5]
            }

       jsondict.append(todo)
   conn.close()
   return jsonify(jsondict)


##
@app.route("/update", methods = ["POST"])
def update():
    id = request.form['update']
    url = 'update/'+id
    return render_template ('add_data_update.html',**locals())


#@app.route("/update", methods = ["POST"])
#def update():
#    id = str(request.form['update'])
#    url = '127.0.0.1:5000/update/'+str(id)
#    return redirect(url)
    
@app.route('/update_todo', methods=['GET'])
def update_todos():
#    conn = getDb()
#    cursor = conn.cursor()
#    query = cursor.execute("SELECT * FROM todos WHERE ID = ?",(id,))
#    results = query.fetchall()
#    
#    title=request.form["update_task_title"]
#    description=request.form["update_description"]
#    result = request.form.getlist("checkbox1")
#    if result != []:
#        result = 'Yes'
#    else:
#        result= 'No'
#    important = result
#    status = 0
#    date = request.form["update_date"]
    return render_template('complete_update.html', title='All todos', **locals())

    



@app.route('/update/<int:id>', methods=['GET'])
def update_todo(id):
   conn = getDb()
   cursor = conn.cursor()
   query = cursor.execute("SELECT * FROM todos WHERE ID = ?",(id,))
   results = query.fetchall()
   jsondict = []
   for row in results:
       todo = {
            'id' : row[0],
            'title' : row[1],
            'description' : row[2],
            'important' : row[3],
            'status' : row[4],
            'data' : row[5]
            }

       jsondict.append(todo)
   return jsonify(jsondict)


if __name__ == '__main__':
    app.run(debug =True)
