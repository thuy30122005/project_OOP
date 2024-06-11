# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 303)
        Dialog.setStyleSheet(u"background-color: rgb(247, 218, 230);\n"
"color: rgb(0, 0, 0);")
        self.gridLayout_4 = QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"	color:black;\n"
"	border-radius:10px;\n"
"\n"
"}")
        self.Login_tab = QWidget()
        self.Login_tab.setObjectName(u"Login_tab")
        self.gridLayout_2 = QGridLayout(self.Login_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(9, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.widget = QWidget(self.Login_tab)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 5)

        self.register_2 = QPushButton(self.widget)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setStyleSheet(u"\n"
"border-color: rgb(0, 0, 0);")
        self.register_2.setCheckable(True)

        self.gridLayout.addWidget(self.register_2, 4, 1, 1, 1)

        self.login = QPushButton(self.widget)
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"border-color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.login, 4, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.user_name = QLineEdit(self.widget)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.user_name, 0, 2, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 4, 4, 1, 1)

        self.password = QLineEdit(self.widget)
        self.password.setObjectName(u"password")
        self.password.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password, 1, 2, 1, 3)

        self.horizontalSpacer_5 = QSpacerItem(299, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 0, 1, 5)

        self.horizontalSpacer_4 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(11)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 2, 1, 1, 1)

        self.widget_3 = QWidget(self.Login_tab)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_4.setFont(font2)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.Login_tab)
        self.Register_tab = QWidget()
        self.Register_tab.setObjectName(u"Register_tab")
        self.gridLayout_9 = QGridLayout(self.Register_tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(87, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.widget_4 = QWidget(self.Register_tab)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_5.setFont(font3)
        self.label_5.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_5.addWidget(self.widget_4, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(87, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.Register_tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(246, 245, 244);}")
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(92, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_9, 2, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)

        self.confirm = QLineEdit(self.widget_2)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.confirm.setEchoMode(QLineEdit.Password)

        self.gridLayout_8.addWidget(self.confirm, 2, 1, 1, 1)

        self.password_1 = QLineEdit(self.widget_2)
        self.password_1.setObjectName(u"password_1")
        self.password_1.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.password_1.setEchoMode(QLineEdit.Password)

        self.gridLayout_8.addWidget(self.password_1, 1, 1, 1, 1)

        self.user_name_1 = QLineEdit(self.widget_2)
        self.user_name_1.setObjectName(u"user_name_1")
        self.user_name_1.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.gridLayout_8.addWidget(self.user_name_1, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 3)

        self.horizontalSpacer_10 = QSpacerItem(91, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_10, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.register_1 = QPushButton(self.widget_2)
        self.register_1.setObjectName(u"register_1")
        self.register_1.setStyleSheet(u"border-color: rgb(0, 0, 0);")

        self.gridLayout_7.addWidget(self.register_1, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 1, 1, 2, 1)


        self.gridLayout_9.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Register_tab)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"M\u1eadt kh\u1ea9u:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"N\u1ebfu b\u1ea1n ch\u01b0a c\u00f3 t\u00e0i kho\u1ea3n h\u00e3y b\u1ea5m \u0111\u0103ng k\u00ed ", None))
        self.register_2.setText(QCoreApplication.translate("Dialog", u"\u0110\u0103ng k\u00ed", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"\u0110\u0103ng nh\u1eadp", None))
        self.user_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"T\u00ean \u0111\u0103ng nh\u1eadp", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Dialog", u"M\u1eadt kh\u1ea9u", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"T\u00ean \u0111\u0103ng nh\u1eadp:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"XIN CH\u00c0O !!!", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0110\u0102NG K\u00cd", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Nh\u1eadp l\u1ea1i m\u1eadt kh\u1ea9u:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"M\u1eadt kh\u1ea9u:", None))
        self.confirm.setText("")
        self.confirm.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nh\u1eadp l\u1ea1i", None))
        self.password_1.setText("")
        self.password_1.setPlaceholderText(QCoreApplication.translate("Dialog", u"M\u1eadt kh\u1ea9u", None))
        self.user_name_1.setText("")
        self.user_name_1.setPlaceholderText(QCoreApplication.translate("Dialog", u"T\u00ean \u0111\u0103ng nh\u1eadp", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"T\u00ean \u0111\u0103ng nh\u1eadp:", None))
        self.register_1.setText(QCoreApplication.translate("Dialog", u"\u0110\u0103ng k\u00ed", None))
    # retranslateUi

