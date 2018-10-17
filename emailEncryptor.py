import yagmail
import os
import random
import sys
import string
import getpass

# Encrypt the string and return it
def encrypt(string):
  shift = random.randint(1,25)
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif char == '.' or char == ',':
      cipher = cipher + char
    elif is_number(char):
      cipher = cipher + encryptNumber(char)
    elif char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

  cipher += ' '
  cipher += str(shift)
  return cipher

# If there is a number in the string, it is sent here for a special encoding (WORK IN PROGRESS)
def encryptNumber(char):
  if char == '0':
    return '['
  elif char == '1':
    return '}'
  elif char == '2':
    return '|'
  elif char == '3':
    return '&'
  elif char == '4':
    return '*'
  elif char == '5':
    return '#'
  elif char == '6':
    return '>'
  elif char == '7':
    return '-'
  elif char == '8':
    return '%'
  else:
    return '~'

# Decrypt the string (WORK IN PROGRESS)
def decrpyt(string, key):
  shift = int(key)
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif char == '.' or char == ',':
      cipher = cipher + char
    elif char == '[':
      cipher = cipher + '0'
    elif char == '}':
      cipher = cipher + '1'
    elif char == '|':
      cipher = cipher + '2'
    elif char == '&':
      cipher = cipher + '3'
    elif char == '*':
      cipher = cipher + '4'
    elif char == '#':
      cipher = cipher + '5'
    elif char == '>':
      cipher = cipher + '6'
    elif char == '-':
      cipher = cipher + '7'
    elif char == '%':
      cipher = cipher + '8'
    elif char == '~':
      cipher = cipher + '9'
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

  return cipher

# Determine if a character in the body is actually a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux
    else: 
        _ = os.system('clear') 

# Get encoded message and decrypt it based on key
def decodeMail():
	key = input("Enter the key found at the end of your emailEncryptor message: ")
	content = input("Paste the email contents here: ")
	decodedContent = decrpyt(content, key)
	clear()
	print("\n")
	print(decodedContent)
	print("\n")

	again = input("Decode another message? (yes/no) ")
	if again == 'yes' or again == 'Yes':
		decodeMail()
	else:
		print("Goodybye!")
		sys.exit(0)

# Encrypt a message and send an email
def sendMail():
	usrEmail = input("Great! What is your e-mail address? ")
	usrPass = getpass.getpass(prompt = "What is your password: ")
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

# This is the start of the main function, user determines if they want to encode or decode
print("\nWelcome to emailEncryptor!\n")
print("Writen by Hayden Riewe  \n")
while True:
	decision = input("Would you like to send, or decode mail? ")

	if decision == "send" or decision == "Send":
		sendMail()
		break

	if decision == "decode" or decision == "Decode":
		decodeMail()
		break
