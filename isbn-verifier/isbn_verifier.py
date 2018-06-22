def verify(isbn):
    if len (isbn) == 10 and isbn.digits == True:
        return True
    elif len (isbn) == 10 and isbn[-1:] == 'X':
        return True
    else:
        return False
