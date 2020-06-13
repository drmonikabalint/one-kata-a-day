def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    else:
        for x in range(3, n):      
            signature.append(sum (signature[-3:]))
        return (signature)
