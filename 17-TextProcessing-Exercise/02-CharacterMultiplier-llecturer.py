input_string = input().split()
word_1 = input_string[0]
word_2 = input_string[1]

total_sum = 0
shorter_word_length = min(len(word_1), len(word_2))
longer_word_length = max(len(word_1), len(word_2))

# We process the shorter string first:
for i in range(shorter_word_length):
    total_sum += ord(word_1[i]) * ord(word_2[i])

# If the strings have different lengths we have to process characters of the longer string
for i in range(shorter_word_length, longer_word_length):
    if len(word_1) > len(word_2):
        curr_word_ch = word_1[i]
    else:
        curr_word_ch = word_2[i]

    total_sum += ord(curr_word_ch)

print(total_sum)