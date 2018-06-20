def is_isogram(string):

    str=string.lower()

    word=[]
    for a in str:
        if a.isalpha():
            if a in word:
                return False
            word.append(a)
    return True

