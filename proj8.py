alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_change, shift_amnt, chosen_direction):
    if chosen_direction == "encode":
        encrypted_text = ""
        for letter in range(0, len(text_change)):
            if text_change[letter] != " ":
                index_encrypted_letter = alphabet.index(text_change[letter]) + shift_amnt
                if index_encrypted_letter >= len(alphabet):
                    encrypted_text += alphabet[index_encrypted_letter - len(alphabet)]
                else:
                    encrypted_text += alphabet[index_encrypted_letter]
            else:
                encrypted_text += " "
        print(f"The encoded text is {encrypted_text}")
    elif chosen_direction == "decode":
        decoded_text = ""
        for letter in text_change:
            if letter != " ":
                position = alphabet.index(letter)
                new_position = position - shift_amnt
                if new_position >= len(alphabet):
                    decoded_text += alphabet[new_position - len(alphabet)]
                else:
                    decoded_text += alphabet[new_position]
            else:
                decoded_text += " "
        print(f"The decoded text is {decoded_text}")
    else:
        print("You typed an incorrect direction")    
    
caesar(text, shift, direction)