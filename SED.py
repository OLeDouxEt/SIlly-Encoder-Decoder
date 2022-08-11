def silly_encrypter(word_input):
    #Quick input type check
    if type(word_input) == str:
        word_list = word_input.split(" ")
        #Setting up a new list to contain all of the input words after they have been 'encrypted'
        new_words = []
        #Each Loop will slice the first character off the word and set it to a variable. Then
        #perform an open ended slice to grab the rest of the word a set it to a variable. These
        #two vars will be concatenated with the original beginning character now at the end.
        #Afer which, "IE" will be added to the end of the word, the word will be formatted to 
        #uppercase, and then appended to the 'new_words' list.
        for word in word_list:
            beginning_char = word[:1]
            word = word[1:]
            swapped_word = word + beginning_char
            encryted_word = swapped_word + "IE"
            encryted_word.upper()
            new_words.append(encryted_word)
        #joining all the words in 'new_words' seperated by a space and returning new ouput
        encryted_ouput = " ".join(new_words)
        return encryted_ouput
    else:
        return "Not a string"

def silly_decrypter(word_input):
    #Quick input type check
    if type(word_input) == str:
        word_list = word_input.split(" ")
        #Setting up a new list to contain all of the input words after they have been 'encrypted'
        new_words = []
        for word in word_list:
            #Formatting all the words to uppercase
            word = word.upper()
            #removing 'IE' from the end of each word
            cleaned_word = word.rstrip("IE")
            #Starting from the '-1' index to grab the last character and setting a var for it
            end_char = cleaned_word[-1:]
            #Ending on the '-1' index to grab the remainder of the word and setting a var for it
            piece_of_word = cleaned_word[:-1]
            complete_word = end_char + piece_of_word
            new_words.append(complete_word)
        #joining all the words in 'new_words' seperated by a space and returning new ouput
        unencryted_ouput = " ".join(new_words)
        return unencryted_ouput
    else:
        return "Not a string"

print(silly_encrypter("HAVE A NICE DAY"))

print(silly_decrypter(silly_encrypter("HAVE A NICE DAY")))