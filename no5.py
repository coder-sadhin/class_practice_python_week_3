def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        print(f"{char}:{count}")

input_string = input()
count_characters(input_string)
