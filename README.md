# emailEncryptor
A simple program to send encrypted emails and decode encrypted emails.
Currently, it uses a Caesar Cipher to encrypt your message. This is a well known method of
encryption that is not hard to crack if someone really knows how. In the future, better forms
of encryption will be implemented.
Anybody who sees these encrypted messages will see a bunch of giberish, and this will be uncrackable
to most.

## Set up
If you are trying to send encrypted messages, I do not suggest using your primary email account.
You can, and it will work, but you will need to alter some settings for the program to work.
I suggest creating a new Gmail account with a VERY strong password, and using that for sending and
recieving messages with emailEncryptor.

In order to send mail through Gmail, you will have to "enable less secure apps"
To do this:
1. Navigate to your Google account settings
2. In the "Sign in and Security pane", click "Apps with account access"
3. Set the "Allow less secure apps" slider to ON

Also, the program will not work if you have "2 step verification" enabled on your account

NOTE: Gmail WILL send you a critical security alert email. You can ignore this.

You will need python.
If you dont have python installed, you can get it [Here](https://www.python.org/downloads/)

Install the needed module with:

`pip3 install yagmail`

Thats it! You can now send mail through emailEncryptor

## How to run the program

Run this command on your command line to install the program:

`git clone https://github.com/hriewe/emailEncryptor.git`

CD into the emailEncryptor folder:

`cd emailEncryptor/`

Run the program with:

`python emailEncryptor.py`

If you have multiple different versions of python installed on your machine, you might need to run:

`python3 emailEncryptor.py`

And if you're like me and have multiple different versions of Python 3 installed, you may have to include
your specific version number when you run the program. For me, I have yagmail installed on Python 3.6 so I would run:

`python3.6 emailEncryptor.py`

## Notes
* This program is intended to be used by two people to send and decode encrypted messages. When using the program, you can
send mail to anybody without them having to change any setting in their email accounts, but they will not be able to decode
the message without my program. Spread the word and try it out with your friends! Even if you have nothing to hide ;)

* This program will ask you for your gmail username and password. These are not stored anywhere, but if
you do not feel safe, do not enter your information. (There is no practicle way around this, as yagmail needs to be
able to access your account in order to send mail for you)

* I am currently working on a version which uses a GUI for input, and also the hashlib library for extra security

* Using my program? Let me know!! Send an encrypted email to hriewe13@gmail.com and I will get back to you! 
