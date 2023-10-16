alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    new_text = ""
    for c in plain_text:
        new_index = alphabet.index(c) + shift_amount
        if new_index > 25:
            new_index -= 26
        new_text += alphabet[new_index]
    print(f"The encoded text is {new_text}.")

def decrypt(plain_text, shift_amount):
    new_text = ""
    for c in plain_text:
        new_index = alphabet.index(c) - shift_amount
        if new_index < 0:
            new_index += 26
        new_text += alphabet[new_index]
    print(f"The decoded text is {new_text}.")

if direction == "encode":    
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)