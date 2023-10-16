alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_text = ""
    for c in text:
        new_index = alphabet.index(c) + shift
        if new_index > 25:
            new_index -= 26
        new_text += alphabet[new_index]
    print(new_text)

if direction == "encode":    
    encrypt(text, shift)