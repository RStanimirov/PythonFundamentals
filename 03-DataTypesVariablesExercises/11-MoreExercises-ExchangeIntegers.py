# int_a = int(input())
# int_b = int(input())
#
# print("Before:")
# print(f"a = {int_a}")
# print(f"b = {int_b}")
# print("After:")
# print(f"a = {int_b}")
# print(f"b = {int_a}")

a = old_a = input()
b = old_b = input()

print(f"Before:")
print(f"a = {a}")
print(f"b = {b}")
a = old_b
b = old_a
print(f"After:")
print(f"a = {a}")
print(f"b = {b}")