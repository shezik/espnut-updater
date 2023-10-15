# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QEvent
from serial.tools.list_ports import comports
from FileDialog import FileDialog
from Flasher import Flasher
from enum import Enum

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainwindow import Ui_MainWindow

class ButtonState(Enum):
    Start = 0
    StartUnavailable = 1
    Stop = 2
    ForceStop = 3

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Init UI
        self._btn_state = ButtonState.Start
        ## Append version to window title
        self.setWindowTitle(self.windowTitle() + ' v0.1')
        ## Init serial port combo box
        self.ui.comboBoxSerialPort.installEventFilter(self)
        self.refreshSerialComboBox()
        self.ui.comboBoxSerialPort.setCurrentIndex(0)
        ## Init baud rate combo box
        self.refreshBaudrateComboBox()
        ## Init start button state
        self.updatePushButtonStartAvailability()
        # Init Flasher
        self.flasher = Flasher(self.ui.plainTextEditTerminal)
        self.flasher.RegisterFinishCallback(self.updatePushButtonStartState)

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

    # Triggered on lineEdit text change and tab change
    def updatePushButtonStartAvailability(self):
        if self._btn_state != ButtonState.Start:
            return

        if self.ui.tabWidget.currentIndex() == 0:
            self.ui.pushButtonStart.setEnabled(len(self.ui.comboBoxSerialPort.currentText()) > 0 \
                                           and len(self.ui.comboBoxBaudrate.currentText())   > 0 \
                                           and len(self.ui.lineEdit_1.text()) \
                                             + len(self.ui.lineEdit_2.text()) \
                                             + len(self.ui.lineEdit_3.text()) \
                                             + len(self.ui.lineEdit_4.text()) > 0)
        elif self.ui.tabWidget.currentIndex() == 1:
            self.ui.pushButtonStart.setEnabled(len(self.ui.comboBoxSerialPort.currentText()) > 0 \
                                           and len(self.ui.comboBoxBaudrate.currentText())   > 0 \
                                           and len(self.ui.lineEdit_5.text()) > 0)


    def updatePushButtonStartState(self):
        self._btn_state = ButtonState.Start
        self.ui.pushButtonStart.setText(self.tr('开始'))
        self.ui.pushButtonStart.setStatusTip(self.tr('开始刷写过程。'))
        self.updatePushButtonStartAvailability()

    def pushButtonStartClicked(self):
        if self._btn_state == ButtonState.Start:
            self._btn_state = ButtonState.Stop
            self.ui.pushButtonStart.setText(self.tr('取消'))
            self.ui.pushButtonStart.setStatusTip(self.tr('取消刷写过程。'))
            if self.ui.tabWidget.currentIndex() == 0:
                self.flasher.Flash(self.ui.comboBoxSerialPort.currentText(), \
                                   self.ui.comboBoxBaudrate.currentText(), \
                                   self.ui.lineEdit_1.text(), \
                                   self.ui.lineEdit_2.text(), \
                                   self.ui.lineEdit_3.text(), \
                                   self.ui.lineEdit_4.text())
            elif self.ui.tabWidget.currentIndex() == 1:
                self.flasher.FlashFS(self.ui.comboBoxSerialPort.currentText(), \
                                     self.ui.comboBoxBaudrate.currentText(), \
                                     self.ui.lineEdit_5.text(), \
                                     './littlefs.bin')
        elif self._btn_state == ButtonState.Stop:
            self._btn_state = ButtonState.ForceStop
            self.ui.pushButtonStart.setText(self.tr('强制停止'))
            self.ui.pushButtonStart.setStatusTip(self.tr('强制停止刷写过程，这具有一定风险。'))
            self.flasher.Terminate()
        elif self._btn_state == ButtonState.ForceStop:
            self.ui.pushButtonStart.setEnabled(False)
            self.flasher.Kill()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
