class FenTree:
    """
    Структура данных дерево Фенвика
    """
    def __init__(self):
        """
        Инициализация дерева
        """
        self.BITTree = []
        self.size = 0

    def get_sum(self, i):
        """
        Функция частичной суммы элементов
        :param i: элемент
        :return: s
        """
        s = 0
        i = i + 1

        while i > 0:
            s += self.BITTree[i]
            i -= i & (-i)
        return s

    def update_bit(self, i, v):
        """
        Функция преобразования в биты
        :param i: позиция
        :param v: значение
        :return: None
        """
        i += 1
        n = self.size
        while i <= n:
            self.BITTree[i] += v
            i += i & (-i)

    def construct(self, arr):
        """
        Функция построения битового массива
        :param arr: список элементов
        :return: None
        """
        self.size = len(arr)

        self.BITTree = [0]*(self.size+1)

        for i in range(self.size):
            self.update_bit(i, arr[i])

    def range_sum(self, l, r):
        """
        Функция вычисления суммы
        :param l: первый элемент
        :param r: второй элемент
        :return:
        """
        return self.get_sum(r) - self.get_sum(l - 1)
