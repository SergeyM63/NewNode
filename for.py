for i in range (10):
    print (i)

    var = str(i)
    print ("""self.label_"""+var+""" = QtGui.QLabel("Current value_"""+var+""":")
    self.spinBox_"""+var+""" = QtGui.QSpinBox()
    self.spinBox_"""+var+""" = QtGui.QSpinBox()
    self.spinBox_"""+var+""".setRange(-1000, 1000)
    self.spinBox_"""+var+""".setSingleStep(1)
    self.spinBox_"""+var+""".setValue(23)
    self.a = str(self.spinBox_"""+var+""".value())
    self.LineView_"""+var+""" = QtGui.QLineEdit(self.a)
    self.LineView_"""+var+""".setReadOnly(True)""")

    print ("""   def LineViewPaste_"""+var+"""(self):
        print("valueSTR = ", str(self.spinBox_"""+var+""".value()))
        self.LineView_"""+var+""".clear()
        self.LineView_"""+var+""".insert(str(self.spinBox_"""+var+""".value()))
        """)
    print ("""
    self.spinBox_"""+var+""".valueChanged.connect(self.spinBox_"""+var+""".setValue)
    self.spinBox_"""+var+""".valueChanged.connect(self.LineViewPaste_"""+var+""")
""")