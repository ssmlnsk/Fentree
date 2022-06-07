import unittest

from PyQt5 import Qt, QtCore
from PyQt5.QtTest import QTest

from window import MainWindow


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mwin = MainWindow()
        self.mwin.show()

    def test_construct(self):
        self.mwin.lineEdit.setText('5 3 6 7 4 2')
        QTest.mouseClick(self.mwin.createbtn, QtCore.Qt.LeftButton)
        self.assertEqual(self.mwin.label_2.text(), "[5, 3, 6, 7, 4, 2]")

    def test_sum(self):
        self.mwin.lineEdit.setText('5 3 6 7 4 2')
        QTest.mouseClick(self.mwin.createbtn, QtCore.Qt.LeftButton)
        self.mwin.fval.setValue(1)
        self.mwin.sval.setValue(4)
        QTest.mouseClick(self.mwin.sumbtn, QtCore.Qt.LeftButton)
        self.assertEqual(self.mwin.label.text(), "Результат: 20")

    def test_upd(self):
        self.mwin.lineEdit.setText('5 3 6 7 4 2')
        QTest.mouseClick(self.mwin.createbtn, QtCore.Qt.LeftButton)
        self.mwin.fval2.setValue(3)
        self.mwin.sval2.setValue(1)
        QTest.mouseClick(self.mwin.updbtn, QtCore.Qt.LeftButton)
        self.assertEqual(self.mwin.label_2.text(), "[5, 3, 6, 1, 4, 2]")

    def test_db(self):
        self.mwin.lineEdit.setText('5 3 6 7 4 2')
        QTest.mouseClick(self.mwin.createbtn, QtCore.Qt.LeftButton)
        self.mwin.fileline.setText('sometest')
        QTest.mouseClick(self.mwin.sbtn, QtCore.Qt.LeftButton)
        self.mwin.lineEdit.setText('0')
        QTest.mouseClick(self.mwin.createbtn, QtCore.Qt.LeftButton)
        QTest.mouseClick(self.mwin.lbtn, QtCore.Qt.LeftButton)
        QTest.mouseClick(self.mwin.dbtn, QtCore.Qt.LeftButton)
        self.assertEqual(self.mwin.label_2.text(), "[5, 3, 6, 7, 4, 2]")

if __name__ == '__main__':
    unittest.main()