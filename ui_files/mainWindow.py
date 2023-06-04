# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"    border: None;\n"
"}\n"
"QPushButton::menu-indicator{\n"
"    width:0px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-radius:10px;\n"
"    padding-left:5px;\n"
"    padding-right:10px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 103, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setEnabled(True)
        self.widget_6.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_compress = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_compress.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/compress.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_compress.setIcon(icon)
        self.pushButton_compress.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_compress.setObjectName("pushButton_compress")
        self.horizontalLayout_3.addWidget(self.pushButton_compress)
        self.pushButton_extract = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_extract.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/de-compress.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_extract.setIcon(icon1)
        self.pushButton_extract.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_extract.setObjectName("pushButton_extract")
        self.horizontalLayout_3.addWidget(self.pushButton_extract)
        self.pushButton_add_folder = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_add_folder.setEnabled(False)
        self.pushButton_add_folder.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/add-folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add_folder.setIcon(icon2)
        self.pushButton_add_folder.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_add_folder.setObjectName("pushButton_add_folder")
        self.horizontalLayout_3.addWidget(self.pushButton_add_folder)
        self.pushButton_add_file = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_add_file.setEnabled(False)
        self.pushButton_add_file.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/add-database-script.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add_file.setIcon(icon3)
        self.pushButton_add_file.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_add_file.setObjectName("pushButton_add_file")
        self.horizontalLayout_3.addWidget(self.pushButton_add_file)
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(200, 200))
        self.widget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.menu_button = QtWidgets.QPushButton(self.widget_4)
        self.menu_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_button.setIcon(icon4)
        self.menu_button.setIconSize(QtCore.QSize(24, 24))
        self.menu_button.setObjectName("menu_button")
        self.horizontalLayout_5.addWidget(self.menu_button, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addWidget(self.widget_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_9 = QtWidgets.QWidget(self.widget_7)
        self.widget_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.back_button = QtWidgets.QPushButton(self.widget_9)
        self.back_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/nav-arrow-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon5)
        self.back_button.setIconSize(QtCore.QSize(28, 28))
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_7.addWidget(self.back_button)
        self.forward_button = QtWidgets.QPushButton(self.widget_9)
        self.forward_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/nav-arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward_button.setIcon(icon6)
        self.forward_button.setIconSize(QtCore.QSize(28, 28))
        self.forward_button.setObjectName("forward_button")
        self.horizontalLayout_7.addWidget(self.forward_button)
        self.horizontalLayout_6.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.widget_7)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_path = QtWidgets.QLineEdit(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_path.setSizePolicy(sizePolicy)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.verticalLayout_3.addWidget(self.lineEdit_path)
        self.horizontalLayout_6.addWidget(self.widget_10)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.treeWidget = QtWidgets.QTreeWidget(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.horizontalLayout_8.addWidget(self.treeWidget)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_drag_and_drop = QtWidgets.QWidget(self.widget_3)
        self.widget_drag_and_drop.setMinimumSize(QtCore.QSize(700, 70))
        self.widget_drag_and_drop.setStyleSheet("QWidget#widget_drag_and_drop{\n"
"border:  4px dashed #aaaaaa\n"
"}")
        self.widget_drag_and_drop.setObjectName("widget_drag_and_drop")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_drag_and_drop)
        self.horizontalLayout_9.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_drop = QtWidgets.QLabel(self.widget_drag_and_drop)
        self.label_drop.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_drop.setFont(font)
        self.label_drop.setStyleSheet("color:rgb(170, 170, 170);")
        self.label_drop.setAlignment(QtCore.Qt.AlignCenter)
        self.label_drop.setObjectName("label_drop")
        self.horizontalLayout_9.addWidget(self.label_drop, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_drag_and_drop, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archive Manager"))
        self.pushButton_compress.setText(_translate("MainWindow", "Compress"))
        self.pushButton_extract.setText(_translate("MainWindow", "Extract"))
        self.label.setText(_translate("MainWindow", "Archive Manager"))
        self.forward_button.setShortcut(_translate("MainWindow", "Enter"))
        self.label_drop.setText(_translate("MainWindow", "Drop Files Here"))
import icons_rc
