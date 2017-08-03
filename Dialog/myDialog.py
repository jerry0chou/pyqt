from Dialog.myDialogUi  import Ui_Dialog
from PyQt5 import QtWidgets

class myDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(myDialog, self).__init__()
        self.setupUi(self)

    def accept(self):
        print('username:',self.username.text())
        print('password:',self.password.text())
        print('mobile',self.mobile.text())
        print('male:',self.male.isChecked())
        print('female:', self.female.isChecked())