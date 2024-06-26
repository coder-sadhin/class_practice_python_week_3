def find_last_position(s, substring):
    return s.rfind(substring)

input_string = "Emma is a data scientist who knows Python. Emma works at google."
specified_substring = "Emma"
last_position = find_last_position(input_string, specified_substring)

print(last_position)
