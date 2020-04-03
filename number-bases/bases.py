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

    # reverse by slicing to use index as power
    digits = digits[::-1]
    result = 0

    # Basically '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base_36 = string.digits + string.ascii_uppercase

    for index, digit in enumerate(digits):
        if digit in string.ascii_letters:
            digit = base_36.index(digit.upper())

        # Python uses ** for exponents
        converted = int(digit) * (base**(index))
        result += converted

    return result

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

    # Encode number in any base (2 up to 36)
    while number > 0:
        quotient = number / base
        remainder = number % base

        # Convert to str to grab just the integer, and then back to int
        split_quotient = str(quotient).split(".")
        number = int(split_quotient[0])

        # Convert to alphanumeric value
        if 9 < remainder < base:
            remainder = base_36[remainder].lower()

        # Add to front
        converted.insert(0, str(remainder))

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
    # Convert digits from any base to any base (2 up to 36)
    decoded = decode(digits, base1)
    return encode(decoded, base2)


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
    main()

    # print(decode("10110011", 2))
    # print(decode("e7a9", 16))
    # print(decode("420224", 12))

    # print(encode(21, 2))
    # print(encode(59305, 16))
    # print(encode(1037116, 12))
    # print(encode(23467, 12))