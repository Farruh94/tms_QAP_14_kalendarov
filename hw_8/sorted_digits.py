"""
На вход подаётся некоторое количество (не больше сотни)
разделённых пробелом целых чисел (каждое не меньше 0 и не
больше 19). Выведите их через пробел в порядке
лексикографического возрастания названий этих чисел в
английском языке.Т.е., скажем числа 1, 2, 3 должны быть
выведены в порядке 1, 3, 2, поскольку слово two в словаре
встречается позже слова three, а слово three -- позже слова one
(иначе говоря, поскольку выражение 'one' < 'three' < 'two'
является истинным)

"""

number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
                13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                18: 'eighteen', 19: 'nineteen'}

# sorted_tuples = sorted(number_names.items(), key=lambda item: item[1])
# sorted_dict = {k: v for k, v in sorted_tuples}
def sort_numbers_by_name(numbers):
    """
    :param numbers str divided by whitespase:
    :return: Sorted params by name
    """
    # numbers = "12 18 8 1 0 19 11 15"
    user_list = list(map(int, numbers.split()))
    number_by_name = []
    keys = number_names.keys()
    for i in user_list:
        if i in keys:
            number_by_name.append(number_names.get(i))
            sorted_number = sorted(number_by_name)
    return sorted_number

print(sort_numbers_by_name("12 18 8 1 0 19 11 15"))
