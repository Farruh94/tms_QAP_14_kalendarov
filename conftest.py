import pytest



@pytest.fixture(name="create_and_read_from_file")
def digit_write(tmp_path):
    digit_file = tmp_path / "new_digits.txt"
    with open(digit_file, "w") as file:
        file.writelines("10.3 11.2 25.6 30.5")
    with open(digit_file, "r") as f:
        file_content = map(float, f.readline().split())
    new_list = []
    for i in file_content:
        new_list.append(i)
    return new_list

@pytest.fixture(name="work_on_first_bin")
def bin_file_1(tmp_path):
    first_bin = tmp_path / "first.bin"
    with open(first_bin, "wb") as first:
        first.write("У лукоморья дуб зелёный;\nЗлатая цепь на дубе том:\n"
                    "И днём и ночью кот учёный\nВсё ходит по цепи кругом;")
    with open(first_bin, "rb") as fc:
        first_content = fc.readline()
    return first_content

@pytest.fixture(name="work_on_second_bin")
def bin_file_1(tmp_path):
    second_bin = tmp_path / "second.bin"
    with open(second_bin, "wb") as second:
        second.write("— Скажи-ка, дядя, ведь недаром\nМосква, спаленная пожаром,\n"
                     "Французу отдана?\nВедь были ж схватки боевые,\n"
                     "Да, говорят, еще какие!\nНедаром помнит вся "
                     "Россия\nПро день Бородина!")
    with open(second_bin, "rb") as sc:
        second_content = sc.readline()
    return second_content
