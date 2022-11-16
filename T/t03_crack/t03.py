"""Sample t3xt."""


def is_even(num: int) -> bool:
    """Even."""
    if (num % 2) == 0:
        return True
    return False


def multiply_between(start: int, end: int) -> int:
    """Multiply Between."""
    multiply_result = 1
    numberlist = list(range(start, end + 1))
    for x in numberlist:
        multiply_result = multiply_result * x
    return multiply_result


def sum_numbers(sumlist: list) -> int:
    """Sum Numbers."""
    sum_result = 0
    for sum_input in sumlist:
        if str(sum_input).isdigit() is True:
            sum_result = sum_result + int(sum_input)
    return sum_result


def filter_letters(letterslist: list) -> list:
    """Filter Letters."""
    new_list = []
    for letter in letterslist:
        if str(letter).isalpha() is True:
            new_list.append(letter)
    return new_list


def remove_vowels(inputmessage: str) -> str:
    """Remove Vowels."""
    result = ""
    vowel_list = ["i", "ü", "u", "e", "ö", "õ", "o", "ä", "a"]

    for letter in range(len(inputmessage)):
        charin = inputmessage[letter]
        if charin in vowel_list:
            char = ""
        else:
            char = charin
        result += char
    return result
