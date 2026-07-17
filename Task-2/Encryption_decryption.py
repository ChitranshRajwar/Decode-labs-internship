print("===== Caesar Cipher =====")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Encrypt or Decrypt? (e/d): ")

if choice == "d":
    shift = shift * -1

result = ""

for letter in message:
    if letter.isalpha():
        if letter.isupper():
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"

        position = alphabet.index(letter)
        new_position = (position + shift) % 26
        result = result + alphabet[new_position]
    else:
        result = result + letter

print("Result:", result)
