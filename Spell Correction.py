from textblob import TextBlob

words= ['cricket','pytho','srinivs','vuppal']

#take one empty list to store the corrected words

spell_corrected_words = []

for word in words:
    spell_corrected_words.append(TextBlob(word))
print("Misspelled words: ", words)
print("corrected words: ")

for word in spell_corrected_words:
    print(word.correct() , end =" ")
                                 