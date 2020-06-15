def rot13(message):
    # traverse text 
    result = ""
    for i in range(len(message)): 
        char = message[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + 13-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        elif (char.islower()): 
            result += chr((ord(char) + 13- 97) % 26 + 97) 
        else:
            result += chr (ord(char))
    return result 
    
