import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

diag_1 = math.sqrt(x1**2 + y1**2)
diag_2 = math.sqrt(x2**2 + y2**2)

if diag_1 <= diag_2:
    print(f"({math.floor(x1)}, {math.floor(y1)})")
else:
    print(f"({math.floor(x2)}, {math.floor(y2)})")