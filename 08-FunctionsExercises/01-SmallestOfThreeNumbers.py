def smallest_func(a, b, c):
    smallest_num = 0
    if a < b and a < c:
        smallest_num = a
    elif b < a and b < c:
        smallest_num = b
    elif c < a and c < b:
        smallest_num = c
    return smallest_num


int_a = int(input())
int_b = int(input())
int_c = int(input())

print(smallest_func(int_a, int_b, int_c))
