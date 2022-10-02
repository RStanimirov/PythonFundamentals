num = int(input())

ready = ("%" * int(num/10))
remain = ("." * int(10-num/10))
loading_bar = (ready + remain)

if num == 100:
    print(f"100% Complete!")
    print(f"[{loading_bar}]")
else:
    print(f"{num}% [{loading_bar}]")
    print("Still loading...")
