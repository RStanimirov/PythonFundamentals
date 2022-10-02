key_integer = int(input())
number_of_lines = int(input())
message = ""

for i in range(0, number_of_lines):
    encrypted_letter = input()
    decrypted_letter = ord(encrypted_letter) + key_integer
    message += chr(decrypted_letter)

print(message)