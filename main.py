import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtRemoveInputHook, pyqtSlot
from PyQt5.QtGui import QFont, QKeySequence, QWheelEvent
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QShortcut

from base.Interpreter import Interpreter

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    pass

Ui_MainWindow, QtBaseClass = uic.loadUiType('layout.ui')


class PyPascalApp(QMainWindow):
    def __init__(self):
        self.newLines = 1
        super(PyPascalApp, self).__init__(None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.shortcut_execute = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Return), self)
        self.shortcut_execute.activated.connect(self.interpret)

        self.ui.pushButton.clicked.connect(self.interpret)
        self.ui.textEdit.setReadOnly(True)
        self.ui.textEdit.setFont(QFont('Courier', 14))
        self.ui.textEdit.setStyleSheet('QTextEdit:focus { border: 1px solid grey; }')
        self.ui.textEdit_2.setReadOnly(True)
        self.ui.textEdit_2.setFont(QFont('Courier', 14))
        self.ui.textEdit_2.setStyleSheet('QTextEdit:focus { border: 1px solid grey; }')

    @pyqtSlot()
    def interpret(self):
        program = self.ui.plainTextEdit.toPlainText()

        try:
            interpreter = Interpreter(program)
            interpreter.interpret()
            scope = interpreter.GLOBAL_SCOPE
            symtab = interpreter.symtab_builder.symtab.symbols
            self.ui.textEdit.setPlainText('\n'.join([f'{k}: {scope[k]}' for k in sorted(scope.keys())]))
            self.ui.textEdit.setStyleSheet('color: black')
            self.ui.textEdit_2.setPlainText('\n'.join([f'{i}' for i in symtab.values()]))

        except Exception as e:
            self.ui.textEdit.setPlainText(str(e))
            self.ui.textEdit.setStyleSheet('color: red')
            self.ui.textEdit_2.setPlainText('')


if __name__ == '__main__':
    pyqtRemoveInputHook()
    app = QApplication(sys.argv)
    window = PyPascalApp()
    window.setWindowTitle('PyPascal')

    window.show()
    sys.exit(app.exec())
