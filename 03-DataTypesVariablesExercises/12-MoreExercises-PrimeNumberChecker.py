num = int(input())
prime = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break
# if is_not_prime:
#     print("False")
# else:
#     print("True")
print(prime)