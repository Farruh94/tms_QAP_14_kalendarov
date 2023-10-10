import pytest

from hw_18.read_file_1 import read_from_file, check_file
from hw_18.hw_18_1 import squaring, writing_to_file, rewrite_to_file

const_content = " 106.09 125.44 655.36 930.25"


class TestContent:
    @pytest.mark.parametrize("content_1, result", [(read_from_file(), "10.3 11.2 25.6 30.5"),
                                                   (writing_to_file(squaring()), " 106.09 125.44 655.36 930.25")])
    def test_written_content(self, content_1, result):
        assert result == content_1, f"Result 2 should be {content_1},  but you got {result}"

    @pytest.mark.is_exist
    def test_file_is_exist(self):
        assert check_file() is True

    @pytest.fixture_create_and_read_from_file
    def test_new_file_pow(self, create_and_read_from_file):
        assert create_and_read_from_file == [10.3, 11.2, 25.6, 30.5]


#     # def test_squaring_result(self):
#     #     self.assertEqual(squaring(), [106.09, 125.44, 655.36, 930.25])
#     #
#     # def test_square_int(self):
#     #     self.assertEqual(squaring(), [106.09, 125.44, 655.36, 930.25])
#     #
#     # def test_not_equal(self):
#     #     self.assertNotEqual(squaring(), [106, 125, 655, 930])
#     #
#     # def test_negative_result(self):
#     #     self.assertNotEqual(squaring(), [-106.09, -125.44, 158.76, 1169.64])
#     #
#     # # @unittest.skip("Fil may be does not exist")
#     # def test_if_file_exist(self):
#     #     if check_file() is False:
#     #         return False
#     #     self.assertEqual(False, False, "File doesn't exist")
import pytest

# from main_func import sum_func
#
#
# class Test1():
#     @pytest.mark.parametrize("current_result,result",
#                              [(sum_func([1, 2, 3, 4, 5, 6, 78]), 99),
#                               (sum_func((6, 34)), 40)])
#     @pytest.mark.tag_1
#     def test_1(self, current_result, result):
#         print("Tests")
#         assert result == result, f"Result should be {result}, but has {current_result}"
#
#     @pytest.mark.tag_2
#     def test_2(self):
#         assert True
