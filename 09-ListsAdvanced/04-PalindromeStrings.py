input_list = input().split()
palindrome = input()

palindromes_list = [x for x in input_list if x == x[::-1]]

print(palindromes_list)

if palindrome in palindromes_list:
    n_occurrence = palindromes_list.count(palindrome)
    print(f"Found palindrome {n_occurrence} times")
else:
    print("Found palindrome 0 times")

