def spin_words(sentence):
    array = []
    for i in sentence.split():
        if len(i) >= 5:
            array.append(i[::-1])
        else:
            array.append(i)        
    return ' '.join(array)
