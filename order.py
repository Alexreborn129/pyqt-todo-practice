from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
from TodoItem import TodoItem
from PyQt5.QtCore import Qt
import sqlite3



def order():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM TODO ORDER BY month, day;"):
        





order()