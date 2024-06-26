# s="/*Jon is @developer & musician!!"

#  ''.join(c for c in s if c.islower())
import string

def replace_special_symbols(s):
    for char in string.punctuation:
        s = s.replace(char, '#')
    return s

input_string = "/*Jon is @developer & musician!!"
output = replace_special_symbols(input_string)

print(output)
