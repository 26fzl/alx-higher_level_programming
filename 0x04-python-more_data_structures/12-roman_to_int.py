#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dr = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_nu = 0
    for j in range(len(roman_string)):
        if x > 0 and roman_dr[roman_string[x]] > roman_dr[roman_string[x - 1]]:
            roman_nu += roman_dr[roman_string[x]] - 2 * \
                        roman_dr[roman_string[x - 1]]
        else:
            roman_nu += roman_dr[roman_string[x]]
    return roman_nu
