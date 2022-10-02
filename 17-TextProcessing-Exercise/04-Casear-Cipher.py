sentence = input()

reassigned_ch = ''
rearranged_sentence = ''

for x in sentence:
    reassigned_ch = ord(x) + 3
    rearranged_sentence += chr(reassigned_ch)

print(rearranged_sentence)