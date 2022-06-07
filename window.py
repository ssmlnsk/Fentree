import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from main import FenTree
from db_sql import Database


class MainWindow(QWidget):
    """
    Класс создания главного окна
    """
    def __init__(self):
        """
        Загрузка основного окна, прикрепление действий к кнопкам
        """
        super().__init__()
        self.setWindowTitle('Fenwick Tree')
        self.ui = uic.loadUi('1.ui', self)
        self.sumbtn.clicked.connect(self.sum_cl)
        self.createbtn.clicked.connect(self.create_tree)
        self.updbtn.clicked.connect(self.upd_tree)
        self.sbtn.clicked.connect(self.save_tree)
        self.lbtn.clicked.connect(self.load_tree)
        self.dbtn.clicked.connect(self.del_tree)
        self.tree = []
        self.treefile = Database()
        self.ftree = FenTree()

    def sum_cl(self):
        """
        Функция суммирования диапазона чисел
        :return: None
        """
        x = self.fval.value()
        y = self.sval.value()
        if self.tree == []:
            self.warning()
        else:
            rs = self.ftree.range_sum(x, y)
            self.label.setText('Результат: ' + str(rs))

    def upd_tree(self):
        """
        Функция обновления числа в выбранной позиции списка
        :return: None
        """
        x = self.fval2.value()
        y = self.sval2.value()
        if self.tree == []:
            self.warning()
        else:
            val = y - self.tree[x]
            self.ftree.update_bit(x, val)
            self.tree[x] = y
            self.label_2.setText(str(self.tree))

    def warning(self):
        """
        Диалоговое окно с ошибкой
        :return: None
        """
        messagebox = QMessageBox(self)
        messagebox.setWindowTitle("Ошибка")
        messagebox.setText("Список пуст!")
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setStandardButtons(QMessageBox.Ok)

        messagebox.show()

    def create_tree(self):
        """
        Функция построения дерева
        :return: None
        """
        a = self.lineEdit.text().split()
        if a == []:
            self.warning_num()
        elif a[0].isnumeric() == False:
            self.warning_num()
        else:
            self.tree = list(map(int, a))
            self.label_2.setText(str(self.tree))
            self.ftree.construct(self.tree)
            self.fval.setMaximum(len(a)-1)
            self.fval2.setMaximum(len(a)-1)
            self.sval.setMaximum(len(a)-1)

    def warning_num(self):
        """
        Диалоговое окно с ошибкой
        :return: None
        """
        messagebox = QMessageBox(self)
        messagebox.setWindowTitle("Ошибка")
        messagebox.setText("Введите числа через пробел!")
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setStandardButtons(QMessageBox.Ok)

        messagebox.show()

    def save_tree(self):
        """
        Функция сохранения данных в базу данных
        :return: None
        """
        mkstr = ' '.join(map(str, self.tree))
        data = [self.fileline.text(), mkstr]

        self.treefile.save_db(data)

    def load_tree(self):
        """
        Функция загрузки данных из базы данных
        :return: None
        """
        s = self.treefile.load_db(self.fileline.text())
        if s:
            self.lineEdit.setText(s[0])
            self.create_tree()
            self.tabWidget.setCurrentIndex(0)

    def del_tree(self):
        """
        Функция удаления сохранения из базы данных
        :return: None
        """
        name = self.fileline.text()
        if self.treefile.load_db(name):
            self.treefile.delete_db(name)
            self.fileline.setText('Удалено')


app = QApplication(sys.argv)
if __name__ == "__main__":
    mwin = MainWindow()
    mwin.show()
    sys.exit(app.exec_())
