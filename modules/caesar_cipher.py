from corpus import reference_list

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

        if all(word.lower() in reference_list for word in test_phrase):
            return ' '.join(test_phrase)

phrase = encrypt('Cross the Rubicon', 3)
print(crack(phrase))
