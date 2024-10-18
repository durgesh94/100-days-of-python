alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(cipher_text, shift_value):
    decoded_text = ""
    for letter in cipher_text:
        idx = alphabet.index(letter)
        position = idx - shift_value
        if position < 0:
            position += 26
        decoded_text += alphabet[position]
    return decoded_text

def encrypt(original_text, shift_value):
    encoded_text = ""
    for letter in original_text:
        idx = alphabet.index(letter)
        position = idx + shift_value
        if position > 25:
            position -= 26
        encoded_text += alphabet[position]
    return encoded_text