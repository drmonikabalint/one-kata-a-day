def high_and_low(numbers):
    
    array = [int(x) for x in numbers.split(' ')]
    array.sort()
    return '{} {}'.format(array[-1], array[0])
