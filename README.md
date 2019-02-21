<img src="logo.PNG" >

# Crapo

## Introduction
A simple tool to encrypt/decrypt your personnals/private files or directory.

## Requirements

- Python 3.X (if you don't want to have troubleshouting on Python 2.x)

## installation

To install Crapo, just hit theese commands:
```shell
# Launch this file, il you are a linux user and follow instructions
install.sh

# Launch this file, il you are a WINDOWS user and follow instructions
install.bat

### All done.
```

### List of parameters

```php
## -----------------------------------------------------------------
## Launch the script and pass theese parameters

[REQUIRED] method : "encrypt" or "decrypt" (Only theese method are supported) 
[REQUIRED] path : "Your_directory" or "Your.file" (You can provide a path of a file or directory (it will work recursively))
[REQUIRED] key : "sanix_code" (You just need to specify the key of the encryption)
[OPTIONNAL] erase: "erase" (This parameter is use when you encrypt a file and want to delete  the original file/directory)
```

### Usage

#### Basic Usage
```shell
cd to/path/of/the/project

# Launch this file, il you are a linux user and follow instructions
starter_for_linux.sh

# if you are a WINDOWS user
# open the Cmd in this folder
python start.py

```

#### CLI Usage
```shell
cd to/path/of/the/project

# To encrypt
## For directory
python crapo.py encrypt ./Personnaldirectory/ your_secret_code
## For a directory with spaces
python crapo.py encrypt "./Personnaldirectory/Example of dir" your_secret_code
## or for file
python crapo.py encrypt ./personal.file your_secret_code

# To encrypt and delete initial Origin file add "erase"
python crapo.py encrypt ./Personnaldirectory/ your_secret_code erase

# -----------------------------------------------------------------------
# To decrypt
# For directory
python crapo.py decrypt ./Personnaldirectory/ your_secret_code
# or for file
python crapo.py decrypt ./personal.file your_secret_code
```

## DEMO HERE

[See DEMO](https://youtu.be/MajlnQmW7vQ)

## Author

- [🐼Sanix-darker](https://github.com/sanix-darker)