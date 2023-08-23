import unittest


def summ(a_1, b_2):
    nat = 0
    for i in range(a_1, b_2 + 1):
        nat += i

    return nat


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(summ(2, 5), 14)

    def test_2(self):
        self.assertEqual(summ(3, 5),  12)

    def test_3(self):
        self.assertEqual(summ(3, -5),  10)

    def test_4(self):
        self.assertEqual(summ(0, 0), 0)

    def test_5(self):
        self.assertGreater(5, 1, "Error!!@")

    def test_6(self):
        self.assertIsNot(5, 5, '*')


if __name__ == '__main__':
    unittest.main()