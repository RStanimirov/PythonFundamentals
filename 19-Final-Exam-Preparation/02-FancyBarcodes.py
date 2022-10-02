import re

n = int(input())
pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"

for i in range(n):
    barcode = input()
    if re.match(pattern, barcode):
        digits = re.findall(r"\d", barcode)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
