def word_count(str):
    counts = dict()   #here keys are indices values are words
    words = str.split() #onverting str into list
    
    #str-->list
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count("srinivas vuppala srinivas vuppala 50"))

