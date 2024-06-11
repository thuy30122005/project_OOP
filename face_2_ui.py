# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'face_2.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(878, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Menu = QWidget(self.centralwidget)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(240, 194, 213);\n"
"	color:black;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"QPushButton {\n"
"	text-align:left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:rgb(251, 111, 146);\n"
"	font-weight:bold;\n"
"}")
        self.gridLayout_18 = QGridLayout(self.Menu)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 10, 15, 10)
        self.verticalSpacer_2 = QSpacerItem(20, 241, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.Home = QPushButton(self.Menu)
        self.Home.setObjectName(u"Home")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.Home.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/home_24dp_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home.setIcon(icon)
        self.Home.setIconSize(QSize(25, 25))
        self.Home.setCheckable(True)
        self.Home.setAutoExclusive(True)

        self.gridLayout_18.addWidget(self.Home, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Product = QPushButton(self.Menu)
        self.Product.setObjectName(u"Product")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.Product.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/filter_vintage_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/filter_vintage_1.png", QSize(), QIcon.Normal, QIcon.On)
        self.Product.setIcon(icon1)
        self.Product.setCheckable(True)
        self.Product.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.Product)

        self.Bill = QPushButton(self.Menu)
        self.Bill.setObjectName(u"Bill")
        self.Bill.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/content_paste_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/content_paste_1.png", QSize(), QIcon.Normal, QIcon.On)
        self.Bill.setIcon(icon2)
        self.Bill.setCheckable(True)
        self.Bill.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.Bill)

        self.Revenue = QPushButton(self.Menu)
        self.Revenue.setObjectName(u"Revenue")
        self.Revenue.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/price_change_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/price_change_1.png", QSize(), QIcon.Normal, QIcon.On)
        self.Revenue.setIcon(icon3)
        self.Revenue.setCheckable(True)
        self.Revenue.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.Revenue)


        self.gridLayout_18.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.gridLayout_18.addLayout(self.verticalLayout_5, 6, 0, 1, 1)

        self.logout = QPushButton(self.Menu)
        self.logout.setObjectName(u"logout")
        icon4 = QIcon()
        icon4.addFile(u":/icons/logout_24dp_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon4)
        self.logout.setCheckable(True)
        self.logout.setAutoExclusive(True)

        self.gridLayout_18.addWidget(self.logout, 4, 0, 1, 1)


        self.gridLayout_5.addWidget(self.Menu, 0, 1, 1, 1)

        self.Window = QWidget(self.centralwidget)
        self.Window.setObjectName(u"Window")
        self.Window.setCursor(QCursor(Qt.ArrowCursor))
        self.Window.setFocusPolicy(Qt.NoFocus)
        self.Window.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:black;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Window)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Control = QFrame(self.Window)
        self.Control.setObjectName(u"Control")
        self.Control.setLayoutDirection(Qt.LeftToRight)
        self.Control.setAutoFillBackground(False)
        self.Control.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(240, 194, 213);\n"
"	border-radius: 5px;\n"
"	color:black;\n"
"}\n"
"QPushButton {\n"
"	text-align:center;\n"
"	height: 30px;\n"
"	padding-left:5px;\n"
"	padding-right:5px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"   border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:rgb(0, 0, 0);\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.Control.setFrameShape(QFrame.StyledPanel)
        self.Control.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Control)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.icon_delete = QPushButton(self.Control)
        self.icon_delete.setObjectName(u"icon_delete")
        self.icon_delete.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/icons/delete_24dp_FILL0_wght400_GRAD0_opsz24(1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_delete.setIcon(icon5)
        self.icon_delete.setCheckable(True)
        self.icon_delete.setAutoExclusive(True)

        self.gridLayout.addWidget(self.icon_delete, 0, 1, 1, 1)

        self.icon_fix = QPushButton(self.Control)
        self.icon_fix.setObjectName(u"icon_fix")
        self.icon_fix.setCursor(QCursor(Qt.ArrowCursor))
        self.icon_fix.setMouseTracking(False)
        self.icon_fix.setContextMenuPolicy(Qt.NoContextMenu)
        self.icon_fix.setLayoutDirection(Qt.LeftToRight)
        self.icon_fix.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons/update_24dp_FILL0_wght400_GRAD0_opsz24(1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_fix.setIcon(icon6)
        self.icon_fix.setCheckable(True)
        self.icon_fix.setAutoExclusive(True)

        self.gridLayout.addWidget(self.icon_fix, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_search = QPushButton(self.Control)
        self.icon_search.setObjectName(u"icon_search")
        icon7 = QIcon()
        icon7.addFile(u":/icons/search_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_search.setIcon(icon7)
        self.icon_search.setCheckable(True)
        self.icon_search.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.icon_search)

        self.search = QLineEdit(self.Control)
        self.search.setObjectName(u"search")
        self.search.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout.addWidget(self.search)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 3, 1, 1)

        self.icon_add = QPushButton(self.Control)
        self.icon_add.setObjectName(u"icon_add")
        font2 = QFont()
        font2.setPointSize(11)
        self.icon_add.setFont(font2)
        self.icon_add.setCursor(QCursor(Qt.ArrowCursor))
        self.icon_add.setFocusPolicy(Qt.StrongFocus)
        self.icon_add.setLayoutDirection(Qt.LeftToRight)
        icon8 = QIcon()
        icon8.addFile(u":/icons/add_24dp_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_add.setIcon(icon8)
        self.icon_add.setCheckable(True)
        self.icon_add.setAutoExclusive(True)

        self.gridLayout.addWidget(self.icon_add, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_2.addWidget(self.Control, 0, 1, 1, 1)

        self.icon_menu = QPushButton(self.Window)
        self.icon_menu.setObjectName(u"icon_menu")
        font3 = QFont()
        font3.setPointSize(64)
        self.icon_menu.setFont(font3)
        self.icon_menu.setCursor(QCursor(Qt.ClosedHandCursor))
        self.icon_menu.setStyleSheet(u"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/menu_24dp_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_menu.setIcon(icon9)
        self.icon_menu.setIconSize(QSize(30, 30))
        self.icon_menu.setCheckable(True)

        self.gridLayout_2.addWidget(self.icon_menu, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.Window)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.Home_tab = QWidget()
        self.Home_tab.setObjectName(u"Home_tab")
        self.gridLayout_9 = QGridLayout(self.Home_tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_5 = QWidget(self.Home_tab)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_21 = QGridLayout(self.widget_5)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.verticalSpacer_4 = QSpacerItem(20, 85, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/icons/Screenshot from 2024-06-11 22-40-10.png"))
        self.label_14.setScaledContents(False)

        self.gridLayout_21.addWidget(self.label_14, 0, 2, 3, 1)

        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_12 = QGridLayout(self.widget_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setFamilies([u"URW Gothic"])
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_9.setFont(font4)
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_12.addWidget(self.label_9, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_12.addWidget(self.label_10, 1, 0, 1, 2)


        self.gridLayout_21.addWidget(self.widget_2, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_7, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 84, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_5, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Home_tab)
        self.Product_tab = QWidget()
        self.Product_tab.setObjectName(u"Product_tab")
        self.gridLayout_10 = QGridLayout(self.Product_tab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.price = QLineEdit(self.Product_tab)
        self.price.setObjectName(u"price")

        self.gridLayout_3.addWidget(self.price, 0, 0, 1, 1)

        self.VND = QLabel(self.Product_tab)
        self.VND.setObjectName(u"VND")

        self.gridLayout_3.addWidget(self.VND, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 1, 1, 1)

        self.quantity = QSpinBox(self.Product_tab)
        self.quantity.setObjectName(u"quantity")

        self.gridLayout_4.addWidget(self.quantity, 1, 1, 1, 1)

        self.quantity_label = QLabel(self.Product_tab)
        self.quantity_label.setObjectName(u"quantity_label")

        self.gridLayout_4.addWidget(self.quantity_label, 1, 0, 1, 1)

        self.name_label = QLabel(self.Product_tab)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_4.addWidget(self.name_label, 0, 0, 1, 1)

        self.price_label = QLabel(self.Product_tab)
        self.price_label.setObjectName(u"price_label")

        self.gridLayout_4.addWidget(self.price_label, 2, 0, 1, 1)

        self.name = QLineEdit(self.Product_tab)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.name, 0, 1, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_4, 0, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(286, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.quantity_sort = QComboBox(self.Product_tab)
        self.quantity_sort.addItem("")
        self.quantity_sort.addItem("")
        self.quantity_sort.addItem("")
        self.quantity_sort.setObjectName(u"quantity_sort")

        self.gridLayout_7.addWidget(self.quantity_sort, 1, 1, 1, 1)

        self.price_sort = QComboBox(self.Product_tab)
        self.price_sort.addItem("")
        self.price_sort.addItem("")
        self.price_sort.addItem("")
        self.price_sort.setObjectName(u"price_sort")

        self.gridLayout_7.addWidget(self.price_sort, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_7)

        self.sort_icon_item = QPushButton(self.Product_tab)
        self.sort_icon_item.setObjectName(u"sort_icon_item")
        icon10 = QIcon()
        icon10.addFile(u":/icons/swap_vert_24dp_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sort_icon_item.setIcon(icon10)
        self.sort_icon_item.setCheckable(True)
        self.sort_icon_item.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.sort_icon_item)


        self.gridLayout_10.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(292, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 1, 1, 1, 2)

        self.Product_table = QTableWidget(self.Product_tab)
        if (self.Product_table.columnCount() < 4):
            self.Product_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.Product_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Product_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Product_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Product_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.Product_table.setObjectName(u"Product_table")

        self.gridLayout_10.addWidget(self.Product_table, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.Product_tab)
        self.Bill_tab = QWidget()
        self.Bill_tab.setObjectName(u"Bill_tab")
        self.gridLayout_17 = QGridLayout(self.Bill_tab)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.widget = QWidget(self.Bill_tab)
        self.widget.setObjectName(u"widget")
        self.gridLayout_14 = QGridLayout(self.widget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.name_customer = QLineEdit(self.widget)
        self.name_customer.setObjectName(u"name_customer")

        self.gridLayout_6.addWidget(self.name_customer, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 2, 0, 1, 1)

        self.address = QLineEdit(self.widget)
        self.address.setObjectName(u"address")

        self.gridLayout_6.addWidget(self.address, 2, 1, 1, 1)

        self.phone = QLineEdit(self.widget)
        self.phone.setObjectName(u"phone")

        self.gridLayout_6.addWidget(self.phone, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 3, 0, 1, 1)

        self.email = QLineEdit(self.widget)
        self.email.setObjectName(u"email")

        self.gridLayout_6.addWidget(self.email, 3, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(13)
        self.label.setFont(font5)

        self.gridLayout_14.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.widget_3 = QWidget(self.Bill_tab)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_13 = QGridLayout(self.widget_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.gridLayout_13.addWidget(self.label_11, 0, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.status = QComboBox(self.widget_3)
        self.status.addItem("")
        self.status.addItem("")
        self.status.addItem("")
        self.status.addItem("")
        self.status.setObjectName(u"status")

        self.gridLayout_8.addWidget(self.status, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_8.addWidget(self.label_2, 1, 0, 1, 1)

        self.order_item = QLineEdit(self.widget_3)
        self.order_item.setObjectName(u"order_item")

        self.gridLayout_8.addWidget(self.order_item, 1, 1, 1, 1)

        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_8.addWidget(self.label_12, 2, 0, 1, 1)

        self.order_quantity = QSpinBox(self.widget_3)
        self.order_quantity.setObjectName(u"order_quantity")

        self.gridLayout_8.addWidget(self.order_quantity, 2, 1, 1, 1)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 3, 0, 1, 1)

        self.order_date = QDateEdit(self.widget_3)
        self.order_date.setObjectName(u"order_date")
        self.order_date.setMinimumTime(QTime(0, 0, 0))
        self.order_date.setCalendarPopup(True)
        self.order_date.setCurrentSectionIndex(0)
        self.order_date.setDate(QDate(2024, 1, 1))

        self.gridLayout_8.addWidget(self.order_date, 3, 1, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_8, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_3, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_15, 0, 0, 1, 2)

        self.widget_4 = QWidget(self.Bill_tab)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_16 = QGridLayout(self.widget_4)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_4 = QComboBox(self.widget_4)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_3.addWidget(self.comboBox_4)

        self.comboBox_3 = QComboBox(self.widget_4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.sort_icon_item_2 = QPushButton(self.widget_4)
        self.sort_icon_item_2.setObjectName(u"sort_icon_item_2")
        self.sort_icon_item_2.setIcon(icon10)
        self.sort_icon_item_2.setCheckable(True)
        self.sort_icon_item_2.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.sort_icon_item_2)


        self.gridLayout_16.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.widget_4, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(270, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_10, 1, 1, 1, 1)

        self.Order_table = QTableWidget(self.Bill_tab)
        if (self.Order_table.columnCount() < 11):
            self.Order_table.setColumnCount(11)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem5.setFont(font2);
        self.Order_table.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Order_table.setHorizontalHeaderItem(10, __qtablewidgetitem14)
        self.Order_table.setObjectName(u"Order_table")
        self.Order_table.setFrameShape(QFrame.StyledPanel)
        self.Order_table.setFrameShadow(QFrame.Plain)
        self.Order_table.setLineWidth(1)
        self.Order_table.setMidLineWidth(0)
        self.Order_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Order_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Order_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Order_table.verticalHeader().setDefaultSectionSize(30)

        self.gridLayout_17.addWidget(self.Order_table, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.Bill_tab)
        self.Revenue_tab = QWidget()
        self.Revenue_tab.setObjectName(u"Revenue_tab")
        self.gridLayout_20 = QGridLayout(self.Revenue_tab)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.widget_6 = QWidget(self.Revenue_tab)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_11 = QGridLayout(self.widget_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.grap = QPushButton(self.widget_6)
        self.grap.setObjectName(u"grap")

        self.gridLayout_11.addWidget(self.grap, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.Revenue_table = QTableWidget(self.widget_6)
        if (self.Revenue_table.columnCount() < 3):
            self.Revenue_table.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Revenue_table.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Revenue_table.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Revenue_table.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        self.Revenue_table.setObjectName(u"Revenue_table")

        self.gridLayout_11.addWidget(self.Revenue_table, 1, 0, 1, 2)


        self.gridLayout_20.addWidget(self.widget_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Revenue_tab)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 2)


        self.gridLayout_5.addWidget(self.Window, 0, 2, 1, 1)

        self.Menu_icons = QWidget(self.centralwidget)
        self.Menu_icons.setObjectName(u"Menu_icons")
        self.Menu_icons.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(240, 194, 213);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton {\n"
"	color: black;\n"
"	height: 30px;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.gridLayout_19 = QGridLayout(self.Menu_icons)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalSpacer = QSpacerItem(20, 241, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_19.addLayout(self.verticalLayout_2, 4, 0, 1, 1)

        self.icon_logout = QPushButton(self.Menu_icons)
        self.icon_logout.setObjectName(u"icon_logout")
        self.icon_logout.setIcon(icon4)
        self.icon_logout.setCheckable(True)
        self.icon_logout.setAutoExclusive(True)

        self.gridLayout_19.addWidget(self.icon_logout, 3, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon_Product = QPushButton(self.Menu_icons)
        self.icon_Product.setObjectName(u"icon_Product")
        self.icon_Product.setIcon(icon1)
        self.icon_Product.setCheckable(True)
        self.icon_Product.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.icon_Product)

        self.icon_Bill = QPushButton(self.Menu_icons)
        self.icon_Bill.setObjectName(u"icon_Bill")
        self.icon_Bill.setIcon(icon2)
        self.icon_Bill.setCheckable(True)
        self.icon_Bill.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.icon_Bill)

        self.icon_Revenue = QPushButton(self.Menu_icons)
        self.icon_Revenue.setObjectName(u"icon_Revenue")
        self.icon_Revenue.setIcon(icon3)
        self.icon_Revenue.setCheckable(True)
        self.icon_Revenue.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.icon_Revenue)


        self.gridLayout_19.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.icon_home = QPushButton(self.Menu_icons)
        self.icon_home.setObjectName(u"icon_home")
        self.icon_home.setIcon(icon)
        self.icon_home.setIconSize(QSize(25, 25))
        self.icon_home.setCheckable(True)
        self.icon_home.setAutoExclusive(True)

        self.gridLayout_19.addWidget(self.icon_home, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.Menu_icons, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 878, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.icon_menu.toggled.connect(self.Menu_icons.setHidden)
        self.icon_menu.toggled.connect(self.Menu.setVisible)
        self.icon_Product.toggled.connect(self.Product.setChecked)
        self.icon_Bill.toggled.connect(self.Bill.setChecked)
        self.Product.toggled.connect(self.icon_Product.setChecked)
        self.Bill.toggled.connect(self.icon_Bill.setChecked)
        self.Revenue.toggled.connect(self.icon_Revenue.setChecked)
        self.icon_Revenue.toggled.connect(self.Revenue.setChecked)
        self.Bill.toggled.connect(self.icon_Bill.setChecked)
        self.icon_home.toggled.connect(self.Home.setChecked)
        self.Home.toggled.connect(self.icon_home.setChecked)
        self.logout.clicked["bool"].connect(self.icon_logout.setChecked)
        self.icon_logout.clicked["bool"].connect(self.logout.setChecked)
        self.logout.clicked["bool"].connect(MainWindow.close)
        self.icon_logout.clicked["bool"].connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Home.setText(QCoreApplication.translate("MainWindow", u"Trang ch\u1ee7", None))
        self.Product.setText(QCoreApplication.translate("MainWindow", u"M\u1eb7t H\u00e0ng", None))
        self.Bill.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n H\u00e0ng", None))
        self.Revenue.setText(QCoreApplication.translate("MainWindow", u"Doanh Thu", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng xu\u1ea5t", None))
        self.icon_delete.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.icon_fix.setText(QCoreApplication.translate("MainWindow", u"S\u1eeda", None))
        self.icon_search.setText("")
        self.icon_add.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))
        self.icon_menu.setText("")
        self.label_14.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"XIN CH\u00c0O", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"H\u00f4m nay c\u1eadu c\u00f3 dui hong ??", None))
        self.VND.setText(QCoreApplication.translate("MainWindow", u"VND", None))
        self.quantity_label.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng:", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"T\u00ean:", None))
        self.price_label.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1:", None))
        self.quantity_sort.setItemText(0, QCoreApplication.translate("MainWindow", u"S\u1ed0 L\u01af\u1ee2NG", None))
        self.quantity_sort.setItemText(1, QCoreApplication.translate("MainWindow", u"T\u0103ng d\u1ea7n", None))
        self.quantity_sort.setItemText(2, QCoreApplication.translate("MainWindow", u"Gi\u1ea3m d\u1ea7n", None))

        self.price_sort.setItemText(0, QCoreApplication.translate("MainWindow", u"GI\u00c1", None))
        self.price_sort.setItemText(1, QCoreApplication.translate("MainWindow", u"T\u0103ng d\u1ea7n", None))
        self.price_sort.setItemText(2, QCoreApplication.translate("MainWindow", u"Gi\u1ea3m d\u1ea7n", None))

        self.sort_icon_item.setText("")
        ___qtablewidgetitem = self.Product_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"STT", None));
        ___qtablewidgetitem1 = self.Product_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem2 = self.Product_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng", None));
        ___qtablewidgetitem3 = self.Product_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"T\u00ean kh\u00e1ch h\u00e0ng:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"S\u0111t:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin kh\u00e1ch h\u00e0ng:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin \u0111\u01a1n h\u00e0ng:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i:", None))
        self.status.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0110ang chu\u1ea9n b\u1ecb h\u00e0ng", None))
        self.status.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0110ang giao", None))
        self.status.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0110\u00e3 giao ", None))
        self.status.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0110\u00e3 h\u1ee7y \u0111\u01a1n", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M\u1eb7t h\u00e0ng:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y mua:", None))
        self.order_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Ng\u00e0y", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"C\u0169 h\u01a1n", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"M\u1edbi \u0111\u00e2y", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ed5ng h\u00f3a \u0111\u01a1n", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"T\u0103ng d\u1ea7n", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Gi\u1ea3m d\u1ea7n", None))

        self.sort_icon_item_2.setText("")
        ___qtablewidgetitem4 = self.Order_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"STT", None));
        ___qtablewidgetitem5 = self.Order_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"T\u00ean kh\u00e1ch h\u00e0ng", None));
        ___qtablewidgetitem6 = self.Order_table.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"SDT", None));
        ___qtablewidgetitem7 = self.Order_table.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9", None));
        ___qtablewidgetitem8 = self.Order_table.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem9 = self.Order_table.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"M\u1eb7t h\u00e0ng", None));
        ___qtablewidgetitem10 = self.Order_table.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng", None));
        ___qtablewidgetitem11 = self.Order_table.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1", None));
        ___qtablewidgetitem12 = self.Order_table.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y mua", None));
        ___qtablewidgetitem13 = self.Order_table.horizontalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng h\u00f3a \u0111\u01a1n", None));
        ___qtablewidgetitem14 = self.Order_table.horizontalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None));
        self.grap.setText(QCoreApplication.translate("MainWindow", u"Hi\u1ec3n th\u1ecb bi\u1ec3u \u0111\u1ed3", None))
        ___qtablewidgetitem15 = self.Revenue_table.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"STT", None));
        ___qtablewidgetitem16 = self.Revenue_table.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y \u0111\u1eb7t h\u00e0ng", None));
        ___qtablewidgetitem17 = self.Revenue_table.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng doanh thu", None));
        self.icon_logout.setText("")
        self.icon_Product.setText("")
        self.icon_Bill.setText("")
        self.icon_Revenue.setText("")
        self.icon_home.setText("")
    # retranslateUi

