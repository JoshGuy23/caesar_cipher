import art
# Display the ASCII logo
print(art.logo)

# This stores a list of every lowercase character in the alphabet.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
# This function performs a caesar shift of text.
# input_text - the text that will be transformed by the cipher
# shift_amount - the amount that the text will be shifted by
# text_direction - determines whether the input_text is being encoded or decoded
def caesar(input_text, shift_amount, text_direction):
    new_text = ""
    for c in input_text:
        if not c.isalpha():                                 # Any non-alphabetic characters are ignored and put into the output text.
            new_text += c
            continue

        if text_direction == "encode":
            new_index = alphabet.index(c) + shift_amount    # Shifts the input_text forwards
            while new_index > 25:                           # Accounts for unusually large shift_amounts
                new_index -= 26
        elif text_direction == "decode":
            new_index = alphabet.index(c) - shift_amount    # Shifts the input_text backwards
            while new_index < 0:                            # Accounts for unusually large shift_amounts
                new_index += 26
        else:
            break                                           # Accounts for erroneous inputs that are not "encode" or "decode"
        new_text += alphabet[new_index]                     # Add the shifted characters to a new string.
    print(f"The new text is {new_text}.")                   # Display the shifted string

response = "yes"
while response == "yes":                                    # Ensures the program can repeat if the user desires.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

print("Goodbye.")