# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 575)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabFlashFirmware = QWidget()
        self.tabFlashFirmware.setObjectName(u"tabFlashFirmware")
        sizePolicy.setHeightForWidth(self.tabFlashFirmware.sizePolicy().hasHeightForWidth())
        self.tabFlashFirmware.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.tabFlashFirmware)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_1 = QLineEdit(self.tabFlashFirmware)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.horizontalLayout_3.addWidget(self.lineEdit_1)

        self.toolButtonBrowse_1 = QToolButton(self.tabFlashFirmware)
        self.toolButtonBrowse_1.setObjectName(u"toolButtonBrowse_1")

        self.horizontalLayout_3.addWidget(self.toolButtonBrowse_1)

        self.toolButtonClear_1 = QToolButton(self.tabFlashFirmware)
        self.toolButtonClear_1.setObjectName(u"toolButtonClear_1")
        self.toolButtonClear_1.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.toolButtonClear_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_2 = QLineEdit(self.tabFlashFirmware)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.toolButtonBrowse_2 = QToolButton(self.tabFlashFirmware)
        self.toolButtonBrowse_2.setObjectName(u"toolButtonBrowse_2")

        self.horizontalLayout_4.addWidget(self.toolButtonBrowse_2)

        self.toolButtonClear_2 = QToolButton(self.tabFlashFirmware)
        self.toolButtonClear_2.setObjectName(u"toolButtonClear_2")

        self.horizontalLayout_4.addWidget(self.toolButtonClear_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_3 = QLineEdit(self.tabFlashFirmware)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_5.addWidget(self.lineEdit_3)

        self.toolButtonBrowse_3 = QToolButton(self.tabFlashFirmware)
        self.toolButtonBrowse_3.setObjectName(u"toolButtonBrowse_3")

        self.horizontalLayout_5.addWidget(self.toolButtonBrowse_3)

        self.toolButtonClear_3 = QToolButton(self.tabFlashFirmware)
        self.toolButtonClear_3.setObjectName(u"toolButtonClear_3")

        self.horizontalLayout_5.addWidget(self.toolButtonClear_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_4 = QLineEdit(self.tabFlashFirmware)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_7.addWidget(self.lineEdit_4)

        self.toolButtonBrowse_4 = QToolButton(self.tabFlashFirmware)
        self.toolButtonBrowse_4.setObjectName(u"toolButtonBrowse_4")

        self.horizontalLayout_7.addWidget(self.toolButtonBrowse_4)

        self.toolButtonClear_4 = QToolButton(self.tabFlashFirmware)
        self.toolButtonClear_4.setObjectName(u"toolButtonClear_4")

        self.horizontalLayout_7.addWidget(self.toolButtonClear_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tabFlashFirmware, "")
        self.tabDownloadFile = QWidget()
        self.tabDownloadFile.setObjectName(u"tabDownloadFile")
        self.horizontalLayout_2 = QHBoxLayout(self.tabDownloadFile)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_5 = QLineEdit(self.tabDownloadFile)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_8.addWidget(self.lineEdit_5)

        self.toolButtonBrowse_5 = QToolButton(self.tabDownloadFile)
        self.toolButtonBrowse_5.setObjectName(u"toolButtonBrowse_5")

        self.horizontalLayout_8.addWidget(self.toolButtonBrowse_5)

        self.toolButtonClear_5 = QToolButton(self.tabDownloadFile)
        self.toolButtonClear_5.setObjectName(u"toolButtonClear_5")

        self.horizontalLayout_8.addWidget(self.toolButtonClear_5)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.tabWidget.addTab(self.tabDownloadFile, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(0, 16, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.labelSerialPort = QLabel(self.centralwidget)
        self.labelSerialPort.setObjectName(u"labelSerialPort")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelSerialPort.sizePolicy().hasHeightForWidth())
        self.labelSerialPort.setSizePolicy(sizePolicy2)
        self.labelSerialPort.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelSerialPort)

        self.comboBoxSerialPort = QComboBox(self.centralwidget)
        self.comboBoxSerialPort.setObjectName(u"comboBoxSerialPort")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBoxSerialPort.sizePolicy().hasHeightForWidth())
        self.comboBoxSerialPort.setSizePolicy(sizePolicy3)
        self.comboBoxSerialPort.setEditable(True)

        self.verticalLayout_3.addWidget(self.comboBoxSerialPort)

        self.labelBaudrate = QLabel(self.centralwidget)
        self.labelBaudrate.setObjectName(u"labelBaudrate")
        sizePolicy2.setHeightForWidth(self.labelBaudrate.sizePolicy().hasHeightForWidth())
        self.labelBaudrate.setSizePolicy(sizePolicy2)
        self.labelBaudrate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelBaudrate)

        self.comboBoxBaudrate = QComboBox(self.centralwidget)
        self.comboBoxBaudrate.setObjectName(u"comboBoxBaudrate")
        sizePolicy3.setHeightForWidth(self.comboBoxBaudrate.sizePolicy().hasHeightForWidth())
        self.comboBoxBaudrate.setSizePolicy(sizePolicy3)
        self.comboBoxBaudrate.setEditable(True)

        self.verticalLayout_3.addWidget(self.comboBoxBaudrate)

        self.verticalSpacer = QSpacerItem(0, 16, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButtonStart = QPushButton(self.centralwidget)
        self.pushButtonStart.setObjectName(u"pushButtonStart")

        self.verticalLayout_3.addWidget(self.pushButtonStart)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.plainTextEditTerminal = QPlainTextEdit(self.centralwidget)
        self.plainTextEditTerminal.setObjectName(u"plainTextEditTerminal")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.plainTextEditTerminal.sizePolicy().hasHeightForWidth())
        self.plainTextEditTerminal.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(12, 12, 12, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(18, 18, 18, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(15, 15, 15, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(6, 6, 6, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(8, 8, 8, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(6, 6, 6, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.plainTextEditTerminal.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.plainTextEditTerminal.setFont(font)
        self.plainTextEditTerminal.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEditTerminal.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.plainTextEditTerminal.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.plainTextEditTerminal.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEditTerminal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolButtonClear_1.clicked.connect(self.lineEdit_1.clear)
        self.toolButtonClear_2.clicked.connect(self.lineEdit_2.clear)
        self.toolButtonClear_3.clicked.connect(self.lineEdit_3.clear)
        self.toolButtonClear_4.clicked.connect(self.lineEdit_4.clear)
        self.toolButtonClear_5.clicked.connect(self.lineEdit_5.clear)
        self.toolButtonBrowse_1.clicked.connect(MainWindow.openFile_1)
        self.toolButtonBrowse_2.clicked.connect(MainWindow.openFile_2)
        self.toolButtonBrowse_3.clicked.connect(MainWindow.openFile_3)
        self.toolButtonBrowse_4.clicked.connect(MainWindow.openFile_4)
        self.toolButtonBrowse_5.clicked.connect(MainWindow.openFile_5)
        self.pushButtonStart.clicked.connect(MainWindow.pushButtonStartClicked)
        self.lineEdit_1.textChanged.connect(MainWindow.updatePushButtonStartAvailability)
        self.lineEdit_2.textChanged.connect(MainWindow.updatePushButtonStartAvailability)
        self.lineEdit_3.textChanged.connect(MainWindow.updatePushButtonStartAvailability)
        self.lineEdit_4.textChanged.connect(MainWindow.updatePushButtonStartAvailability)
        self.lineEdit_5.textChanged.connect(MainWindow.updatePushButtonStartAvailability)
        self.tabWidget.currentChanged.connect(MainWindow.updatePushButtonStartAvailability)
        self.comboBoxSerialPort.currentTextChanged.connect(MainWindow.updatePushButtonStartAvailability)
        self.comboBoxBaudrate.currentTextChanged.connect(MainWindow.updatePushButtonStartAvailability)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"espnut Updater", None))
#if QT_CONFIG(statustip)
        self.lineEdit_1.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 bootloader.bin\uff0c\u7559\u7a7a\u4ee5\u8df3\u8fc7\u6b64\u6587\u4ef6\u7684\u5237\u5199\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"bootloader.bin", None))
#if QT_CONFIG(statustip)
        self.toolButtonBrowse_1.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonBrowse_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButtonClear_1.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonClear_1.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
#if QT_CONFIG(statustip)
        self.lineEdit_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 partitions.bin\uff0c\u7559\u7a7a\u4ee5\u8df3\u8fc7\u6b64\u6587\u4ef6\u7684\u5237\u5199\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"partitions.bin", None))
#if QT_CONFIG(statustip)
        self.toolButtonBrowse_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonBrowse_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButtonClear_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonClear_2.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
#if QT_CONFIG(statustip)
        self.lineEdit_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 boot_app0.bin\uff0c\u7559\u7a7a\u4ee5\u8df3\u8fc7\u6b64\u6587\u4ef6\u7684\u5237\u5199\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"boot_app0.bin", None))
#if QT_CONFIG(statustip)
        self.toolButtonBrowse_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonBrowse_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButtonClear_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonClear_3.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
#if QT_CONFIG(statustip)
        self.lineEdit_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 firmware.bin\uff0c\u7559\u7a7a\u4ee5\u8df3\u8fc7\u6b64\u6587\u4ef6\u7684\u5237\u5199\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"firmware.bin", None))
#if QT_CONFIG(statustip)
        self.toolButtonBrowse_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonBrowse_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButtonClear_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonClear_4.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFlashFirmware), QCoreApplication.translate("MainWindow", u"\u56fa\u4ef6\u5347\u7ea7", None))
#if QT_CONFIG(statustip)
        self.lineEdit_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5305\u542b\u8981\u4e0b\u8f7d\u7684\u6587\u4ef6\u7684\u76ee\u5f55\uff0c\u8be5\u76ee\u5f55\u4e0b\u7684\u6240\u6709\u6587\u4ef6\u5c06\u88ab\u4e0b\u8f7d\u81f3\u8bbe\u5907\u4e2d\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u76ee\u5f55", None))
#if QT_CONFIG(statustip)
        self.toolButtonBrowse_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u5939\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonBrowse_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButtonClear_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButtonClear_5.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDownloadFile), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4e0b\u8f7d", None))
        self.labelSerialPort.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None))
#if QT_CONFIG(statustip)
        self.comboBoxSerialPort.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e32\u53e3\u8bbe\u5907\u3002", None))
#endif // QT_CONFIG(statustip)
        self.comboBoxSerialPort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6682\u65e0", None))
        self.labelBaudrate.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
#if QT_CONFIG(statustip)
        self.comboBoxBaudrate.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e0e\u8bbe\u5907\u901a\u4fe1\u7684\u6ce2\u7279\u7387\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushButtonStart.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5237\u5199\u8fc7\u7a0b\u3002", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonStart.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
#if QT_CONFIG(statustip)
        self.plainTextEditTerminal.setStatusTip(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u6267\u884c\u8f93\u51fa\u3002", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

