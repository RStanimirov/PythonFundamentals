input_string_repeating_chars = input()

repeating_char = ''
non_repeating_char = ''
string_no_repeating_chars = []

for i in range(0, len(input_string_repeating_chars)-1):

    if input_string_repeating_chars[i] == input_string_repeating_chars[i+1]:
        repeating_char = input_string_repeating_chars[i]

    else:
        non_repeating_char = input_string_repeating_chars[i]
        string_no_repeating_chars.append(input_string_repeating_chars[i])


string_no_repeating_chars.append(input_string_repeating_chars[-1])
print(''.join(string_no_repeating_chars))

