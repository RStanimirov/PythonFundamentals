input_type = input()
input_data = input()
result_int = 0
result_real = 0
result_str = ''

if input_type == 'int':
    input_data = int(input_data)
    result_int = input_data * 2
    print(result_int)
elif input_type == 'real':
    input_data = float(input_data)
    result_real = input_data * 1.5
    print(f"{result_real:.2f}")
elif input_type == 'string':
    input_data = str(input_data)
    result_str = '$' + input_data + '$'
    print(result_str)