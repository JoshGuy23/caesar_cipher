import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caesar(input_text, shift_amount, text_direction):
    new_text = ""
    for c in input_text:
        if not c.isalpha():
            new_text += c
            continue

        if text_direction == "encode":
            new_index = alphabet.index(c) + shift_amount
            while new_index > 25:
                new_index -= 26
        elif text_direction == "decode":
            new_index = alphabet.index(c) - shift_amount
            while new_index < 0:
                new_index += 26
        else:
            break
        new_text += alphabet[new_index]
    print(f"The new text is {new_text}.")

response = "yes"
while response == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

print("Goodbye.")