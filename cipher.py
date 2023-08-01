# Alphabet list, to compare values and index locations.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Get sentence string and shift value from user.
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
        # Start loop with encryption status = false. Prevents alphabet characters from getting overwritten
        # by non-alphabet character if conditions.
        letter_encrypted = False
        for letter_location in alphabet:
            if letter == letter_location:
                # Location of input character in alphabet list.
                new_letter_location = alphabet.index(letter_location)
                # Shifts list location by user determined amount for cipher.
                new_letter_location += encryption_offset
                # Loops end-of-alphabet characters to beginning.
                if new_letter_location > 25:
                    new_letter_location -= 26
                # Replaces letter in word. Important to maintain list in list for maintaining sentence structure.
                new_letter = letter.replace(letter, alphabet[new_letter_location])
                letter_encrypted = True
            # Preserves non-alphabet characters.
            elif letter_location == "z" and letter_encrypted == False:
                new_letter = letter
        # Builds new encrypted words from the replaced letters.
        encrypted_word.append(new_letter)
    # Builds new encrypted sentences from the encrypted words.
    encrypted_sentence.append(encrypted_word)

#Loop through list. Loops through letters, adding each to new print sentence. Loop through words, adding space
# to end of words.
print_sentence = ""
for word in encrypted_sentence:
    for letter in word:
        print_sentence += str(letter)
    print_sentence += str(" ")
print("Your encrypted message: " + print_sentence)










