#!/usr/bin/env python3
#coder by my-pixel
#this is text encode tool

#library
from cryptography.fernet import Fernet
from time import time, sleep
from tqdm import tqdm
import sys
import hashlib
import pyaes
import os
import pybase64
import base64
import binascii

#variables
data = ""
a = ""
kind = ""
key = ""
space = " "
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

#program name
print("""
 .::.    :::.    :::.  .,-:::::      ...     :::::::-.   .::.    :::::::..   
;'`';;,  `;;;;,  `;;;,;;;'````'   .;;;;;;;.   ;;,   `';,;'`';;,  ;;;;``;;;;  
   .n[[    [[[[[. '[[[[[         ,[[     \[[, `[[     [[   .n[[   [[[,/[[['  
  ``"$$$.  $$$ "Y$c$$$$$         $$$,     $$$  $$,    $$  ``"$$$. $$$$$$c    
  ,,o888"  888    Y88`88bo,__,o, "888,_ _,88P  888_,o8P'  ,,o888" 888b "88bo,
  YMMP"    MMM     YM  "YUMMMMMP"  "YMMMMMP"   MMMMP"`    YMMP"   MMMM   "W"
  """)

#exit fonction 
def muck():
    print(" EXİTİNG...")
    sys.exit()

#print fonction
def write():
    print("\n")
    print("encrypted key: ", key)
    print("salt text: ",data)
    print("encryption type: ",kind)
    print("encrypted text: ", a)

#help
if sys.argv[1] in ["-h"]:
    print("""
 [-h]  help
 [-s]  encryption
 [-v]  version
 [-d]  aes decryption""")

#hash types
elif sys.argv[1] in ["-s"]:
    data = input("Data to be encrypted: ")
    str = data
    kind = input("""

 1)sha1        10)sha3_384
 2)sha224      11)aes
 3)sha256      12)fernet
 4)sha384      13)binary
 5)sha3_512    14)ASCII
 6)sha3_256    15)base64
 7)sha3_224    16)base85
 8)md5         17)hex
 9)sha512      18)morse code\n        
 Enter number:""")
    
    #hashlib library encryption
    if(kind == "1"):
        kind = "sha1"
        a = hashlib.sha1(str.encode()).hexdigest()
    
    elif(kind == "2"):
        kind = "sha254"
        a = hashlib.sha224(str.encode()).hexdigest()

    elif(kind == "3"):
        kind = "sha256"
        a = hashlib.sha256(str.encode()).hexdigest()

    elif(kind == "4"):
        kind == "sha384"
        a = hashlib.sha384(str.encode()).hexdigest()

    elif(kind == "9"):
        kind = "sha512"
        a = hashlib.sha512(str.encode()).hexdigest()

    elif(kind == "8"):
        kind = "md5"
        a = hashlib.md5(str.encode()).hexdigest()

    elif(kind == "7"):
        kind = "sha3_224"
        a = hashlib.sha3_224(str.encode()).hexdigest()

    elif(kind == "6"):
        kind = "sha3_256"
        a = hashlib.sha3_256(str.encode()).hexdigest() 

    elif(kind == "10"):
        kind = "sha3_384"
        a = hashlib.sha3_384(str.encode()).hexdigest()

    elif(kind == "5"):
        kind = "sha3_512"
        a = hashlib.sha3_512(str.encode()).hexdigest()
        
    elif(kind == "11"):

        kind = "aes"
        
        ch = input(" Do you want new key (y/n): ")
        if (ch == "y"):

            for i in tqdm(range(32)):
                    sleep(0.2)
                    pass
            key = os.urandom(32)
            print("New key created")
            sleep(1)
            
        elif (ch == "n"):
            key = b'\xd6\xba\xc3\x86!z\xae\xc3\xdf\x0b\x920o\xc6\xfd\xb9\xd8\x0e\xaf\xb9\xb2z\xb8\xad\x8b\xe3\xa2\xc7\xa2\xa4\xbe\x97'
        
        #aes encryption
        def encrypt(plaintext, key):
            
            aes = pyaes.AESModeOfOperationCTR(key)
            ciphertext = aes.encrypt(plaintext)
            return ciphertext

        e = encrypt(data, key)
        a = e.decode('latin-1')
        
    elif(kind == "12"):

        kind = "fernet"
        str = data
        
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        ciphertext = cipher_suite.encrypt(str.encode())
        a = ciphertext.decode('latin-1')

        orginal_text = cipher_suite.decrypt(ciphertext)
        data = orginal_text.decode('latin-1')
        
    elif(kind == "13"):

        kind = "binary"
        
        # Converting String to binary 
        res = ' '.join(format(ord(i), 'b') for i in data)   
        # printing result  
        a = res

    elif(kind == "14"):

        kind = "ASCII"

        #Converting data to ASCII
        rek = ' '.join(format(ord(i)) for i in data)
        a = rek

    elif(kind == "15"):

        kind = "base64"

        #Converting data to bytes 
        data = data.encode('utf-8')

        a = pybase64.b64encode(data).decode('utf-8')

        #Repeat converting of salt text
        data = data.decode('utf-8')
        
    elif(kind == "16"):

        kind = "base85"

        #Converting data to bytes 
        data = data.encode('utf-8')

        a = base64.b85encode(data).decode('utf-8')

        #Repeat converting of salt text
        data = data.decode('utf-8')


    elif(kind == "17"):

        kind = "hex"
        
        k = ' '.join(i.encode('utf-8').hex() for i in data)
        
        a = k.upper()
    elif(kind == "18"):

        kind = "morse code" 
        
# Function to encrypt the string 
# according to the morse code chart 
        def encrypt(message):
            
                        cipher = ''
                        
                        for letter in message: 
                                if letter != ' ': 
 
                                    cipher += MORSE_CODE_DICT[letter] + ' '
                                    
                                else: 
                                # 1 space indicates different characters 
                                # and 2 indicates different words 
                                    cipher += ' '

                        return cipher

        # Hard-coded driver function to run the program 
        def main(): 
                    message = data
                    
        a = encrypt(data.upper())
                    
# Executes the main function 
        if __name__ == '__main__': 
                 main()
        else:
            main()
    else:
        print(" Number not found!")
        muck()
        
#sofware info
elif sys.argv[1] in ["-v"]:
    print("""
PROGRAM İNFO

Coder by my-pixel
This tool is hash maker
""")

#aes decryption
elif sys.argv[1] in ["-d"]:

    print("""
1)base64
2)base85
3)aes
""")
    number = input("Enter number:")

    if(number == "1"):

        data = input("Data to be decrypted: ")

        data = data.encode('utf-8') 
        
        yep = pybase64.b64decode(data, altchars='_:', validate=True)

        print("Decryption text: ", yep.decode('utf-8'))
        
    elif(number == "2"):

        data = input("Data to be decrypted: ")

        data = data.encode('utf-8') 
        
        yep = base64.b85decode(data)

        print("Decryption text:", yep.decode('utf-8'))
        
    elif(number == "3"):
        
        key = b'\xd6\xba\xc3\x86!z\xae\xc3\xdf\x0b\x920o\xc6\xfd\xb9\xd8\x0e\xaf\xb9\xb2z\xb8\xad\x8b\xe3\xa2\xc7\xa2\xa4\xbe\x97'
    
        data = input("Data to be decrypted: ")
    
        int = data
        aes = pyaes.AESModeOfOperationCTR(key)
        plaintext = aes.decrypt(data)
    
        print("Decryption text: ", plaintext.decode('latin-1'))
    else: 
        print(" Number not found!")
        muck()

else:
    muck()

if key == "":
    key = "not found!"
else:
    key = key

if a == "" or data == "":
    print("")
else:
    load = len(data)
    load = load + 4
    
    for i in tqdm(range(load)):
        sleep(0.5)
        pass
    write()
