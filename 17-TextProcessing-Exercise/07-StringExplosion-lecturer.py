# Lecturer's initial entangled and unoptimised solution:
text = input()

result_text = ''
i = 0
bomb_power = 0

while i < len(text):

    if text[i] != '>' and bomb_power == 0:
        result_text += text[i]

    elif text[i] == '>':
        result_text += '>'
        bomb_power += int(text[i + 1])

        while bomb_power > 0:
            i += 1

            if i >= len(text):
                break

            if text[i] == '>':
                result_text += '>'
                bomb_power += int(text[i + 1])
            else:
                bomb_power -= 1

    i += 1

print(result_text)

# Easy way solution
# text = input()
#
# result_text = ''
#
# i = 0
# explosion_power = 0
# while i < len(text):
#     curr_ch = text[i]
#
#     if curr_ch == '>':
#         result_text += '>'
#         explosion_power += int(text[i + 1])
#     else:
#         if explosion_power > 0:
#             explosion_power -= 1
#         else:
#             result_text += curr_ch
#
#     i += 1
#
# print(result_text)
