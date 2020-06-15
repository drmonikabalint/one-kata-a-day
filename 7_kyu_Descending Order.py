def descending_order(num):
    # Bust a move right here
    res = [int (i) for i in str(num)] 
    res_sorted = sorted (res, reverse = True)
    return int("".join([str(i) for i in res_sorted]))
