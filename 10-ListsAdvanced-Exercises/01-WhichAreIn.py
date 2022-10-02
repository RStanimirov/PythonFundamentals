first_input_list = input().split(', ')
second_input_text = input()

output_list = [x for x in first_input_list if x in second_input_text]

print(output_list)
