#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:35:16 2019

@author: hienh
"""

import sqlite3
import random

import requests

def getDb():
    conn = sqlite3.connect('Todolist.db')
    return conn

conn = getDb()


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todos(ID INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(255), description VARCHAR(600), important REAL, status REAL,date REAL)')

create_table(conn)
