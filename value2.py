#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

# class Posic(QtGui.QWidget):
#  def __init__(self):
#     super(Posic, self).__init__()
#
#     self.valueLabel = QtGui.QLabel("Current value:")
#     self.SpinBox = QtGui.QSpinBox()
#     self.SpinBox.setRange(-1000, 1000)
#     self.SpinBox.setSingleStep(1)
#     self.SpinBox.setValue(5)
#     self.a = str(self.SpinBox.value())
#     self.LineView = QtGui.QLineEdit(self.a)
#     self.LineView.setReadOnly(True)
#
#     self.SpinBox.valueChanged.connect(self.SpinBox.setValue)
#     self.SpinBox.valueChanged.connect(self.LineViewPaste)

class MySpinBox(QtGui.QWidget):
 def __init__(self):
    super(MySpinBox, self).__init__()

    self.valueLabel = QtGui.QLabel("Current value:")
    self.SpinBox = QtGui.QSpinBox()
    self.SpinBox.setRange(-1000, 1000)
    self.SpinBox.setSingleStep(1)
    self.SpinBox.setValue(5)
    self.a = str(self.SpinBox.value())

class MyLineView(QtGui.QWidget):
 def __init__(self):
    super(MyLineView, self).__init__()

    self.a = str(789)
    self.LineView = QtGui.QLineEdit(self.a)
    self.LineView.setReadOnly(True)



class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("ValuesSeter")

        self.SpinBox1=MySpinBox()




        # self.SpinBox1.valueChanged.connect(self.SpinBox1.setValue)
        # self.SpinBox1.valueChanged.connect(self.LineViewPaste)

    # def LineViewPaste(self):
    #     print("valueSTR = ", str(self.SpinBox.value()))
    #     self.LineView.clear()
    #     self.LineView.insert(str(self.SpinBox.value()))


        gridLayout = QtGui.QGridLayout()
       # gridLayout.addWidget(self.valueLabel, 0, 0)
        gridLayout.addWidget(self.SpinBox1, 0, 0)
       # gridLayout.addWidget(self.LineView, 0, 2)
        self.setLayout(gridLayout)







if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
