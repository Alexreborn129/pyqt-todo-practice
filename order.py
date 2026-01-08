from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
from TodoItem import TodoItem
from PyQt5.QtCore import Qt
import sqlite3



# def order():
#     conn = sqlite3.connect('todo.db')
#     cursor = conn.cursor()
#     for row in cursor.execute("SELECT * FROM TODO ORDER BY month, day;"):



def quickOrder(self):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    print(range(self.verticalLayout.count()))
    for i in reversed(range(self.verticalLayout.count())): 
        self.verticalLayout.itemAt(i).widget().setParent(None)
    for row in cursor.execute("SELECT * FROM TODO ORDER BY month, day;"):
        self.verticalLayout.addWidget(TodoItem(str(row[1]), str(row[2]), row[0]))


# order()