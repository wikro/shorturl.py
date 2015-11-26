DIGITS='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE=len(DIGITS)

def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def base62_decode(s):
    try:
        r, m = 0,1
        for c in reversed(s):
            r += m*DIGITS.index(c)
            m *= BASE
        return str(r)
    except ValueError:
        return '0'

def base62_encode(i):
    i = int(i)
    if i < 0: raise Exception("negative number: %s" % i)
    if i == 0: return '0'
    r = ''
    while i != 0:
        r = (DIGITS[i%BASE])+r
        i = int(i/BASE)
    return str(r)
