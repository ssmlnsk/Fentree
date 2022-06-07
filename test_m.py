import unittest

from main import FenTree


class MyTestCase(unittest.TestCase):
    def test_construct(self):
        freq = [1, 2, 3, 4]
        fentree = FenTree()
        fentree.construct(freq)
        self.assertEqual(fentree.BITTree, [0, 1, 3, 3, 10])  # add assertion here

    def test_getsum(self):
        freq = [1, 2, 3, 4]
        fentree = FenTree()
        fentree.construct(freq)
        self.assertEqual((fentree.range_sum(0, 3)), 10)
        self.assertEqual((fentree.range_sum(1, 2)), 5)

    def test_getsum_2(self):
        freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
        fentree = FenTree()
        fentree.construct(freq)
        self.assertEqual((fentree.range_sum(3, 7)), 17)
        self.assertEqual((fentree.range_sum(5, 8)), 18)


if __name__ == '__main__':
    unittest.main()
