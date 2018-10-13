import yagmail
import os
import random
import sys
import string

def encrypt(string):
  shift = random.randint(1,26)
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif char == '.' or char == ',':
      cipher = cipher + char
    elif char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

  cipher += ' '
  cipher += str(shift)
  return cipher

def decrpyt(string, key):
  shift = int(key)
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif char == '.' or char == ',':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

  return cipher

def decodeMail():
	key = input("Enter the key found at the end of your emailEncryptor message: ")
	content = input("Paste the email contents here: ")
	decodedContent = decrpyt(content, key)
	print("\n")
	print(decodedContent)
	print("\n")

	again = input("Decode another message? (yes/no) ")
	if again == 'yes' or again == 'Yes':
		decodeMail()
	else:
		print("Goodybye!")
		sys.exit(0)

def sendMail():
	usrEmail = input("Great! What is your e-mail address? ")
	usrPass = input("What is your password? ")
	yag = yagmail.SMTP(usrEmail, usrPass)
	content = input("Please enter the body of the e-mail: ")
	cryptContent = encrypt(content)

	sendTo = input("Who do you want to send this to? ")
	subject = input("Subject line? ")

	yag.send(sendTo, subject, cryptContent)

	print("Message sent successfully!!!")
	again = input("Send another message? (yes/no) ")
	if again == 'yes' or again == 'Yes':
		sendMail()
	else:
		print("Goodybye!")
		sys.exit(0)


print("\nWelcome to emailEncryptor!\n")
print(" Writen by Hayden Riewe  \n")
decision = input("Would you like to send, or decode mail? ")

if decision == "send":
	sendMail()

if decision == "decode":
	decodeMail()
