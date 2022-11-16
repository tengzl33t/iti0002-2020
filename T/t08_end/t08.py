"""T08."""


def alarm_clock(day: int, vacation: bool) -> str:
    """Sample text."""
    if vacation is False:
        if day < 5:
            alarm = "08:00"
        else:
            alarm = "10:00"
    else:
        if day < 5:
            alarm = "10:00"
        else:
            alarm = "off"

    return alarm


def keep_if_first_two_symbols_same(stringys: list) -> list:
    """Sample text."""
    res_list = []
    for i in stringys:
        if len(i) > 1 and (i[0] == i[1]):
            res_list.append(i)

    return res_list


def middle_chars(s: str) -> str:
    """Sample text."""
    leng = len(s)
    if (leng % 2) == 0 and leng > 0:
        index = leng // 2
        return s[index - 1] + s[index]
    else:
        return ""


def remove_nth_symbol(s, n) -> str:
    """Sample text."""
    index = n - 1
    if n <= len(s) and n >= 1:
        result = s[:index] + s[index + 1:]
    else:
        result = s
    return result


def in1to10(n: int, outside_mode: bool) -> bool:
    """Sample text."""
    if outside_mode is True:
        if n <= 1 or n >= 10:
            return True
        else:
            return False
    else:
        if n in range(1, 10 + 1):
            return True
        else:
            return False


def addition_and_subtraction(stringy: str) -> int:
    """Sample text."""
    try:
        return eval(stringy)
    except SyntaxError:
        return 0


def love6(a, b) -> bool:
    """Sample text."""
    if (isinstance(a, int) or isinstance(a, float)) is True and (
            isinstance(b, int) or isinstance(b, float)
    ) is True:
        if (
                (a == 6 or b == 6)
                or ((a + b) == 6)
                or ((a - b) == 6)
                or ((b - a) == 6)
        ):
            return True
        else:
            return False
    else:
        return False


def equalizer(unequal: list) -> list:
    """Sample text."""
    last_ind = len(unequal) - 1
    result = []
    for i, v in enumerate(unequal):
        if i > 0 and i < last_ind:
            if result[i - 1] < v and unequal[i + 1] < v:
                result.append(v - 1)
            elif result[i - 1] > v and unequal[i + 1] > v:
                result.append(v + 1)
            else:
                result.append(v)
        else:
            result.append(v)
    return result
