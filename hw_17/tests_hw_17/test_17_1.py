import unittest


from hw_17.read_file import read_from_file, check_file
from hw_17.hw_17_1 import squaring, writing_to_file, rewrite_to_file



class TestFileContent(unittest.TestCase):
    # def test_file_content(self):
    #     self.assertEqual(read_from_file(), "10.3 11.2 25.6 30.5")

    def test_written_content(self):
        content_1 = writing_to_file(squaring())
        self.assertEqual(content_1, " 106.09 125.44 655.36 930.25")

    def test_squaring_result(self):
        self.assertEqual(squaring(), [106.09, 125.44, 655.36, 930.25])

    def test_square_int(self):
        self.assertEqual(squaring(), [106.09, 125.44, 655.36, 930.25])

    def test_not_equal(self):
        self.assertNotEqual(squaring(), [106, 125, 655, 930])

    def test_negative_result(self):
        self.assertNotEqual(squaring(), [-106.09, -125.44, 158.76, 1169.64])

    # @unittest.skip("Fil may be does not exist")
    def test_if_file_exist(self):
        if check_file() is False:
            return False
        self.assertEqual(False, False, "File doesn't exist")

    def test_rewrite_to_file(self):
        content_1 = rewrite_to_file()
        self.assertEqual(content_1, "10.3 11.2 25.6 30.5")

if __name__ == '__main__':
    unittest.main()
