# В 1 -> 2 и 2 -> 1
# Если нет 1ого
# Если нет 2ого
# Если нет 1  и 2 ого
# Если файлы текстовые
import pytest

from hw_18.check_files_1 import first_changed, second_changed, check_if_first_file_exist, \
    check_if_second_file_exist, incorrect_files, incorrect_format
from hw_18.hw_18_2 import first_file, second_file, change_content

fb = "У лукоморья дуб зелёный;\nЗлатая цепь на дубе том:\nИ днём и ночью кот учёный\nВсё ходит по цепи кругом;"
sb = ("— Скажи-ка, дядя, ведь недаром\nМосква, спаленная пожаром,\nФранцузу отдана?\nВедь были ж схватки боевые,\nДа,"
      "\nговорят, еще какие!\nНедаром помнит вся Россия\nПро день Бородина!")


class TestFiles():

    def test_first_file_content(self):
        content_1 = first_file()  # read from files
        content_2 = second_file()

        change_content(content_1, content_2)  # change files content

        changed_content_1 = first_changed()  # read from changed files
        changed_content_2 = second_changed()

        assert content_1 == changed_content_2
        assert content_2 == changed_content_1

    def test_second_file_content(self):
        file_1 = first_file()
        file_2 = second_file()

        change_content(file_1, file_2)
        new_content_1 = first_changed()
        new_content_2 = second_changed()

        assert file_2 == new_content_1
        assert file_1 == new_content_2

    @pytest.fixture
    def test_fix(self, work_on_second_bin, work_on_first_bin):
        first_con = work_on_first_bin
        second_con = work_on_second_bin

        assert first_con == fb
        assert second_con == sb

    def test_first_file_not_exist(self):

        if check_if_first_file_exist() is False:
            return False
        assert False is False, "First file does not exist"

    def test_second_file_not_exist(self):

        if check_if_second_file_exist() is False:
            return False
        assert False is False, "Second file does not exist"

    def test_if_both_not_file_exist(self):

        if check_if_first_file_exist() and check_if_second_file_exist() is False:
            return False
        assert False is False, "The both files does not exist"

    def test_files_format(self):
        if incorrect_files(incorrect_format()) is False:
            return False
        assert False is False, "Files format are not .bin"
