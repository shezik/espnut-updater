# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QEvent
from FileDialog import FileDialog
from serial.tools.list_ports import comports

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Init UI
        ## Append version to window title
        self.setWindowTitle(self.windowTitle() + ' v0.1')
        ## Init serial port combo box
        self.ui.comboBoxSerialPort.installEventFilter(self)
        self.refreshSerialComboBox()
        self.ui.comboBoxSerialPort.setCurrentIndex(0)
        ## Init baud rate combo box
        self.refreshBaudrateComboBox()

    # Click to refresh serial port list
    def eventFilter(self, object, event):
        if event.type() == QEvent.MouseButtonPress and object == self.ui.comboBoxSerialPort:
            self.refreshSerialComboBox()
        return super().eventFilter(object, event)

    def refreshSerialComboBox(self):
        currentPort = self.ui.comboBoxSerialPort.currentText()
        self.ui.comboBoxSerialPort.clear()
        self.ui.comboBoxSerialPort.addItems(sorted([comport.device for comport in comports()]))
        self.ui.comboBoxSerialPort.setCurrentText(currentPort)

    def refreshBaudrateComboBox(self):
        self.ui.comboBoxBaudrate.clear()
        self.ui.comboBoxBaudrate.addItems(['9600', '57600', '115200', '230400', '460800', '921600', '1500000'])
        self.ui.comboBoxBaudrate.setCurrentText('460800')

    def openBinToWidget(self, widget):
        path = FileDialog(fmt='bin')
        if path != '':
            widget.setText(path)

    def openDirToWidget(self, widget):
        path = FileDialog(isFolder=True)
        if path != '':
            widget.setText(path)

    def openFile_1(self):
        self.openBinToWidget(self.ui.lineEdit_1)
    def openFile_2(self):
        self.openBinToWidget(self.ui.lineEdit_2)
    def openFile_3(self):
        self.openBinToWidget(self.ui.lineEdit_3)
    def openFile_4(self):
        self.openBinToWidget(self.ui.lineEdit_4)

    def openFile_5(self):
        self.openDirToWidget(self.ui.lineEdit_5)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
