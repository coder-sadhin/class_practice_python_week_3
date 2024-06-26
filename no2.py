def count_chars_digits_symbols(s):
    num_char = 0
    num_digit = 0
    num_symbol = 0
    for char in s:
        if char.isalpha():
            num_char += 1
        elif char.isdigit():
            num_digit += 1
        else:
            num_symbol += 1
    return num_char, num_digit, num_symbol
s=input()
num_char, num_digit, num_symbol=count_chars_digits_symbols(s)

print("Chars={}".format(num_char))
print("Digits={}".format(num_digit))
print("Symbol={}".format(num_symbol))