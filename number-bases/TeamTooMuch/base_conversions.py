def get_hex_value(num):
    hex_values = { 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }
    return hex_values[num]

def dec_to_hex(num):
    hex_code = []
    quotient = num

    while quotient != 0:
        quotient = num / 16
        split_quotient = str(quotient).split(".")
        int_quotient = int(split_quotient[0])
        remainder = int_quotient % 16
        if remainder < 16:
            hex_code.append(get_hex_value(int_quotient))
        num = remainder
    print(hex_code)

dec_to_hex(145)

def add_index():
    hex_values = {}
    derp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

    for index, each in enumerate(derp):
        hex_values[index] = each

    return hex_values

# print(add_index())
