from PyQt5.QtWidgets import QMessageBox, QPushButton


class Popup():
    def __init__(self, parent=None):
        self.parent = parent

    def message(self, mType, message, buttonStatusOk=False, buttonStatusYes=False, buttonStatusNo=False,
                buttonOpen=False, buttonCancel=False):
        messageBox = QMessageBox()
        # <------ Information / Warning / Question / Critical ------>
        if mType == "Information":
            messageBox.setIcon(QMessageBox.Information)
        elif mType == "Warning":
            messageBox.setIcon(QMessageBox.Warning)
        elif mType == "Question":
            messageBox.setIcon(QMessageBox.Question)
        elif mType == "Critical":
            messageBox.setIcon(QMessageBox.Critical)

        messageBox.setText(message)
        messageBox.setWindowTitle(mType)
        if not buttonStatusOk == False:
            messageBox.addButton(QMessageBox.Ok)
        if not buttonStatusYes == False:
            messageBox.addButton(QMessageBox.Yes)
        if not buttonStatusNo == False:
            messageBox.addButton(QMessageBox.No)
        if not buttonOpen == False:
            messageBox.addButton(QPushButton("Open"), QMessageBox.YesRole)
        if not buttonCancel == False:
            messageBox.addButton(QPushButton("Cancel"), QMessageBox.NoRole)

        messageBox.exec_()