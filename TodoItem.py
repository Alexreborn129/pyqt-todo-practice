from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
import time
import random
from PyQt5 import QtCore, QtWidgets
import sqlite3

class TodoItem(QWidget): 
    
    def __init__(self, name: str, due: str, id: int):
        print(id)
        super().__init__()
        uic.loadUi("TodoItem.ui", self)
        self.name.setText(name)
        self.due.setText(due)
        self.id = id
        self.done.stateChanged.connect(self.checked)
        
    def checked(self):
        self.done.setEnabled(False)
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todo WHERE id=?", (self.id,))
        print("DELETED: " + str(self.id))
        conn.commit()
        conn.close()
        disintegrate_widget_local(self, finished=self.deleteLater)


def disintegrate_widget_local(widget, *, tile=8, duration=420, scatter=80, finished=None):
    """
    Disintegrates ONLY inside `widget` bounds (clipped to widget rect).
    Works best for list items / rows inside layouts.
    """

    # Snapshot the widget
    pixmap = widget.grab()
    w, h = pixmap.width(), pixmap.height()

    # Overlay is a CHILD of the widget (so it is clipped to widget rect)
    overlay = QtWidgets.QWidget(widget)
    overlay.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
    overlay.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
    overlay.setGeometry(widget.rect())
    overlay.raise_()
    overlay.show()

    # Hide ONLY the widget's existing content, not the widget itself
    hidden_children = []
    for child in widget.findChildren(QtWidgets.QWidget):
        if child is overlay:
            continue
        if child.isVisible():
            hidden_children.append(child)
            child.setVisible(False)

    group = QtCore.QParallelAnimationGroup(overlay)

    for y in range(0, h, tile):
        for x in range(0, w, tile):
            rect = QtCore.QRect(x, y, min(tile, w - x), min(tile, h - y))
            part = pixmap.copy(rect)

            label = QtWidgets.QLabel(overlay)
            label.setPixmap(part)
            label.setGeometry(rect)
            label.show()

            opacity = QtWidgets.QGraphicsOpacityEffect(label)
            label.setGraphicsEffect(opacity)
            opacity.setOpacity(1.0)

            dx = random.randint(-scatter, scatter)
            dy = random.randint(-scatter, scatter) - scatter // 3

            move = QtCore.QPropertyAnimation(label, b"pos", overlay)
            move.setDuration(duration)
            move.setStartValue(label.pos())
            move.setEndValue(label.pos() + QtCore.QPoint(dx, dy))
            move.setEasingCurve(QtCore.QEasingCurve.OutCubic)

            fade = QtCore.QPropertyAnimation(opacity, b"opacity", overlay)
            fade.setDuration(duration)
            fade.setStartValue(1.0)
            fade.setEndValue(0.0)
            fade.setEasingCurve(QtCore.QEasingCurve.OutQuad)

            delay = (x + y) // (tile * 2)

            sm = QtCore.QSequentialAnimationGroup(overlay)
            sm.addPause(delay * 6)
            sm.addAnimation(move)

            sf = QtCore.QSequentialAnimationGroup(overlay)
            sf.addPause(delay * 6)
            sf.addAnimation(fade)

            group.addAnimation(sm)
            group.addAnimation(sf)

    def cleanup():
        overlay.deleteLater()
        if finished:
            finished()
        else:
            # If you're NOT deleting the widget, restore children:
            for c in hidden_children:
                c.setVisible(True)

    group.finished.connect(cleanup)
    group.start(QtCore.QAbstractAnimation.DeleteWhenStopped)