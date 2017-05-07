for i in range (10):
    var = str(i)
    print ("""    self.label_"""+var+""" = QtGui.QLabel("Current value_"""+var+""":")
    self.spinBox_"""+var+""" = QtGui.QSpinBox()
    self.spinBox_"""+var+""" = QtGui.QSpinBox()
    self.spinBox_"""+var+""".setRange(-1000, 1000)
    self.spinBox_"""+var+""".setSingleStep(1)
    self.spinBox_"""+var+""".setValue(23)
    self.a = str(self.spinBox_"""+var+""".value())
    self.LineView_"""+var+""" = QtGui.QLineEdit(self.a)
    self.LineView_"""+var+""".setReadOnly(True)
    """)

    print ("""
    self.spinBox_"""+var+""".valueChanged.connect(self.spinBox_"""+var+""".setValue)
    self.spinBox_"""+var+""".valueChanged.connect(self.LineViewPaste_"""+var+""")
""")





for i in range(10):
    var = str(i)
    print("""    def LineViewPaste_""" + var + """(self):
            print("valueSTR = ", str(self.spinBox_""" + var + """.value()))
            self.LineView_""" + var + """.clear()
            self.LineView_""" + var + """.insert(str(self.spinBox_""" + var + """.value()))
            """)

for i in range(10):
    var = str(i)
    print("""    gridLayout.addWidget(self.label_""" + var + """, """ + var + """, 0)
        gridLayout.addWidget(self.spinBox_""" + var + """, """ + var + """, 1)
        gridLayout.addWidget(self.LineView_""" + var + """, """ + var + """, 2)
        """)
