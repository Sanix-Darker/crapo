# Crapo
# Crypt your file easy
# By 🐼Sanix darker

import os
import sys
import argparse

from clint.arguments import Args
#from pyfilesec import SecFile
import pyAesCrypt
from pathlib import Path

import base64

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
args = Args()

def encrypt(path, key):
    print("> Encrypting ", path)
    # encrypt
    with open(path, "rb") as fIn:
        with open(path+".crp", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, str(key), bufferSize)
            # sf = SecFile(path+".crp")
            # sf.encrypt(path)
            print(">", path, " encrypted!")

def decrypt(path, key):
    print("> Decrypting ", path)
    # get encrypted file size
    encFileSize = os.stat(path).st_size
    # decrypt
    # sf = SecFile(path+".crp")
    # sf.decrypt(path)
    with open(path, "rb") as fIn:
        with open(path.replace(".crp", ""), "wb") as fOut:
            try:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, str(key), bufferSize, encFileSize)
                print(">", path, " decrypted!")
            except ValueError:
                # remove output file on error
                os.remove(path)

def do_stuff(do, path, key, erase_it):
    if(os.path.isfile(path)):
        if("encrypt" in str(do).lower()):
            if ".crp" not in path: 
                print("> Working on: ", path)
                encrypt(path, key)
                # Delete file if erase is confirmed
                if erase_it == True:
                    os.remove(path.replace(".crp", ""))
            else:
                print("> Skipping: ", path)

        elif("decrypt" in str(do).lower()):
            if ".crp" in path: 
                print("> Working on: ", path)
                decrypt(path, key)
                os.remove(path)
            else:
                print("> Skipping: ", path)

        else:
            sys.exit("> Command Error choose either 'encrypt' or 'decrypt'")

    elif(os.path.isdir(path)):
        print("> ---------")
        print("> In "+path)
    else:
        sys.exit("> Can't proceed!")


def var_exist(varr):
    if varr in locals() or varr in globals():
        return True
    else:
        return False

def error_oooo():
    sys.exit("\n-----------------------------------------------------------------------------\nCrapo: Grrlouups!!\nBad parameters passed, please use Crapo like this: \nEx: crapo encrypt ./file_or_directory secret_password\nEx: crapo decrypt ./file_or_directory secret_password\n")

def main():
    erase = False
    
    if len(args.all) == 0:
        error_oooo()
    else:

        if len(args.all) >= 4:
            if "erase" in str(args.all[3]):
                erase = True

        if var_exist(args.all[0]):
            path = args.all[1]
            key = base64.b64encode(b""+str.encode(args.all[2]))
            print("\n> -----------------------------------------------------------------------------")
            print("> --- Crapo v0.1---------------------------------------------------------------")
            print("> -----------------------------------------------------------------------------")
            print(">                                                             By 🐼Sanix darker")
            print("> -----------------------------------------------------------------------------\n> Crapo is starting Grrlouups:\n")
            print("> Checking the path")
            if(os.path.exists(path)):
                if(os.path.isfile(path)):
                    print("> Vefiying the file given")
                    do_stuff(args.all[0], str(path), key, erase)
                else:
                    if(os.path.isdir(path)):
                        print("> Vefiying files in the directory given")
                        print("> ---------")
                        print("> In "+path)
                        for path in Path(path).glob('**/*'):
                            # because path is object not string
                            # encrypt or decrypt if it's only a file
                            do_stuff(args.all[0], str(path), key, erase)                     
                    else:
                        print("> This path(file/directory) is not valid, please restart again")
            else:
                print("> This path(file/directory) is not valid.")

        else:
            error_oooo()
    print("\n> -----------------------------------------------------------------------------")    
    print("> Crapo: Process ended! Grrlouups! Thank's you using me!")
    print("> -----------------------------------------------------------------------------\n")
            
main()