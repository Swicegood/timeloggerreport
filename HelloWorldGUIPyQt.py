import PyQt5.QtGui
app = PyQt5.QtGui.QApplication([])
pb = PyQt5.QtGui.QPushButton('Hello World')
pb.connect(pb,PyQt5.QtCore.SIGNAL("clicked()"),pb.close)
pb.show()
exit(app.exec_())