# emailEncryptor
A simple program to send encrypted emails and decode encrypted emails.
Currently, it uses a Caesar Cipher to encrypt your message. This is a well known method of
encryption that is not hard to crack if someone really wants to. In the future, better forms
of encryption will be implemented.
Anybody who sees these encrypted messages will see a bunch of giberish, and this will be uncrackable
to most.

## Set up
In order to send mail through gmail, you will have to "Enable less secure apps"
To do this:
1. Navigate to your google account settings
2. In the "Sign in and Security pane", click "Apps with account access"
3. Set the "Allow less secure apps" slider to ON

If you dont have python installed, you can get it [Here](https://www.python.org/downloads/)

Install the needed module with:

`pip3 install yagmail`

Thats it! You can now send mail through emailEncryptor

## How to run the program

Run this command on your command line:

`git clone https://github.com/hriewe/emailEncryptor.git`

CD into the emailEncryptor folder:

`cd emailEncryptor/`

Run the program with:

`python emailEncryptor.py`

If you have multiple different versions of python installed on your machine, you might need to run:

`python3 emailEncryptor.py`

## Notes
This program will ask you for your gmail username and password. These are not stored anywhere, but if
you do not feel safe, do not enter your information.
