import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtRemoveInputHook, pyqtSlot
from PyQt5.QtGui import QFont, QKeySequence, QWheelEvent
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QMainWindow,
    QShortcut,
    QTableWidgetItem,
    QTreeWidgetItem,
)

from base.Interpreter import Interpreter

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    pass

Ui_MainWindow, QtBaseClass = uic.loadUiType('layout.ui')


class PyPascalApp(QMainWindow):
    def __init__(self):
        self.interpreter: Interpreter
        self.newLines = 1
        super(PyPascalApp, self).__init__(None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.shortcut_execute = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Return), self)

        self.shortcut_execute.activated.connect(self.interpret)
        self.ui.pushButton.clicked.connect(self.interpret)

        self.ui.scopeComboBox.currentIndexChanged.connect(self.update_scope_table)

    @pyqtSlot()
    def update_scope_table(self):
        if self.ui.scopeTable.rowCount() == 0:
            return

        scope_name = self.ui.scopeComboBox.currentText()
        scope_level = self.ui.scopeTable.findItems(scope_name, Qt.MatchExactly)[0].row()

        self.ui.activationTree.clear()
        self.ui.activationTree.setColumnCount(4)
        self.ui.activationTree.setHeaderLabels(['Name', 'Execution Order', 'Variable', 'Value'])

        activations = self.interpreter.ar_tree.find(scope_name, scope_level)

        if activations:
            item = QTreeWidgetItem(self.ui.activationTree)
            item.setText(0, activations[0].scope_name)
            item.setExpanded(True)

            for activation in activations:
                activation_item = QTreeWidgetItem(item)
                activation_item.setText(1, str(activation.execution_order))
                activation_item.setExpanded(True)

                for member in activation.members:
                    member_item = QTreeWidgetItem(activation_item)
                    member_item.setText(2, member)
                    member_item.setText(3, str(activation.members[member]))
                    member_item.setExpanded(True)

    @pyqtSlot()
    def interpret(self):
        program = self.ui.plainTextEdit.toPlainText()
        self.ui.output.setText('')
        self.ui.output.setStyleSheet('color: black;')

        self.ui.scopeTable.clear()
        self.ui.scopeTable.setRowCount(0)
        self.ui.scopeComboBox.clear()

        try:
            self.interpreter = Interpreter(program)
            self.interpreter.interpret()

            self.ui.scopeTable.setRowCount(self.interpreter.ar_tree.size)
            self.ui.scopeTable.setColumnCount(3)
            self.ui.scopeTable.setHorizontalHeaderLabels(['Name', 'Level', 'Enclosing Scope'])

            row = 0
            for node in self.interpreter.ar_tree.bf_traverse():
                self.ui.scopeTable.setItem(row, 0, QTableWidgetItem(node.scope.scope_name))
                self.ui.scopeTable.setItem(row, 1, QTableWidgetItem(str(node.scope.scope_level)))
                self.ui.scopeTable.setItem(row, 2, QTableWidgetItem(str(node.scope.enclosing_scope)))
                row += 1

                self.ui.scopeComboBox.addItem(node.scope.scope_name)

            for out in self.interpreter.stdout:
                self.ui.output.append(out)

        except Exception as e:
            self.ui.output.setText(str(e))
            self.ui.output.setStyleSheet('color: red;')


if __name__ == '__main__':
    pyqtRemoveInputHook()
    app = QApplication(sys.argv)
    window = PyPascalApp()
    window.setWindowTitle('PyPascal')

    window.show()
    sys.exit(app.exec())
