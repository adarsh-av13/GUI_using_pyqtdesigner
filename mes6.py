# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'css4.ui'
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

gradeDict = {
  "O":10,
  "A+":9,
  "A":8.5,
  "B+":8,
  "B":7,
  "C":6,
  "P":5,
  "F":0
}

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(799, 569)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(430, 500, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 111, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 80, 111, 29))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 140, 113, 29))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 200, 113, 29))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 260, 113, 29))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 330, 113, 29))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(20, 390, 113, 29))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 460, 113, 29))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(20, 500, 113, 29))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(200, 20, 69, 25))
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
        self.comboBox_2.setGeometry(QtCore.QRect(200, 80, 69, 25))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(200, 140, 69, 25))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_4 = QtGui.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(200, 200, 69, 25))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_5 = QtGui.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(200, 260, 69, 25))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_6 = QtGui.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(200, 330, 69, 25))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_7 = QtGui.QComboBox(Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(200, 390, 69, 25))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_8 = QtGui.QComboBox(Dialog)
        self.comboBox_8.setGeometry(QtCore.QRect(200, 460, 69, 25))
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_9 = QtGui.QComboBox(Dialog)
        self.comboBox_9.setGeometry(QtCore.QRect(200, 500, 69, 25))
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.calc)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Grade Card", None))
        self.lineEdit.setText(_translate("Dialog", "ME 302", None))
        self.lineEdit_2.setText(_translate("Dialog", "ME 304", None))
        self.lineEdit_3.setText(_translate("Dialog", "ME 306", None))
        self.lineEdit_4.setText(_translate("Dialog", "ME 308", None))
        self.lineEdit_5.setText(_translate("Dialog", "ME 312", None))
        self.lineEdit_6.setText(_translate("Dialog", "Elective 2", None))
        self.lineEdit_7.setText(_translate("Dialog", "ME 352", None))
        self.lineEdit_8.setText(_translate("Dialog", "ME 332", None))
        self.lineEdit_9.setText(_translate("Dialog", "ME 334", None))
        self.comboBox.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox.setItemText(7, _translate("Dialog", "F", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox_2.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox_2.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox_2.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox_2.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox_2.setItemText(7, _translate("Dialog", "F", None))
        self.comboBox_3.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox_3.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox_3.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox_3.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox_3.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox_3.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox_3.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox_3.setItemText(7, _translate("Dialog", "F", None))
        self.comboBox_4.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox_4.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox_4.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox_4.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox_4.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox_4.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox_4.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox_4.setItemText(7, _translate("Dialog", "F", None))
        self.comboBox_5.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox_5.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox_5.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox_5.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox_5.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox_5.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox_5.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox_5.setItemText(7, _translate("Dialog", "F", None))
        self.comboBox_6.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox_6.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox_6.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox_6.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox_6.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox_6.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox_6.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox_6.setItemText(7, _translate("Dialog", "F", None))
        self.comboBox_7.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox_7.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox_7.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox_7.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox_7.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox_7.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox_7.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox_7.setItemText(7, _translate("Dialog", "F", None))
        self.comboBox_8.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox_8.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox_8.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox_8.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox_8.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox_8.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox_8.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox_8.setItemText(7, _translate("Dialog", "F", None))
        self.comboBox_9.setItemText(0, _translate("Dialog", "O", None))
        self.comboBox_9.setItemText(1, _translate("Dialog", "A+", None))
        self.comboBox_9.setItemText(2, _translate("Dialog", "A", None))
        self.comboBox_9.setItemText(3, _translate("Dialog", "B+", None))
        self.comboBox_9.setItemText(4, _translate("Dialog", "B", None))
        self.comboBox_9.setItemText(5, _translate("Dialog", "C", None))
        self.comboBox_9.setItemText(6, _translate("Dialog", "P", None))
        self.comboBox_9.setItemText(7, _translate("Dialog", "F", None))

    def calc(self):
        sum=0.0
        credSum=23
        sum+=gradeDict[str(self.comboBox.currentText())]*4
        sum+=gradeDict[str(self.comboBox_2.currentText())]*3
        sum+=gradeDict[str(self.comboBox_3.currentText())]*3
        sum+=gradeDict[str(self.comboBox_4.currentText())]*3
        sum+=gradeDict[str(self.comboBox_5.currentText())]*3
        sum+=gradeDict[str(self.comboBox_6.currentText())]*3
        sum+=gradeDict[str(self.comboBox_7.currentText())]*2
        sum+=gradeDict[str(self.comboBox_8.currentText())]*1
        sum+=gradeDict[str(self.comboBox_9.currentText())]*1
        sum/=credSum

        msg=QtGui.QMessageBox()
        msg.setWindowTitle("GPA")
        msg.setText("Your GPA is "+str(sum))
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

