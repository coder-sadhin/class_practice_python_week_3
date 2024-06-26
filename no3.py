def mixed_string(s1, s2):
    result = ""
    len_s1, len_s2 = len(s1), len(s2)
    max_len = max(len_s1, len_s2)
    for i in range(max_len):
        if i < len_s1:
            result += s1[i]
        if i < len_s2:
            result += s2[-(i + 1)]

    print(result)

s1=input()
s2=input()
mixed_string(s1,s2)