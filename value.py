#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

# class Posic(QtGui.QWidget):
#     def __init__(self):
#         super(Posic, self).__init__()
#
#         self.label_2 = QtGui.QLabel("Current value_2:")
#         self.spinBox_2 = QtGui.QSpinBox()
#         self.spinBox_2 = QtGui.QSpinBox()
#         self.spinBox_2.setRange(-1000, 1000)
#         self.spinBox_2.setSingleStep(1)
#         self.spinBox_2.setValue(23)
#         self.a = str(self.spinBox_2.value())
#         self.LineView_2 = QtGui.QLineEdit(self.a)
#         self.LineView_2.setReadOnly(True)
#
#         self.spinBox_2.valueChanged.connect(self.spinBox_2.setValue)
#         self.spinBox_2.valueChanged.connect(self.LineViewPaste_2)
#
#     def LineViewPaste_2(self):
#       print("valueSTR = ", str(self.spinBox_2.value()))
#       self.LineView_2.clear()
#       self.LineView_2.insert(str(self.spinBox_2.value()))




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

        self.label_3 = QtGui.QLabel("Current value_3:")
        self.spinBox_3 = QtGui.QSpinBox()
        self.spinBox_3 = QtGui.QSpinBox()
        self.spinBox_3.setRange(-1000, 1000)
        self.spinBox_3.setSingleStep(1)
        self.spinBox_3.setValue(23)
        self.a = str(self.spinBox_3.value())
        self.LineView_3 = QtGui.QLineEdit(self.a)
        self.LineView_3.setReadOnly(True)

        self.spinBox_3.valueChanged.connect(self.spinBox_3.setValue)
        self.spinBox_3.valueChanged.connect(self.LineViewPaste_3)

        self.label_4 = QtGui.QLabel("Current value_4:")
        self.spinBox_4 = QtGui.QSpinBox()
        self.spinBox_4 = QtGui.QSpinBox()
        self.spinBox_4.setRange(-1000, 1000)
        self.spinBox_4.setSingleStep(1)
        self.spinBox_4.setValue(23)
        self.a = str(self.spinBox_4.value())
        self.LineView_4 = QtGui.QLineEdit(self.a)
        self.LineView_4.setReadOnly(True)

        self.spinBox_4.valueChanged.connect(self.spinBox_4.setValue)
        self.spinBox_4.valueChanged.connect(self.LineViewPaste_4)

        self.label_5 = QtGui.QLabel("Current value_5:")
        self.spinBox_5 = QtGui.QSpinBox()
        self.spinBox_5 = QtGui.QSpinBox()
        self.spinBox_5.setRange(-1000, 1000)
        self.spinBox_5.setSingleStep(1)
        self.spinBox_5.setValue(23)
        self.a = str(self.spinBox_5.value())
        self.LineView_5 = QtGui.QLineEdit(self.a)
        self.LineView_5.setReadOnly(True)

        self.spinBox_5.valueChanged.connect(self.spinBox_5.setValue)
        self.spinBox_5.valueChanged.connect(self.LineViewPaste_5)

        self.label_6 = QtGui.QLabel("Current value_6:")
        self.spinBox_6 = QtGui.QSpinBox()
        self.spinBox_6 = QtGui.QSpinBox()
        self.spinBox_6.setRange(-1000, 1000)
        self.spinBox_6.setSingleStep(1)
        self.spinBox_6.setValue(23)
        self.a = str(self.spinBox_6.value())
        self.LineView_6 = QtGui.QLineEdit(self.a)
        self.LineView_6.setReadOnly(True)

        self.spinBox_6.valueChanged.connect(self.spinBox_6.setValue)
        self.spinBox_6.valueChanged.connect(self.LineViewPaste_6)

        self.label_7 = QtGui.QLabel("Current value_7:")
        self.spinBox_7 = QtGui.QSpinBox()
        self.spinBox_7 = QtGui.QSpinBox()
        self.spinBox_7.setRange(-1000, 1000)
        self.spinBox_7.setSingleStep(1)
        self.spinBox_7.setValue(23)
        self.a = str(self.spinBox_7.value())
        self.LineView_7 = QtGui.QLineEdit(self.a)
        self.LineView_7.setReadOnly(True)

        self.spinBox_7.valueChanged.connect(self.spinBox_7.setValue)
        self.spinBox_7.valueChanged.connect(self.LineViewPaste_7)

        self.label_8 = QtGui.QLabel("Current value_8:")
        self.spinBox_8 = QtGui.QSpinBox()
        self.spinBox_8 = QtGui.QSpinBox()
        self.spinBox_8.setRange(-1000, 1000)
        self.spinBox_8.setSingleStep(1)
        self.spinBox_8.setValue(23)
        self.a = str(self.spinBox_8.value())
        self.LineView_8 = QtGui.QLineEdit(self.a)
        self.LineView_8.setReadOnly(True)

        self.spinBox_8.valueChanged.connect(self.spinBox_8.setValue)
        self.spinBox_8.valueChanged.connect(self.LineViewPaste_8)


        # for i in range (10):
        self.label_9 = QtGui.QLabel("Current value_9:")
        self.spinBox_9 = QtGui.QSpinBox()
        self.spinBox_9 = QtGui.QSpinBox()
        self.spinBox_9.setRange(-1000, 1000)
        self.spinBox_9.setSingleStep(1)
        self.spinBox_9.setValue(23)
        self.a = str(self.spinBox_9.value())
        self.LineView_9 = QtGui.QLineEdit(self.a)
        self.LineView_9.setReadOnly(True)

        self.spinBox_9.valueChanged.connect(self.spinBox_9.setValue)
        self.spinBox_9.valueChanged.connect(self.LineViewPaste_9)







        gridLayout = QtGui.QGridLayout()
        gridLayout.addWidget(self.valueLabel, 0, 0)
        gridLayout.addWidget(self.SpinBox, 0, 1)
        gridLayout.addWidget(self.LineView, 0, 2)

        gridLayout.addWidget(self.label_2, 1, 0)
        gridLayout.addWidget(self.spinBox_2, 1, 1)
        gridLayout.addWidget(self.LineView_2, 1, 2)

        gridLayout.addWidget(self.label_3, 3, 0)
        gridLayout.addWidget(self.spinBox_3, 3, 1)
        gridLayout.addWidget(self.LineView_3, 3, 2)

        gridLayout.addWidget(self.label_4, 4, 0)
        gridLayout.addWidget(self.spinBox_4, 4, 1)
        gridLayout.addWidget(self.LineView_4, 4, 2)


        gridLayout.addWidget(self.label_5, 5, 0)
        gridLayout.addWidget(self.spinBox_5, 5, 1)
        gridLayout.addWidget(self.LineView_5, 5, 2)

        gridLayout.addWidget(self.label_6, 6, 0)
        gridLayout.addWidget(self.spinBox_6, 6, 1)
        gridLayout.addWidget(self.LineView_6, 6, 2)

        gridLayout.addWidget(self.label_7, 7, 0)
        gridLayout.addWidget(self.spinBox_7, 7, 1)
        gridLayout.addWidget(self.LineView_7, 7, 2)

        gridLayout.addWidget(self.label_8, 8, 0)
        gridLayout.addWidget(self.spinBox_8, 8, 1)
        gridLayout.addWidget(self.LineView_8, 8, 2)

        gridLayout.addWidget(self.label_9, 9, 0)
        gridLayout.addWidget(self.spinBox_9, 9, 1)
        gridLayout.addWidget(self.LineView_9, 9, 2)

        self.setLayout(gridLayout)



    def LineViewPaste(self):
        print("valueSTR = ", str(self.SpinBox.value()))
        self.LineView.clear()
        self.LineView.insert(str(self.SpinBox.value()))

    def LineViewPaste_2(self):
        print("valueSTR = ", str(self.spinBox_2.value()))
        self.LineView_2.clear()
        self.LineView_2.insert(str(self.spinBox_2.value()))

    def LineViewPaste_3(self):
        print("valueSTR = ", str(self.spinBox_3.value()))
        self.LineView_3.clear()
        self.LineView_3.insert(str(self.spinBox_3.value()))

    def LineViewPaste_4(self):
        print("valueSTR = ", str(self.spinBox_4.value()))
        self.LineView_4.clear()
        self.LineView_4.insert(str(self.spinBox_4.value()))

    def LineViewPaste_5(self):
        print("valueSTR = ", str(self.spinBox_5.value()))
        self.LineView_5.clear()
        self.LineView_5.insert(str(self.spinBox_5.value()))

    def LineViewPaste_6(self):
        print("valueSTR = ", str(self.spinBox_6.value()))
        self.LineView_6.clear()
        self.LineView_6.insert(str(self.spinBox_6.value()))

    def LineViewPaste_7(self):
        print("valueSTR = ", str(self.spinBox_7.value()))
        self.LineView_7.clear()
        self.LineView_7.insert(str(self.spinBox_7.value()))

    def LineViewPaste_8(self):
        print("valueSTR = ", str(self.spinBox_8.value()))
        self.LineView_8.clear()
        self.LineView_8.insert(str(self.spinBox_8.value()))

    def LineViewPaste_9(self):
        print("valueSTR = ", str(self.spinBox_9.value()))
        self.LineView_9.clear()
        self.LineView_9.insert(str(self.spinBox_9.value()))


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
