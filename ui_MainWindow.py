# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(329, 161)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)

        self.verticalLayout_1.addWidget(self.label)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.xRadioButton = QRadioButton(self.centralwidget)
        self.xRadioButton.setObjectName(u"xRadioButton")
        self.xRadioButton.setFont(font1)
        self.xRadioButton.setChecked(True)

        self.horizontalLayout_1.addWidget(self.xRadioButton)

        self.yRadioButton = QRadioButton(self.centralwidget)
        self.yRadioButton.setObjectName(u"yRadioButton")
        self.yRadioButton.setFont(font1)

        self.horizontalLayout_1.addWidget(self.yRadioButton)

        self.zRadioButton = QRadioButton(self.centralwidget)
        self.zRadioButton.setObjectName(u"zRadioButton")
        self.zRadioButton.setFont(font1)

        self.horizontalLayout_1.addWidget(self.zRadioButton)


        self.verticalLayout_1.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 0))
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.fwdShortPushButton = QPushButton(self.centralwidget)
        self.fwdShortPushButton.setObjectName(u"fwdShortPushButton")
        self.fwdShortPushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.fwdShortPushButton)

        self.fwdMiddlePushButton = QPushButton(self.centralwidget)
        self.fwdMiddlePushButton.setObjectName(u"fwdMiddlePushButton")
        self.fwdMiddlePushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.fwdMiddlePushButton)

        self.fwdLongPushButton = QPushButton(self.centralwidget)
        self.fwdLongPushButton.setObjectName(u"fwdLongPushButton")
        self.fwdLongPushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.fwdLongPushButton)


        self.verticalLayout_1.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 0))
        self.label_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.backShortPushButton = QPushButton(self.centralwidget)
        self.backShortPushButton.setObjectName(u"backShortPushButton")
        self.backShortPushButton.setFont(font1)

        self.horizontalLayout_4.addWidget(self.backShortPushButton)

        self.backMiddlePushButton = QPushButton(self.centralwidget)
        self.backMiddlePushButton.setObjectName(u"backMiddlePushButton")
        self.backMiddlePushButton.setFont(font1)

        self.horizontalLayout_4.addWidget(self.backMiddlePushButton)

        self.backLongPushButton = QPushButton(self.centralwidget)
        self.backLongPushButton.setObjectName(u"backLongPushButton")
        self.backLongPushButton.setFont(font1)

        self.horizontalLayout_4.addWidget(self.backLongPushButton)


        self.verticalLayout_1.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Control StackShot", None))
        self.xRadioButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.yRadioButton.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.zRadioButton.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Forward", None))
        self.fwdShortPushButton.setText(QCoreApplication.translate("MainWindow", u"short", None))
        self.fwdMiddlePushButton.setText(QCoreApplication.translate("MainWindow", u"middle", None))
        self.fwdLongPushButton.setText(QCoreApplication.translate("MainWindow", u"long", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.backShortPushButton.setText(QCoreApplication.translate("MainWindow", u"short", None))
        self.backMiddlePushButton.setText(QCoreApplication.translate("MainWindow", u"middle", None))
        self.backLongPushButton.setText(QCoreApplication.translate("MainWindow", u"long", None))
    # retranslateUi

