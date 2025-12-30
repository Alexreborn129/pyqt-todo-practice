from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

class TodoItem(QWidget): 
    
    def __init__(self, name: str, due: str):
        print(name, due)
        super().__init__()
        uic.loadUi("TodoItem.ui", self)
        self.name.setText(name)
        self.due.setText(due)
        
