<img src="logo.PNG" />

# Crapo

## Introduction

A simple tool to encrypt/decrypt your personnals/private files or directory.

**NB:** Am not responsible of the bad use of this project, so be sure to use it properly.

## installation

To install Crapo, just hit theese commands:

```shell
pip install --upgrade setuptools pip
pip install setuptools --upgrade --ignore-installed
pip install -r requirements.txt
```

### List of parameters

```php
## -----------------------------------------------------------------
## Launch the script and pass theese parameters

[REQUIRED] `method` : "encrypt" or "decrypt" (Only theese method are supported)
[REQUIRED] `path` : "Your_directory" or "Your.file" (You can provide a path of a file or directory (it will work recursively))
[REQUIRED] `key` : "sanix_code" (You just need to specify the key of the encryption)
[OPTIONNAL] `erase`: "erase" (This parameter is used when you encrypt a file and want to delete  the original file/directory)
```

### Usage

#### Basic Usage

```shell
# Clone the project
git clone https://github.com/sanix-darker/crapo

# cd to the project
cd to/path/of/the/project

# To encrypt or decrypt, hit this command and follow instructions
python ./src/main.py
```

#### Basic output

```shell

> -----------------------------------------------------------------------------
> --- Crapo v0.1---------------------------------------------------------------
> -----------------------------------------------------------------------------
>                                                              By Sanix darker
> -----------------------------------------------------------------------------
> Crapo is starting OK:

> What do you want to do encrypt or Decrypt?
> Method: (e / d) or (en / de):en
> Give me a valid path of your file/directory!
> Path (of a file or directory):./logo.PNG
> Give me the secret Code!(You will not able to see what you hit, cuz it's secret right?) 
> Secret_code:*******
> Do you want to erase origin's files after encryption ?
> Erase (y / n):n
> Checking the path
> Verifying the file given
> Working on:  ./logo.PNG
> encrypting  ./logo.PNG
> ./logo.PNG  encrypted!

> -----------------------------------------------------------------------------
> Crapo: Process ended! OK! Thank's you using me!
> -----------------------------------------------------------------------------
```

## DEMO HERE

[See DEMO](https://youtu.be/MajlnQmW7vQ)

## Author

- [Sanix-darker](https://github.com/sanix-darker)