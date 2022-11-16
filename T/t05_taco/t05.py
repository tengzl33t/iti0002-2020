"""T05."""


def can_make_tacos(ingredients: list) -> bool:
    """I do not need this text. It's for automaattester))."""
    shell = ingredients.count("taco_shell")

    meat = ingredients.count("meat")

    guacamole = ingredients.count("guacamole")
    tomato_sauce = ingredients.count("tomato_sauce")
    sour_cream = ingredients.count("sour_cream")

    cheese = ingredients.count("cheese")

    onion = ingredients.count("onion")
    tomatoes = ingredients.count("tomatoes")
    paprika = ingredients.count("paprika")
    lettuce = ingredients.count("lettuce")

    if (
        shell >= 1
        and meat >= 1
        and cheese >= 1
        and (guacamole >= 1 or tomato_sauce >= 1 or sour_cream >= 1)
        and (onion >= 1 or tomatoes >= 1 or paprika >= 1 or lettuce >= 1)
    ):
        return True
    else:
        return False


def make_tacos(ingredients: list) -> int:
    """I do not need this text. It's for automaattester))."""
    if can_make_tacos(ingredients) is True:
        result = ingredients.count("taco_shell")
    else:
        result = 0
    return result


def has_correct_format(str_given: str) -> bool:
    """I do not need this text. It's for automaattester))."""
    str_split = str_given.split()
    check_dot = str_given[-1] == "."
    if str_split[0].istitle() and (check_dot is True):
        return True
    else:
        return False


def has_searchable(random_letters: str, searchable: str) -> bool:
    """I do not need this text. It's for automaattester))."""
    rletters = []
    sletters = []
    for i in random_letters:
        rletters.append(i)
    for i in searchable:
        sletters.append(i)

    print(sletters)
    print(rletters)
    counter = len(searchable)

    if len(random_letters) >= len(searchable):
        print("lentest")
        for s in sletters:
            if s in rletters:
                rletters.remove(s)
                counter -= 1
            else:
                return False
            if counter < 1:
                return True
    else:
        return False


def upper_lower_continuity(continuity: str) -> bool:
    """I do not need this text. It's for automaattester))."""
    if continuity:
        check1 = continuity[::2].isupper()
        check2 = continuity[1::2].islower()

        if (check1 and check2) is True:
            return True
        else:
            return False
    else:
        return True


def equilibrium_of_letters(letters: str) -> bool:
    """I do not need this text. It's for automaattester))."""
    vowels = {"a", "e", "i", "o", "u"}
    consonants = {
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "x",
        "z",
        "w",
        "y",
    }

    vow_count = 0
    con_count = 0
    lc_input = letters.lower()

    for vowel in lc_input:
        if vowel in vowels:
            vow_count = vow_count + 1

    for consonant in lc_input:
        if consonant in consonants:
            con_count = con_count + 1

    if con_count == vow_count:
        return True
    else:
        return False
