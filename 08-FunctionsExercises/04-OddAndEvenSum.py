def odd_even_sum(a):
    even_list = []
    odd_list = []
    for i in a:
        i = int(i)
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}")


input_num_str = str(input())

odd_even_sum(input_num_str)