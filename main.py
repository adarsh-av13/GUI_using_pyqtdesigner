# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FPG.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(210, 50, 69, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 120, 69, 25))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 50, 113, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 120, 113, 29))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.check)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "KTU GPA Calculator", None))
        self.comboBox.setItemText(0, _translate("Dialog", "S1", None))
        self.comboBox.setItemText(1, _translate("Dialog", "S2", None))
        self.comboBox.setItemText(2, _translate("Dialog", "S3", None))
        self.comboBox.setItemText(3, _translate("Dialog", "S4", None))
        self.comboBox.setItemText(4, _translate("Dialog", "S5", None))
        self.comboBox.setItemText(5, _translate("Dialog", "S6", None))
        self.comboBox.setItemText(6, _translate("Dialog", "S7", None))
        self.comboBox.setItemText(7, _translate("Dialog", "S8", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "CS", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "ME", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", "EEE", None))
        self.lineEdit.setText(_translate("Dialog", "Semester", None))
        self.lineEdit_2.setText(_translate("Dialog", "Branch", None))
    
    def check(self):
        import sys
        if str(self.comboBox_2.currentText())=="CS" and str(self.comboBox.currentText())=="S4":
            import css4
            Dialog2 = QtGui.QDialog()
            ui2 = css4.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()
        elif str(self.comboBox_2.currentText())=="CS" and str(self.comboBox.currentText())=="S3":
            import css3
            Dialog2 = QtGui.QDialog()
            ui2 = css3.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="CS" and str(self.comboBox.currentText())=="S1":
            import css1
            Dialog2 = QtGui.QDialog()
            ui2 = css1.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="CS" and str(self.comboBox.currentText())=="S2":
            import css2
            Dialog2 = QtGui.QDialog()
            ui2 = css2.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="CS" and str(self.comboBox.currentText())=="S5":
            import css5
            Dialog2 = QtGui.QDialog()
            ui2 = css5.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="CS" and str(self.comboBox.currentText())=="S6":
            import css6
            Dialog2 = QtGui.QDialog()
            ui2 = css6.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="CS" and str(self.comboBox.currentText())=="S7":
            import css7
            Dialog2 = QtGui.QDialog()
            ui2 = css7.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()                        
        elif str(self.comboBox_2.currentText())=="CS" and str(self.comboBox.currentText())=="S8":
            import css8
            Dialog2 = QtGui.QDialog()
            ui2 = css8.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()  
        elif str(self.comboBox_2.currentText())=="EEE" and str(self.comboBox.currentText())=="S4":
            import eees4
            Dialog2 = QtGui.QDialog()
            ui2 = eees4.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()
        elif str(self.comboBox_2.currentText())=="EEE" and str(self.comboBox.currentText())=="S3":
            import eees3
            Dialog2 = QtGui.QDialog()
            ui2 = eees3.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="EEE" and str(self.comboBox.currentText())=="S1":
            import eees1
            Dialog2 = QtGui.QDialog()
            ui2 = eees1.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="EEE" and str(self.comboBox.currentText())=="S2":
            import eees2
            Dialog2 = QtGui.QDialog()
            ui2 = eees2.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="EEE" and str(self.comboBox.currentText())=="S5":
            import eees5
            Dialog2 = QtGui.QDialog()
            ui2 = eees5.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="EEE" and str(self.comboBox.currentText())=="S6":
            import eees6
            Dialog2 = QtGui.QDialog()
            ui2 = eees6.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()    
        elif str(self.comboBox_2.currentText())=="EEE" and str(self.comboBox.currentText())=="S7":
            import eees7
            Dialog2 = QtGui.QDialog()
            ui2 = eees7.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()
        elif str(self.comboBox_2.currentText())=="EEE" and str(self.comboBox.currentText())=="S8":
            import eees8
            Dialog2 = QtGui.QDialog()
            ui2 = eees8.Ui_Dialog()
            ui2.setupUi(Dialog2)
            Dialog.hide()
            Dialog2.exec_()       

                             
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

