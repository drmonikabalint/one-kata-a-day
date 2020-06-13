def to_jaden_case(string):
    return ' '.join(x[:1].upper() + x[1:] for x in string.split(' '))
