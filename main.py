from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate
from TodoItem import TodoItem
from PyQt5.QtCore import Qt
from datetime import date
import sqlite3
# from order import quickOrder
class todo(QMainWindow):
    def __init__(self):
        super(todo, self).__init__()
        uic.loadUi("todo.ui", self)
        self.verticalLayout.setAlignment(Qt.AlignTop)
        self.show()
        self.pushButton.setDefault(True)
        self.pushButton.clicked.connect(self.addTodo)
        today = date.today()
        self.due.setDate(QDate(2026, today.month, today.day))
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            due DATE NOT NULL,
            day INTEGER NOT NULL,
            month INTEGER NOT NULL
            )
        ''')
        quickOrder(self)

        # cursor.execute("DROP TABLE todo")
        # conn.commit()
        # conn.close()

    def addTodo(self):
        name = self.name.toPlainText()
        due = self.due.date()
        due = due.toString("dd/MM")
        # day = self.day
        # month = self.month
        # print("Added Task: " + "Name: " + name + ", Due Date: " + due)
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM todo")
        count = cursor.fetchone()[0]
        day = int(due[0:2])
        month = int(due[3:5])
        # print(f"Currently, the table has {count} rows.")
        cursor.execute("INSERT INTO todo VALUES (?, ?, ?, ?, ?)", (count, name, due, day, month))
        self.verticalLayout.addWidget(TodoItem(name, due, count))
        # quickOrder(self)
        self.name.clear()
        # self.due.clear()
        conn.commit()
        conn.close()
        quickOrder(self)


def quickOrder(self):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    print(range(self.verticalLayout.count()))
    for i in reversed(range(self.verticalLayout.count())): 
        self.verticalLayout.itemAt(i).widget().setParent(None)
    for row in cursor.execute("SELECT * FROM TODO ORDER BY month, day;"):
        self.verticalLayout.addWidget(TodoItem(str(row[1]), str(row[2]), row[0]))



def main():
    app = QApplication([])
    window = todo()
    app.exec_()


main()