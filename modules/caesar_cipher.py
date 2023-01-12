from modules.corpus import reference_list

def encrypt(phrase, shift):
    encrypted_phrase = ""
    for char in phrase:
        if char.isalpha():
            shift %= 26
            char_code = ord(char)
            char_code += shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            encrypted_phrase += chr(char_code)
        else:
            encrypted_phrase += char
    return encrypted_phrase

def decrypt(encrypted_phrase, shift):
    return encrypt(encrypted_phrase, -shift)

def crack(encrypted_phrase):

    for shift in range(26):
        decrypted_phrase = decrypt(encrypted_phrase, shift)
        test_phrase = decrypted_phrase.split()

        if all(word.lower() in reference_list for word in test_phrase if word.isalpha()):
            return ' '.join(test_phrase)
    else:
        return ''

def get_user_method():
    print('Would you like to (e)ncrypt, (d)ecrypt, (c)rack a message, or (q)uit?')
    global user_method
    user_method = input('> ')
    return user_method
        
def get_user_message():
    print('Please enter your message: ')
    global message
    message = input('> ')
    return message

def run_encryption(message):
    print('Please enter the number of shifts for this message')
    shift_input = input('> ')
    shift = int(shift_input)
    encrypted_message = encrypt(message, shift)
    print(encrypted_message)
    return encrypted_message

def run_decryption(message):
    print('Please enter the number of shifts for this message')
    shift_input = input('> ')
    shift = int(shift_input)
    decrypted_message = decrypt(message, shift)
    print(decrypted_message)
    return decrypted_message

def run_crack(message):
    cracked_message = crack(message)
    print(cracked_message)
    return cracked_message

def run_methods(message):
    if user_method == 'e':
        return run_encryption(message)
    if user_method == 'd':
        return run_decryption(message)
    if user_method == 'c':
        return run_crack(message)

def run_program(method, user_message):
    while True:
        get_user_method()
        if user_method == 'q':
            break
        get_user_message()
        run_methods(message)

user_method = None
message = None


if __name__ == '__main__':
    run_program(user_method, message)
