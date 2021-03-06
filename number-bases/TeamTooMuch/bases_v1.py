#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # Wow, so unnecessary. rip
    spot = []
    result = []
    
    for each in str(digits):
        if base == 16 and each in string.hexdigits: 
            if each not in string.digits:
                hex_str = { "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15 }
                each = hex_str[each.upper()]
            spot.insert(0, each)
            continue
        elif base == 2 and each in ("0", "1", " "):
            if each in ("0", "1"):
                spot.insert(0, each)
        elif base == 26:
            base_26 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}            
            each = base_26[each.upper()]
            spot.insert(0, each)
        else:
             # TODO: Replace this temporary code for the other bases.. currently only accepts digits
            if each not in string.digits:
                return f"This is not valid digit in base {base}"
            spot.insert(0, each)

    for index, digit in enumerate(spot):
        converted = int(digit) * (base**(index))

        result.append(converted)

    return sum(result)

    # WAIT. BUT REALLY THO.
    # return int(digits, base)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # Basically '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base_36 = string.digits + string.ascii_uppercase

    converted = []

    # Encode number in binary (base 2)
    if base == 2:
        while number > 0:
            remainder = number % 2
            quotient = number / 2
            split_quotient = str(quotient).split(".")
            number = int(split_quotient[0])
            converted.append(str(remainder))
        return "".join(converted)

    # Encode number in hexadecimal (base 16)
    elif base == 16:
        while number > 0:
            quotient = number / 16
            remainder = number % 16
            split_quotient = str(quotient).split(".")
            number = int(split_quotient[0])
            if 9 < remainder < 16:
                remainder = base_36[remainder]
            converted.insert(0, str(remainder))
            # print(f"{number} r: {remainder}")
        return "".join(converted)

    # Encode number in any base (2 up to 36)
    else:
        while number > 0:
            quotient = number / base
            remainder = number % base
            split_quotient = str(quotient).split(".")
            number = int(split_quotient[0])
            if 9 < remainder < base:
                remainder = base_36[remainder]
            converted.insert(0, str(remainder))
            # print(f"{number} r: {remainder}")
        return "".join(converted)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()

    # print(decode("10110011", 2))
    print(decode("e7a9", 16))
    # print(decode("420224", 12))

    # base_20 = {}

    # for i, char in enumerate("0123456789ABCDEFGHJKLMNOPQRSTUVWXYZ"):
    #     base_20[char] = i
    # print(base_20)