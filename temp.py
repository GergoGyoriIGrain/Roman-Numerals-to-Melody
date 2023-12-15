
def int_to_roman(num):
    """
    Converts an integer to a roman numeral
    :param num: positive integer to convert
    """
    if not isinstance(num, int) or num <= 0:
        raise ValueError('num must be a positive integer')
    roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''
    for value, symbol in sorted(roman_map.items(), reverse=True):
        while num >= value:
            result += symbol
            num -= value
    return result


def roman_to_melody(roman_numeral):
    """
    Converts a roman numeral to a melody
    :param roman_numeral: roman numeral to convert
    """
    notes = {'I': 261.63, 'V': 293.66, 'X': 329.63, 'L': 349.23, 'C': 392.00, 'D': 440.00, 'M': 493.88}
    melody = []
    for symbol in roman_numeral:
        if symbol not in notes:
            raise ValueError(f"Invalid roman numeral symbol: {symbol}")
        melody.append(notes[symbol])
    return melody



roman_numeral = int_to_roman(23.41)
print(roman_numeral)
melody = roman_to_melody(roman_numeral)
print(melody)
