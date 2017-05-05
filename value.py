#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

class Posic(QtGui.QWidget):
    def __init__(self):
        super(Posic, self).__init__()

        self.label_2 = QtGui.QLabel("Current value_2:")
        self.spinBox_2 = QtGui.QSpinBox()
        self.spinBox_2 = QtGui.QSpinBox()
        self.spinBox_2.setRange(-1000, 1000)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setValue(23)
        self.a = str(self.spinBox_2.value())
        self.LineView_2 = QtGui.QLineEdit(self.a)
        self.LineView_2.setReadOnly(True)

        self.spinBox_2.valueChanged.connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged.connect(self.LineViewPaste_2)

    def LineViewPaste_2(self):
      print("valueSTR = ", str(self.spinBox_2.value()))
      self.LineView_2.clear()
      self.LineView_2.insert(str(self.spinBox_2.value()))




class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("ValuesSeter")

        self.valueLabel = QtGui.QLabel("Current value:")
        self.SpinBox = QtGui.QSpinBox()
        self.SpinBox.setRange(-1000, 1000)
        self.SpinBox.setSingleStep(1)
        self.SpinBox.setValue(5)
        self.a = str(self.SpinBox.value())
        self.LineView = QtGui.QLineEdit(self.a)
        self.LineView.setReadOnly(True)

        self.SpinBox.valueChanged.connect(self.SpinBox.setValue)
        self.SpinBox.valueChanged.connect(self.LineViewPaste)

        self.label_2 = QtGui.QLabel("Current value_2:")
        self.spinBox_2 = QtGui.QSpinBox()
        self.spinBox_2 = QtGui.QSpinBox()
        self.spinBox_2.setRange(-1000, 1000)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setValue(23)
        self.a = str(self.spinBox_2.value())
        self.LineView_2 = QtGui.QLineEdit(self.a)
        self.LineView_2.setReadOnly(True)

        self.spinBox_2.valueChanged.connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged.connect(self.LineViewPaste_2)

        pos11 = Posic()
        pos13 = Posic()
        pos14 = Posic()

        gridLayout = QtGui.QGridLayout()
        gridLayout.addWidget(self.valueLabel, 0, 0)
        gridLayout.addWidget(self.SpinBox, 0, 1)
        gridLayout.addWidget(self.LineView, 0, 2)

        gridLayout.addWidget(self.label_2, 1, 0)
        gridLayout.addWidget(self.spinBox_2, 1, 1)
        gridLayout.addWidget(self.LineView_2, 1, 2)

        gridLayout.addWidget(pos11(), 3, 0)
        self.setLayout(gridLayout)



    def LineViewPaste(self):
        print("valueSTR = ", str(self.SpinBox.value()))
        self.LineView.clear()
        self.LineView.insert(str(self.SpinBox.value()))

    def LineViewPaste_2(self):
        print("valueSTR = ", str(self.spinBox_2.value()))
        self.LineView_2.clear()
        self.LineView_2.insert(str(self.spinBox_2.value()))




if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
