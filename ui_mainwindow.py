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
        self.lineEdit = QLineEdit(self.tabFlashFirmware)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.tabFlashFirmware)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_3.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.tabFlashFirmware)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.toolButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_2 = QLineEdit(self.tabFlashFirmware)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.toolButton_3 = QToolButton(self.tabFlashFirmware)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_4.addWidget(self.toolButton_3)

        self.toolButton_4 = QToolButton(self.tabFlashFirmware)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.horizontalLayout_4.addWidget(self.toolButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_3 = QLineEdit(self.tabFlashFirmware)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_5.addWidget(self.lineEdit_3)

        self.toolButton_5 = QToolButton(self.tabFlashFirmware)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.horizontalLayout_5.addWidget(self.toolButton_5)

        self.toolButton_6 = QToolButton(self.tabFlashFirmware)
        self.toolButton_6.setObjectName(u"toolButton_6")

        self.horizontalLayout_5.addWidget(self.toolButton_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_4 = QLineEdit(self.tabFlashFirmware)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_7.addWidget(self.lineEdit_4)

        self.toolButton_7 = QToolButton(self.tabFlashFirmware)
        self.toolButton_7.setObjectName(u"toolButton_7")

        self.horizontalLayout_7.addWidget(self.toolButton_7)

        self.toolButton_8 = QToolButton(self.tabFlashFirmware)
        self.toolButton_8.setObjectName(u"toolButton_8")

        self.horizontalLayout_7.addWidget(self.toolButton_8)


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

        self.toolButton_9 = QToolButton(self.tabDownloadFile)
        self.toolButton_9.setObjectName(u"toolButton_9")

        self.horizontalLayout_8.addWidget(self.toolButton_9)

        self.toolButton_10 = QToolButton(self.tabDownloadFile)
        self.toolButton_10.setObjectName(u"toolButton_10")

        self.horizontalLayout_8.addWidget(self.toolButton_10)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.tabWidget.addTab(self.tabDownloadFile, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(0, 16, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy3)
        self.comboBox.setEditable(True)

        self.verticalLayout_3.addWidget(self.comboBox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy3.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy3)
        self.comboBox_2.setEditable(True)

        self.verticalLayout_3.addWidget(self.comboBox_2)

        self.verticalSpacer = QSpacerItem(0, 16, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy4)
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
        self.plainTextEdit.setPalette(palette)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"espnut Updater", None))
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 bootloader.bin\uff0c\u7559\u7a7a\u4ee5\u8df3\u8fc7\u6b64\u6587\u4ef6\u7684\u5237\u5199\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"bootloader.bin", None))
#if QT_CONFIG(statustip)
        self.toolButton.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButton_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
#if QT_CONFIG(statustip)
        self.lineEdit_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 partitions.bin\uff0c\u7559\u7a7a\u4ee5\u8df3\u8fc7\u6b64\u6587\u4ef6\u7684\u5237\u5199\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"partitions.bin", None))
#if QT_CONFIG(statustip)
        self.toolButton_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButton_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
#if QT_CONFIG(statustip)
        self.lineEdit_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 boot_app0.bin\uff0c\u7559\u7a7a\u4ee5\u8df3\u8fc7\u6b64\u6587\u4ef6\u7684\u5237\u5199\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"boot_app0.bin", None))
#if QT_CONFIG(statustip)
        self.toolButton_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButton_6.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
#if QT_CONFIG(statustip)
        self.lineEdit_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9 firmware.bin\uff0c\u7559\u7a7a\u4ee5\u8df3\u8fc7\u6b64\u6587\u4ef6\u7684\u5237\u5199\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"firmware.bin", None))
#if QT_CONFIG(statustip)
        self.toolButton_7.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButton_8.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_8.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFlashFirmware), QCoreApplication.translate("MainWindow", u"\u56fa\u4ef6\u5347\u7ea7", None))
#if QT_CONFIG(statustip)
        self.lineEdit_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5305\u542b\u8981\u4e0b\u8f7d\u7684\u6587\u4ef6\u7684\u76ee\u5f55\uff0c\u8be5\u76ee\u5f55\u4e0b\u7684\u6240\u6709\u6587\u4ef6\u5c06\u88ab\u4e0b\u8f7d\u81f3\u8bbe\u5907\u4e2d\u3002", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u76ee\u5f55", None))
#if QT_CONFIG(statustip)
        self.toolButton_9.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u5939\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_9.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.toolButton_10.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.toolButton_10.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDownloadFile), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4e0b\u8f7d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None))
#if QT_CONFIG(statustip)
        self.comboBox.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e32\u53e3\u8bbe\u5907\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
#if QT_CONFIG(statustip)
        self.comboBox_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e0e\u8bbe\u5907\u901a\u4fe1\u7684\u6ce2\u7279\u7387\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushButton_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5237\u5199\u8fc7\u7a0b\u3002", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
#if QT_CONFIG(statustip)
        self.plainTextEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u6267\u884c\u8f93\u51fa\u3002", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

