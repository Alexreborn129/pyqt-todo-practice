from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
from TodoItem import TodoItem

class todo(QMainWindow):
    def __init__(self):
        super(todo, self).__init__()
        uic.loadUi("todo.ui", self)
        self.show()
        self.pushButton.clicked.connect(self.addTodo)


    def addTodo(self):
        self.verticalLayout.addWidget(TodoItem(self.name.toPlainText(), self.due.toPlainText()))
        print("Added Task: " + "Name: " + self.name.toPlainText() + ", Due Date: " + self.due.toPlainText())
        self.name.clear()
        self.due.clear()




def main():
    app = QApplication([])
    window = todo()
    app.exec_()


main()