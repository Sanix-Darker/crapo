#!/usr/bin/env python
# coding=utf-8
# start.py
# Made by S@n1X-d4rk3r

import os, sys, time
import getpass

print("\n> -----------------------------------------------------------------------------")
print("> --- Crapo v0.1---------------------------------------------------------------")
print("> -----------------------------------------------------------------------------")
print(">                                                              By Sanix darker")
print("> -----------------------------------------------------------------------------\n> Crapo is starting Grrlouups:\n")

Encrypt = False

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

os.system('python crapo.py '+getMethod()+' '+getPath()+' '+getSecret()+' '+ getErase()+' not_cli')

time.sleep(10)