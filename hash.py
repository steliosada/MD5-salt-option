import hashlib  


def add_salt(str2hash):
    
    saltchoice = input("(F)ront or (B)ack: ")
    if saltchoice == 'F':
        salt = input("Give me salt: ")
        str2hash=salt+str2hash
        result = hashlib.md5(str2hash.encode())
        print("Done.")
        print("The hash is :",  result.hexdigest())

    elif saltchoice == 'B':
        salt = input("Give me salt: ")
        str2hash=str2hash+salt
        result = hashlib.md5(str2hash.encode())
        print("Done.")
        print("The hash is :",  result.hexdigest())
        
    else:
        print("No Option selected, closing...")
    
# Main
str2hash=input("Give string to MD5: ")

choice = input("Would you like to add Salt?(Y)es or (N)o?: ")
if choice == 'Y':
        add_salt(str2hash)

elif choice == ("N"):
        result = hashlib.md5(str2hash.encode())
        print("The hash is :" , result.hexdigest())
    
else:
        print("No Option selected, closing...")

pause = input("Press any Key to exit")
        