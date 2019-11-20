import getpass
from os import  path as ospath, remove as osremove, stat as osstat

try: import pyAesCrypt
except ImportError as es: exit(str(es))


# encryption / Decryption buffer size - 64K
bufferSize = 64 * 1024


def crapo_start():

    print("\n> -----------------------------------------------------------------------------")
    print("> --- Crapo v0.1---------------------------------------------------------------")
    print("> -----------------------------------------------------------------------------")
    print(">                                                              By Sanix darker")
    print("> -----------------------------------------------------------------------------\n> Crapo is starting OK:\n")


def crapo_end():

    print("\n> -----------------------------------------------------------------------------")
    print("> Crapo: Process ended! OK! Thank's you using me!")
    print("> -----------------------------------------------------------------------------\n")


def encrypt(path, key):
    print("> encrypting ", path)
    # encrypt
    with open(path, "rb") as fIn:
        with open(path+".crp0", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, str(key), bufferSize)
            print(">", path, " encrypted!")


def decrypt(path, key):
    print("> Decrypting ", path)
    # get encrypted file size
    enc_file_size = osstat(path).st_size
    # decrypt
    with open(path, "rb") as fIn:
        with open(path.replace(".crp0", ""), "wb") as fOut:
            try:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, str(key), bufferSize, enc_file_size)
                print(">", path, " decrypted!")
            except ValueError:
                # remove output file on error
                exit("> Error Groulps!!! Verify the key")
                # osremove(path)



def check_encrypt_or_decrypt(do, path, key, erase_it):
    """[summary]

    Arguments:
        do {[type]} -- [description]
        path {[type]} -- [description]
        key {[type]} -- [description]
        erase_it {[type]} -- [description]
    """
    if("encrypt" in str(do).lower()):
        if ".crp0" not in path and ".crp__" not in path:
            print("> Working on: ", path)
            encrypt(path, key)
            # Delete file if erase is confirmed
            if erase_it == True:
                print("> Removing the original : ", path.replace(".crp0", ""))
                try:
                    osremove(path.replace(".crp0", ""))
                except:
                    print("> Can't remove due to Permissions purposes or something else!")
                    print("> Skipping: ", path.replace(".crp0", ""))
        else: print("> Skipping: ", path)
    elif("decrypt" in str(do).lower()):
        if ".crp0" in path:
            print("> Working on: ", path)
            decrypt(path, key)
            osremove(path)
        else: print("> Skipping: ", path)
    else: exit("> Command Error choose either 'encrypt' or 'decrypt'")


def do_stuff(do, path, key, erase_it):
    """[summary]

    Arguments:
        do {[type]} -- [description]
        path {[type]} -- [description]
        key {[type]} -- [description]
        erase_it {[type]} -- [description]
    """
    if(ospath.isfile(path)):
        check_encrypt_or_decrypt(do, path, key, erase_it)
    elif(ospath.isdir(path)):
        print("> ----------")
        print("> In "+path)
    else: exit("> Can't proceed!")



def var_exist(varr):
    if varr in locals() or varr in globals():
        return True
    return False


def error_oooo():
    string_to_exit = "\n----------------------------------------------------------------------------- "
    string_to_exit += "\n> Crapo: Grrlouups!! \n> Bad parameters passed, please use Crapo like this: "
    string_to_exit += "\n> Ex: crapo encrypt ./file_or_directory secret_password. "
    string_to_exit += "\n> Ex: crapo decrypt ./file_or_directory secret_password\n"
    exit(string_to_exit)



def get_method():
    method = input("> What do you want to do encrypt or Decrypt? \n> Method: (e / d) or (en / de):")
    if "d" in method.lower() or "de" in method.lower():
        return "decrypt"
    elif "e" in method.lower() or "en" in method.lower():
        encrypt = True
        return "encrypt"
    else: exit("> Error, Make a good choice of the method!")



def get_path():
    path = input("> Give me a valid path of your file/directory! \n> Path (of a file or directory):")
    path = ' '.join(path.split())
    if ospath.isfile(path) == False and ospath.isdir(path) == False:
        exit("> Error, Choose a valid path!")
    else:
        if " " in path :
            path = '"' + path + '"'
        return path



def get_secret():
    secret = getpass.getpass("> Give me the secret Code!(You will not able to see what you hit, cuz it's secret right?) \n> Secret_code:")
    if len(secret) > 0: return secret
    else: exit("> Error, Please provide the secret code")



def get_erase():
    erase = input("> Do you want to erase origin's files after encryption ? \n> Erase (y / n):")
    if "y" in erase.lower(): return "erase"
    elif "n" in erase.lower(): return ""
    else: exit("> Error, Please Choose if you want to erase Origin's files")


def check_blacklist(path):
    if('\.' in path.lower() or '/.' in path.lower() or '/framework/' in path.lower() or '\\framework\\' in path.lower() or '/vendors/' in path.lower() or '\\vendors\\' in path.lower() or '/bundles/' in path.lower() or '\\bundles\\' in path.lower() or '/lib/' in path.lower() or '\\lib\\' in path.lower()or '/plugins/' in path.lower() or '\\plugins\\' in path.lower() or '.min.' in path.lower() or '/bower_components/' in path.lower() or '\\bower_components\\' in path.lower()  or '/node_components/' in path.lower() or '\\node_components\\' in path.lower()):
        return True
    return False