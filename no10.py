def merge_tools(string, k):

    for i in range(0, len(string), k):

        sub_string = string[i:i+k]

        seen = set()
        result = []
        for char in sub_string:
            if char not in seen:
                seen.add(char)
                result.append(char)
       
        print(''.join(result))

string, k = input(), int(input())


merge_tools(string, k)