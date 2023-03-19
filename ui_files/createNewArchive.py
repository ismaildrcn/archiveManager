# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createNewArchive.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 305)
        Form.setMaximumSize(QtCore.QSize(550, 320))
        Form.setStyleSheet("QPushButton{\n"
"    border:None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 7px;\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QComboBox{\n"
"    border-radius:4px;\n"
"}\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(0, 103, 255);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 5px;\n"
"     padding-left: 10px;\n"
" }\n"
"\n"
"QComboBox:on{\n"
"    border-radius:10px;\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"    color: black;\n"
"    background-color: rgb(52, 101, 164);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox:!on{\n"
"    color: black;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancel_button = QtWidgets.QPushButton(self.widget_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon)
        self.cancel_button.setIconSize(QtCore.QSize(20, 20))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_button = QtWidgets.QPushButton(self.widget_5)
        self.create_button.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/folder-settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_button.setIcon(icon1)
        self.create_button.setIconSize(QtCore.QSize(20, 20))
        self.create_button.setObjectName("create_button")
        self.horizontalLayout_2.addWidget(self.create_button)
        self.horizontalLayout.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignTop)
        self.widget_2 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_8 = QtWidgets.QWidget(self.widget_2)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_11 = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_11)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(186, 189, 182);\n"
"    border: none;\n"
"    border-radius:7px;\n"
"    color: rgba(0, 0, 0, 240);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 103, 255);\n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.horizontalLayout_5.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_8)
        self.widget_12.setMaximumSize(QtCore.QSize(120, 16777215))
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_archive_format = QtWidgets.QComboBox(self.widget_12)
        self.comboBox_archive_format.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_archive_format.setFont(font)
        self.comboBox_archive_format.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.comboBox_archive_format.setObjectName("comboBox_archive_format")
        self.comboBox_archive_format.addItem("")
        self.comboBox_archive_format.addItem("")
        self.comboBox_archive_format.addItem("")
        self.comboBox_archive_format.addItem("")
        self.comboBox_archive_format.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_archive_format)
        self.horizontalLayout_5.addWidget(self.widget_12)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(self.widget_2)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 15))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget_7)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_10 = QtWidgets.QWidget(self.widget_2)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox_archive_location = QtWidgets.QComboBox(self.widget_10)
        self.comboBox_archive_location.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_archive_location.setFont(font)
        self.comboBox_archive_location.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.comboBox_archive_location.setObjectName("comboBox_archive_location")
        self.horizontalLayout_7.addWidget(self.comboBox_archive_location)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.widget_9 = QtWidgets.QWidget(self.widget_2)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.widget_9)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "New Archive"))
        self.create_button.setText(_translate("Form", "Create"))
        self.label_2.setText(_translate("Form", "Filename:"))
        self.comboBox_archive_format.setItemText(0, _translate("Form", ".zip"))
        self.comboBox_archive_format.setItemText(1, _translate("Form", ".rar"))
        self.comboBox_archive_format.setItemText(2, _translate("Form", ".tar"))
        self.comboBox_archive_format.setItemText(3, _translate("Form", ".tar.gz"))
        self.comboBox_archive_format.setItemText(4, _translate("Form", ".tar.xz"))
        self.label_3.setText(_translate("Form", "Location:"))
        self.label_4.setText(_translate("Form", "Other Options"))
from ui_files import icons_rc