
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")#,
            # ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"))

sentence_to_encrypt = input("Please enter a message to encrypt: ")
# encryption_offset = input("Please enter the character shift amount for encryption: ")
encryption_offset = 5

# Removed: ability to input cipher shift.
# if str.isdigit(encryption_offset) == False:
#     print("Integer value required. Please try again.")
#     exit()

words_to_encrypt = sentence_to_encrypt.split()
encrypted_sentence = []
for word in words_to_encrypt:
    encrypted_word = []
    for letter in word:
        letter = letter.lower()
        # Removed: ability to substitute capitalized letters.
        letter_encrypted = False
        # case = 0
        # if letter.isupper() == True:
        #     case = 1
        for letter_location in alphabet:
            if letter == letter_location:
                new_letter_location = alphabet.index(letter_location)
                new_letter_location += encryption_offset
                if new_letter_location > 25:
                    new_letter_location -= 26
                new_letter = letter.replace(letter, alphabet[new_letter_location])
                letter_encrypted = True
            elif letter_location == "z" and letter_encrypted == False:
                new_letter = letter
        encrypted_word.append(new_letter)
    encrypted_sentence.append(encrypted_word)

print_sentence = ""
for word in encrypted_sentence:
    for letter in word:
        print_sentence += str(letter)
    print_sentence += str(" ")
print("The encrypted sentence is: " + print_sentence)










