from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
from TodoItem import TodoItem
from PyQt5.QtCore import Qt
import sqlite3
class todo(QMainWindow):
    def __init__(self):
        super(todo, self).__init__()
        uic.loadUi("todo.ui", self)
        self.verticalLayout.setAlignment(Qt.AlignTop)
        self.show()
        self.pushButton.setDefault(True)
        self.pushButton.clicked.connect(self.addTodo)
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            due DATE NOT NULL
            )
        ''')
        for row in cursor.execute("SELECT * from todo"):
            self.verticalLayout.addWidget(TodoItem(str(row[1]), str(row[2]), row[0]))
            print(row[1], row[2], row[0])




        # cursor.execute("DROP TABLE todo")
        # conn.commit()
        # conn.close()


    def addTodo(self):
        print("Added Task: " + "Name: " + self.name.toPlainText() + ", Due Date: " + self.due.toPlainText())
        name = self.name.toPlainText()
        due = self.due.toPlainText()
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM todo")
        count = cursor.fetchone()[0]
        print(f"Currently, the table has {count} rows.")
        cursor.execute("INSERT INTO todo VALUES (?, ?, ?)", (count, name, due))
        self.verticalLayout.addWidget(TodoItem(self.name.toPlainText(), self.due.toPlainText(), count))
        self.name.clear()
        self.due.clear()
        conn.commit()
        conn.close()



def main():
    app = QApplication([])
    window = todo()
    app.exec_()


main()