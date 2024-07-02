def arrange(s):
    lowercase = ''.join(c for c in s if c.islower())
    uppercase = ''.join(c for c in s if c.isupper())
    return lowercase + uppercase

input_string = input()
result = arrange(input_string)
print(result)
# change