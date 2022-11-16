"""Sample text."""


def make_hola_string(number: int) -> str:
    """Sample text."""
    string = ""
    while number != 0:
        string = string + "hola"
        number -= 1
    return string


def alphabet_index(input, n: str) -> int:
    """Sample text."""
    if n in input:
        element_index = input.index(n)
    else:
        return "Letter not found."
    return element_index


def multiply_letter(letter: str, times: int) -> str:
    """Sample text."""
    result = letter * times

    return result


def decrypt_cipher(string: str, key: int) -> str:
    """Sample text."""
    output = ""
    while range(len(string)):
        output = string[::key]
        return output


def find_mode(input: str) -> str:  # ==== WIP ===
    """Sample text."""
    input_to_list = list(input)

    if input:
        result = max(input_to_list, key=lambda x: (input_to_list.count(x)))
    else:
        result = ""

    return result
