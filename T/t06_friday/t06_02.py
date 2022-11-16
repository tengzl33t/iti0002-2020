"""T06_02."""

from math import sqrt


def capitalise_name(name: str) -> str:
    """Anime kruto."""
    result = name.upper()

    return result


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Anime kruto."""
    desc = (b ** 2) - (4 * a * c)

    return desc


def quadratic_formula(a: int, b: int, c: int):
    """Anime kruto."""
    desc = calculate_discriminant(a, b, c)
    if desc > 0:
        x1 = round(((-b + sqrt(desc)) / (2 * a)), 2)
        x2 = round(((-b - sqrt(desc)) / (2 * a)), 2)
        result = (x1, x2)
    elif desc == 0:
        x = (-b) / (2 * a)
        result = float(x)
    elif desc < 0:
        result = "Solution has complex roots!"

    return result


def string_every_other(sentence: str) -> str:
    """Anime kruto."""
    result = sentence[::2]

    return result


def string_reverse(sentence: str) -> str:
    """Anime kruto."""
    result = sentence[::-1]

    return result


def string_concat(string_one: str, string_two: str) -> str:
    """Anime kruto."""
    result = string_one + string_two

    return result


def string_multiply(word: str, key: int) -> str:
    """Anime kruto."""
    result = word * key

    return result


def string_one_in_another(string_one: str, string_two: str) -> bool:
    """Anime kruto."""
    if string_one in string_two:
        return True
    else:
        return False


def list_string_to_list(string: str) -> list:
    """Anime kruto."""
    str_list = []
    for i in string:
        str_list.append(i)

    return str_list


def list_no_start_and_end(list_of_things: list) -> list:
    """Anime kruto."""
    new_list = list_of_things[1:-1]

    return new_list


def list_reverse(list_of_things: list) -> list:
    """Anime kruto."""
    rev_list = list_of_things[::-1]

    return rev_list


def list_remove(list_of_things: list) -> list:
    """Anime kruto."""
    res_list = list_of_things[:1] + list_of_things[2:]
    res_list = res_list[::-1]

    return res_list


def number_is_smaller(number: int, control_number: int) -> bool:
    """Anime kruto."""
    if number >= control_number:
        return False
    else:
        return True


def equal_strings(string_one: str, string_two: str) -> bool:
    """Anime kruto."""
    if string_one is string_two:
        return True
    else:
        return False


def string_in_list(searchable: str, search_list: list) -> bool:
    """Anime kruto."""
    if searchable in search_list:
        return True
    else:
        return False


def filter_numbers(numbers: list) -> int:
    """Anime kruto."""
    result = 0
    for i in numbers:
        if not (i % 2) == 0:
            result += i

    return result


def filter_more_numbers(numbers: list) -> int:
    """Anime kruto."""
    reslist = []
    for i in numbers:
        if not (((i % 2) != 0) and ((i <= 10) or (i > 20))):
            reslist.append(i)

    result = sum(reslist)

    return result


def fixed_loop() -> list:
    """Anime kruto."""
    res_list = []
    for i in range(0, 10):
        res_list.append(i)

    return res_list


def fixed_step_loop() -> list:
    """Anime kruto."""
    res_list = []
    for i in range(0, 10):
        res_list.append(i)
    res_list = res_list[0::3]

    return res_list


def unknown_loop(min_num: int, max_num: int) -> list:
    """Anime kruto."""
    res_list = []
    for i in range(min_num, max_num + 1):
        res_list.append(i)

    return res_list


def unknown_loop_fixed_filter(min_num: int, max_num: int) -> list:
    """Anime kruto."""
    res_list = []
    for i in range(min_num, max_num + 1):
        if i % 3 == 0:
            res_list.append(i)

    return res_list


def unknown_loop_unknown_filter(min_num: int, max_num: int, divisible_by: int) -> list:
    """Anime kruto."""
    res_list = []
    if divisible_by != 0:
        for i in range(min_num, max_num + 1):
            if i % divisible_by == 0:
                res_list.append(i)

    return res_list


def add_to_dict(elements_to_dict: list) -> dict:
    """Anime kruto."""
    res_dict = {}
    for i in elements_to_dict:
        res_dict[i] = len(i)

    return res_dict


def remove_keys(keys_to_remove: list, dictionary: dict) -> dict:
    """Anime kruto."""
    for i in keys_to_remove:
        if i in dictionary:
            dictionary.pop(i)

    return dictionary


def remove_from_values(values_to_remove: list, dictionary: dict) -> dict:
    """Anime kruto."""
    locdict = {}
    for k, v in dictionary.items():
        if v not in values_to_remove:
            locdict[k] = v

    return locdict


def sort_keys_by_alphabet(dictionary: dict) -> list:
    """Anime kruto."""
    res_list = []
    for i in dictionary.keys():
        res_list.append(i)

    result = sorted(res_list, reverse=True)

    return result


def debugging_simple(elements: list, max_size: int) -> list:
    """Anime kruto."""
    res_list = []

    for element in elements:
        print(element)
        if len(element) <= max_size:
            res_list.append(element)
    return res_list
