def likes(names):
    n = len(names)
    n_1 = n - 1
    n_2 = n - 2
    before = ', '.join(names[:n_1])
    after = ','.join(names[-1:])
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return '{} likes this'.format(after) 
    elif len(names) == 2 or len(names) == 3:
        return '{} and {} like this'.format(before, after)
    else: 
        return '{} and {} others like this'.format(', '.join(names[:2]), n_2)
