from modules import encrypt, decrypt

should_continue = True

while should_continue:
    direction = input("Type 'encode' for encrypt, Type 'decode' for decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encoded_text = encrypt(text, shift)
        print(f"Encoded message: {encoded_text}")

    if direction == 'decode':
        decoded_text = decrypt(text, shift)
        print(f"Decoded message: {decoded_text}")

    ans = input("Type 'yes' if you want to go again. Otherwise type 'no': \n" ).lower()
    if ans == 'no':
        should_continue = False