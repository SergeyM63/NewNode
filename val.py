#!/usr/bin/env python

from PyQt4 import QtCore, QtGui


class SlidersGroup(QtGui.QGroupBox):
    valueChanged = QtCore.pyqtSignal(int)

    def __init__(self, orientation, title, parent=None):
        super(SlidersGroup, self).__init__(title, parent)

        self.slider = QtGui.QSlider(orientation)
        self.slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.slider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.slider.setTickInterval(5)
        self.slider.setSingleStep(1)

        self.slider.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.valueChanged)

        slidersLayout = QtGui.QBoxLayout(0)
        slidersLayout.addWidget(self.slider)
        self.setLayout(slidersLayout)

    def setValue(self, value):
        self.slider.setValue(value)

    def setMinimum(self, value):
        self.slider.setMinimum(value)

    def setMaximum(self, value):
        self.slider.setMaximum(value)


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.horizontalSliders = SlidersGroup(QtCore.Qt.Horizontal, "Horizontal")

        self.stackedWidget = QtGui.QStackedWidget()
        self.stackedWidget.addWidget(self.horizontalSliders)

        self.valueLineView = QtGui.QLineEdit('0')
        self.valueLineView.setReadOnly(True)

        self.valueLCDView = QtGui.QLCDNumber(4)
        self.valueLCDView.setNumDigits(20)

        self.createControls("Controls")

        self.horizontalSliders.valueChanged.connect(self.valueSpinBox.setValue)
        self.valueSpinBox.valueChanged.connect(self.horizontalSliders.setValue)
        self.valueSpinBox.valueChanged.connect(self.valueSpinBox.setValue)
        self.valueSpinBox.valueChanged.connect(self.valueLCDView.display)
        self.valueSpinBox.valueChanged.connect(self.valueLineViewPaste)


        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.stackedWidget)
        layout.addWidget(self.controlsGroup)

        self.setLayout(layout)

        self.minimumSpinBox.setValue(0)
        self.maximumSpinBox.setValue(20)
        self.valueSpinBox.setValue(5)

        self.setWindowTitle("Sliders")

    def valueLineViewPaste(self):
        valueSTR = str(self.valueSpinBox.value())
        valueSTR1 = str(self.horizontalSliders.slider.value())
        print("valueSTR = ", valueSTR, valueSTR1)
        self.valueLineView.clear()
        self.valueLineView.insert(valueSTR)

    def createControls(self, title):
        self.controlsGroup = QtGui.QGroupBox(title)

        minimumLabel = QtGui.QLabel("Minimum value:")
        maximumLabel = QtGui.QLabel("Maximum value:")
        valueLabel = QtGui.QLabel("Current value:")

        self.minimumSpinBox = QtGui.QSpinBox()
        self.minimumSpinBox.setRange(-100, 100)
        self.minimumSpinBox.setSingleStep(1)

        self.maximumSpinBox = QtGui.QSpinBox()
        self.maximumSpinBox.setRange(-100, 100)
        self.maximumSpinBox.setSingleStep(1)

        self.valueSpinBox = QtGui.QSpinBox()
        self.valueSpinBox.setRange(-100, 100)
        self.valueSpinBox.setSingleStep(1)

        self.minimumSpinBox.valueChanged.connect(self.horizontalSliders.setMinimum)
        self.maximumSpinBox.valueChanged.connect(self.horizontalSliders.setMaximum)

        controlsLayout = QtGui.QGridLayout()
        controlsLayout.addWidget(valueLabel, 1, 0)
        controlsLayout.addWidget(self.valueSpinBox, 1, 1)
        controlsLayout.addWidget(self.valueLineView, 2, 1)
        controlsLayout.addWidget(self.valueLCDView, 3, 1)

        self.controlsGroup.setLayout(controlsLayout)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
