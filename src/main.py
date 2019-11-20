#!/usr/bin/env python
# coding=utf-8

#
# ---------------------------
# / __| '__/ _` | '_ \ / _ \
#| (__| | | (_| | |_) | (_) |
# \___|_|  \__,_| .__/ \___/
#               |_|
# ---------------------------
# Crypt your files / directories easy
# Made by S@n1X-d4rk3r
#

from os import path as ospath
from sys import exit
import base64
from methods import *

try: from pathlib import Path
except ImportError as es: exit(str(es))

crapo_start()
erase, encrypt = False, False
method_get, path_get, secret_get, erase_get = get_method(), get_path(), get_secret(), get_erase()


def main_process():

    if var_exist(method_get):
        path = path_get
        key = base64.b64encode(b""+str.encode(secret_get))

        print("> Checking the path")
        if(ospath.exists(path)):
            if(ospath.isfile(path)):
                print("> Verifying the file given")
                do_stuff(method_get, str(path), key, erase)
            else:
                if(ospath.isdir(path)):
                    # if it start with .
                    if (check_blacklist(path)):
                        print("> Skipping: ", path)
                    else:
                        print("> In "+path)
                        for path in Path(path).glob('**/*'):
                            # because path is object not string
                            # encrypt or decrypt if it's only a file
                            do_stuff(method_get, str(path), key, erase)
                else: print("> This path " + str(path) + " is not valid, please verify it again before relaunch me.")
        else: print("> This path " + str(path) + " (file/directory) is not valid.")

    else: error_oooo()


def main():

    if "erase" in str(erase_get): erase = True

    main_process()
    crapo_end()

if __name__ == '__main__':
    main()