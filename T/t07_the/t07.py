"""T07."""


def organise_by_first_symbol(strings: list) -> dict:
    """Sample text."""
    res_dict = {}
    for i in strings:
        category = i[0]
        if category in res_dict:
            res_dict[category].append(i)
        else:
            res_dict.setdefault(category, []).append(i)

    return res_dict


def count_symbol_appearances(stringy: str) -> dict:
    """Sample text."""
    res_dict = {}
    for i in stringy:
        if i in res_dict:
            res_dict[i] += 1
        else:
            res_dict[i] = 1

    return res_dict


def get_unique_values(dictionary: dict) -> list:
    """Sample text."""
    str_dict = {}
    for key, value in dictionary.items():
        str_dict[key] = value

    result = list(set(str_dict.values()))

    return result


def count_symbol_appearances_2(stringy: str) -> dict:
    """Sample text."""
    res_dict = {}
    res1_dict = {}
    for i in stringy:
        if i in res_dict:
            res_dict[i] += 1
        else:
            res_dict[i] = 1

    for k, v in res_dict.items():
        res1_dict.setdefault(v, []).append(k)

    return res1_dict


def debug_numbers_in_string(stringy: str) -> list:
    """Sample text."""
    numbers_only = []
    for i in stringy:
        if i.isdigit():
            numbers_only.append(int(i))
    return numbers_only
