def romanToIntMySillyWay(s: str) -> int:
    """
    Given a roman numeral, convert it to an integer.

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M

    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, the number four is written as IV.
    Because the one is before the five we subtract it making four.
    The same principle applies to the number nine, which is written as IX.

    Runtime: 63 ms
    """

    inp_str = s

    res = 0

    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}

    sub_cases = {'IV': 4,
                 'IX': 9,
                 'XL': 40,
                 'XC': 90,
                 'CD': 400,
                 'CM': 900}

    if len(s) < 2:
        return roman_dict[s]

    for case in sub_cases.keys():
        if case in s:
            res += sub_cases[case]

            inp_str = inp_str.replace(case, '')

    for char in inp_str:
        res += roman_dict[char]

    return res


def romanToIntSmarterWay(s: str) -> int:
    """
    Given a roman numeral, convert it to an integer.

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M

    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, the number four is written as IV.
    Because the one is before the five we subtract it making four.
    The same principle applies to the number nine, which is written as IX.

    Runtime: 68ms
    """

    inp_str = s

    # Replace all special cases to 'normal' way

    inp_str = inp_str.replace('IV', 'IIII').replace('IX', 'VIIII').replace(
        'XL', 'XXXX').replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')

    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    
    # Use the power of map function
    return sum(map(lambda x: roman_dict[x], inp_str))
