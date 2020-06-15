def calculate_years(principal, interest, tax, desired):
    count = 0
    if principal ==desired:
        return 0
    while principal <= desired:
        principal = principal+(principal * interest)-(principal*interest*tax)
        count=count + 1
        print (count)
    return count 
