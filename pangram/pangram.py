def is_pangram(sentence):
    List = []

    for i in range(26):
        List.append(False)


    for c in sentence.lower():
        print(c)
        if not c == " ":
            List[ord(c) - ord('a')] = True
        elif c.isdigit() :
            List[c+ord('a')] = True

    for ch in List:
        if ch == False:
            return False
    return True
