def is_palindrome_func(a):
    is_palindrome = False

    for each_str in a:
        if len(each_str) == 1:
            is_palindrome = True
        for i in range(0, int(len(each_str) / 2)):
            if each_str[i] == each_str[len(each_str) - i - 1]:
                is_palindrome = True
            else:
                is_palindrome = False

        print(is_palindrome)


input_list = input().split(', ')

is_palindrome_func(input_list)