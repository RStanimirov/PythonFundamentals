number = int(input())


def solve():
    if number % 2 == 0:
        s = 0
        for i in range(1, number // 2 + 1):
            if number % i == 0:
                s += i
        if s == number:
            print('We have a perfect number!')
        else:
            print("It's not so perfect.")
    else:
        print("It's not so perfect.")


solve()
