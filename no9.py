def create_new_string(s):
    length = len(s)
    if length < 3:
        return "Input string must have at least 3 characters."
    
    if length % 2 == 0:
        middle1 = s[length // 2 - 1]
        middle2 = s[length // 2]
        return f"{s[0]}{middle1}{middle2}{s[-1]}"
    else:
        middle = s[length // 2]
        return f"{s[0]}{middle}{s[-1]}"

