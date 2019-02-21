# Crapo
# Crypt your file easy
# By Sanix darker

# from Crypto.Hash import SHA256
# from Crypto.Cipher import AES
# from Crypto import Random
# import os, random, sys, pkg_resources
 
import os, sys, optparse
import argparse

from clint.arguments import Args
#from pyfilesec import SecFile
import pyAesCrypt

import base64

from pathlib import Path

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
args = Args()

# from uuid import getnode as get_mac
# mac = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 120, 20))
# with open("SECRET_ID", "w") as fOut:
#     fOut.write(str(base64.b64encode(b""+str.encode(mac))))
# def crapo_encrypt(key, filename):
#     FileCipher(filename,filename.replace(".crp0", ".crp__"),mac,"E")
 
# def crapo_decrypt(key, filename):
#     FileCipher(filename,filename.replace(".crp__", ".crp0"),mac,"D")

# os.system("pip install pyAesCrypt")

def encrypt(path, key):
    print("> Encrypting ", path)
    # encrypt
    with open(path, "rb") as fIn:
        with open(path+".crp0", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, str(key), bufferSize)
            # crapo_encrypt(key, path+".crp0")
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
                # crapo_decrypt(key, path+".crp0")
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
                    os.remove(path.replace(".crp0", ""))
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

            if len(args.all) < 5:
                print("\n> -----------------------------------------------------------------------------")
                print("> --- Crapo v0.1---------------------------------------------------------------")
                print(">                                                              By Sanix darker")
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