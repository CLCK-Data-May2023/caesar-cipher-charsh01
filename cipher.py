# Alphabet list, to compare values and index locations.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Get sentence and shift value from user.
sentence_to_encrypt = input("Please enter a message to encrypt: ")
encryption_offset = int(input("Please enter the character shift amount for encryption: "))

# Get character location in list. Shift that value by user input amount. Replace letter with new letter via
# alphabet index location.

# Split sentence into list containing individual words.
words_to_encrypt = sentence_to_encrypt.split()
encrypted_sentence = []

for word in words_to_encrypt:
    encrypted_word = []
    for letter in word:
        new_letter = ""
        for letter_location in alphabet:
            if letter == letter_location:
                new_letter_location = alphabet.index(letter_location)
                new_letter_location += encryption_offset
                if new_letter_location > 25:
                    new_letter_location -= 26
                new_letter = letter.replace(letter, alphabet[new_letter_location])
        encrypted_word.append(new_letter)
    encrypted_sentence.append(encrypted_word)

#Loop through list. Loops through letters, adding each to new print sentence. Loop through words, adding space
# to end of words.
print_sentence = ""
for word in encrypted_sentence:
    for letter in word:
        print_sentence += str(letter)
    print_sentence += str(" ")
print(print_sentence)










