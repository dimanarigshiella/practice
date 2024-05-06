#DIMANARIG, SHIELLA R.
#BSCS 3A

import hashlib
        
def hash_text(text):
    space_hash = '5C1CE938EC4B836703C845A1D8DB57348758F283' #Hash value of space
    hashed_chars = set()
    hash_text = hashlib.sha1(text.encode()).hexdigest().upper() #hash value of each character the set in upper case letter
    
    for char in text: #The iteration for space and hash value of the letter
        if char == ' ':
            if space_hash not in hashed_chars:
                hashed_chars.add(space_hash)
                print(f"{space_hash} <space>")
                
        else:
            hashed_value = hashlib.sha1(char.encode()).hexdigest().upper()
            if hashed_value not in hashed_chars:
                hashed_chars.add(hashed_value)
                print (f"{hashed_value} {char}")
    
    print(hash_text, text) #printing of output
    
text = input() #the variable for each input text
hash_text(text)

#end of program

