# В 1 -> 2 и 2 -> 1
# Если нет 1ого
# Если нет 2ого
# Если нет 1  и 2 ого
# Если файлы текстовые
import unittest

from hw_17.hw_17_2 import first, second, change_content
from hw_17.check_files import first_exist, second_exist, first_changed, second_changed, check_if_first_file_exist, \
    check_if_second_file_exist, incorrect_files, incorrect_format


class TestFiles(unittest.TestCase):

    def test_first_file_content(self):
        content_1 = first()  # read from files
        content_2 = second()

        change_content(content_1, content_2)  # change files content

        changed_content_1 = first_changed()  # read from changed files
        changed_content_2 = second_changed()

        self.assertEqual(content_1, changed_content_2)
        self.assertEqual(content_2, changed_content_1)

    def test_second_file_content(self):
        file_1 = first()
        file_2 = second()

        change_content(file_1, file_2)
        new_content_1 = first_changed()
        new_content_2 = second_changed()

        self.assertEqual(file_2, new_content_1)
        self.assertEqual(file_1, new_content_2)

    def test_first_file_not_exist(self):

        if check_if_first_file_exist() is False:
            return False
        self.assertEqual(False, False, "First file does not exist")

    def test_second_file_not_exist(self):

        if check_if_second_file_exist() is False:
            return False
        self.assertEqual(False, False, "Second file does not exist")

    def test_if_both_not_file_exist(self):

        if check_if_first_file_exist() and check_if_second_file_exist() is False:
            return False
        self.assertEqual(False, False, "The both files does not exist")

    def test_files_format(self):
        if incorrect_files(incorrect_format()) is False:
            return False
        self.assertEqual(False, False, "Files format are not .bin")


if __name__ == '__main__':
    unittest.main()
