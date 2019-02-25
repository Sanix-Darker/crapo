#!/usr/bin/env python
# coding=utf-8
# Crapo
# Crypt your files / directories easy
# Made by S@n1X-d4rk3r

import os, sys, time
import getpass
import pyAesCrypt
import base64
from pathlib import Path

# Encryption / Decryption buffer size - 64K
bufferSize = 64 * 1024

def encrypt(path, key):
    print("> Encrypting ", path)
    # encrypt
    with open(path, "rb") as fIn:
        with open(path+".crp0", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, str(key), bufferSize)
            print(">", path, " encrypted!")

def decrypt(path, key):
    print("> Decrypting ", path)
    # get encrypted file size
    encFileSize = os.stat(path).st_size
    # decrypt
    with open(path, "rb") as fIn:
        with open(path.replace(".crp0", ""), "wb") as fOut:
            try:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, str(key), bufferSize, encFileSize)
                print(">", path, " decrypted!")
            except ValueError:
                # remove output file on error
                sys.exit("> Error Groulps!!! Verify the key")
                # os.remove(path)

def do_stuff(do, path, key, erase_it):
    if(os.path.isfile(path)):
        if("encrypt" in str(do).lower()):
            if ".crp0" not in path and ".crp__" not in path: 
                print("> Working on: ", path)
                encrypt(path, key)
                # Delete file if erase is confirmed
                if erase_it == True:
                    print("> Removing the original : ", path.replace(".crp0", ""))
                    try:
                        os.remove(path.replace(".crp0", ""))
                    except:
                        print("> Can't remove due to Permissions purposes or something else!")
                        print("> Skipping: ", path.replace(".crp0", ""))
                    # os.remove(path.replace(".crp__", ""))
            else:
                print("> Skipping: ", path)
        elif("decrypt" in str(do).lower()):
            if ".crp0" in path: 
                print("> Working on: ", path)
                decrypt(path, key)
                os.remove(path)
                # os.remove(path.replace(".crp0", ".crp__"))
            else:
                print("> Skipping: ", path)
        else:
            sys.exit("> Command Error choose either 'encrypt' or 'decrypt'")
    elif(os.path.isdir(path)):
        print("> ----------")
        print("> In "+path)
    else:
        sys.exit("> Can't proceed!")

def var_exist(varr):
    if varr in locals() or varr in globals():
        return True
    else:
        return False

def error_oooo():
    sys.exit("\n----------------------------------------------------------------------------- \n> Crapo: Grrlouups!! \n> Bad parameters passed, please use Crapo like this: \n> Ex: crapo encrypt ./file_or_directory secret_password. \n> Ex: crapo decrypt ./file_or_directory secret_password\n")


def getMethod():
    method = input("> What do you want to do Encrypt or Decrypt? \n> Method: (e / d) or (en / de):")
    if "d" in method.lower() or "de" in method.lower():
        return "decrypt"
    elif "e" in method.lower() or "en" in method.lower():
        Encrypt = True
        return "encrypt"
    else:
        sys.exit("> Error, Make a good choice of the method!")

def getPath():
    path = input("> Give me a valid path of your file/directory! \n> Path (of a file or directory):")
    path = ' '.join(path.split())
    if os.path.isfile(path) == False and os.path.isdir(path) == False:
        sys.exit("> Error, Choose a valid path!")
    else:
        if " " in path :
            path = '"' + path + '"'
        return path

def getSecret():
    secret = getpass.getpass("> Give me the secret Code!(You will not able to see what you hit, cuz it's secret right?) \n> Secret_code:")
    if len(secret) > 0:
        return secret
    else:
        sys.exit("> Error, Please provide the secret code")

def getErase():
    erase = input("> Do you want to erase origin's files after encryption ? \n> Erase (y / n):")
    if "y" in erase.lower():
        return "erase"
    elif "n" in erase.lower():
        return ""
    else:
        sys.exit("> Error, Please Choose if you want to erase Origin's files")



def main():
    erase = False

    print("\n> -----------------------------------------------------------------------------")
    print("> --- Crapo v0.1---------------------------------------------------------------")
    print("> -----------------------------------------------------------------------------")
    print(">                                                              By Sanix darker")
    print("> -----------------------------------------------------------------------------\n> Crapo is starting Grrlouups:\n")

    Encrypt = False

    method_get = getMethod()
    path_get = getPath()
    secret_get = getSecret()
    erase_get = getErase()

    if "erase" in str(erase_get):
        erase = True

    if var_exist(method_get):
        path = path_get
        key = base64.b64encode(b""+str.encode(secret_get))

        print("> Checking the path")
        if(os.path.exists(path)):
            if(os.path.isfile(path)):
                print("> Vefiying the file given")
                do_stuff(method_get, str(path), key, erase)
            else:
                if(os.path.isdir(path)):
                    # if it start with .
                    if('\.' in path.lower() or '/.' in path.lower() or '/framework/' in path.lower() or '\\framework\\' in path.lower() or '/vendors/' in path.lower() or '\\vendors\\' in path.lower() or '/bundles/' in path.lower() or '\\bundles\\' in path.lower() or '/lib/' in path.lower() or '\\lib\\' in path.lower()or '/plugins/' in path.lower() or '\\plugins\\' in path.lower() or '.min.' in path.lower() or '/bower_components/' in path.lower() or '\\bower_components\\' in path.lower()  or '/node_components/' in path.lower() or '\\node_components\\' in path.lower()):
                        print("> Skipping: ", path)
                    else:
                        print("> Vefiying files in the directory given")
                        print("> ---------")
                        print("> In "+path)
                        for path in Path(path).glob('**/*'):
                            # because path is object not string
                            # encrypt or decrypt if it's only a file
                            do_stuff(method_get, str(path), key, erase)                     
                else:
                    print("> This path " + str(path) + " is not valid, please verify it again before relaunch me.")
        else:
            print("> This path " + str(path) + " (file/directory) is not valid.")

    else:
        error_oooo()
    print("\n> -----------------------------------------------------------------------------")    
    print("> Crapo: Process ended! Grrlouups! Thank's you using me!")
    print("> -----------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()