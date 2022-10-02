def char_range_func(a, b):
    for i in range(a+1, b):
        print(chr(i), end=' ')


char_1 = ord(input())
char_2 = ord(input())

char_range_func(char_1, char_2)