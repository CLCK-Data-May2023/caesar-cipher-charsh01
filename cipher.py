# Alphabet tuple, to compare values and index locations.
alphabet = (("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"),
            ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"))

# Get sentence string and shift value from user.
sentence_to_encrypt = input("Please enter a message to encrypt: ")
# encryption_offset = input("Please enter the character shift amount for encryption: ")

encryption_offset = 5
# if str.isdigit(encryption_offset) == False:
#     print("Integer value required. Please try again.")
#     exit()

# Split sentence into list containing individual words.
words_to_encrypt = sentence_to_encrypt.split()
encrypted_sentence = []

for word in words_to_encrypt:
    encrypted_word = []
    for letter in word:
        # Start loop with encryption status = false. Prevents alphabet characters from getting overwritten
        # by non-alphabet / capitalization character handling conditions below.
        letter_encrypted = False
        # Tracks case of alphabet.
        case = 0
        # Checks if letter capitalized.
        if letter.isupper() == True:
            # Change to capitalized tuple in alphabet list.
            case = 1
        for letter_location in alphabet[case]:
            # When letter in user input sentence matches the current letter in alphabet loop.
            if letter == letter_location:
                # Geet location of input character in alphabet tuple.
                new_letter_location = alphabet[case].index(letter_location)
                # Shifts tuple location by user determined amount for cipher.
                new_letter_location += int(encryption_offset)
                # Loops end-of-alphabet characters to beginning if needed.
                if new_letter_location > 25:
                    new_letter_location -= 26
                # Replaces letter in word. Important to maintain sentence structure.
                new_letter = letter.replace(letter, alphabet[case][new_letter_location])
                letter_encrypted = True
            # Preserves non-alphabet characters.
            elif letter_location == "z" and letter_encrypted == False:
                new_letter = letter
        # Builds new encrypted word from the replaced letters.
        encrypted_word.append(new_letter)
    # Builds new encrypted sentence using the encrypted words.
    encrypted_sentence.append(encrypted_word)

# Loop through new sentence list. First through letters, adding each to new print sentence. Next through words,
# adding space at end of words.
print_sentence = ""
for word in encrypted_sentence:
    for letter in word:
        print_sentence += str(letter)
    print_sentence += str(" ")
print("The encrypted sentence is: " + print_sentence)










