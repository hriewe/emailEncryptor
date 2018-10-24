# This is the first implementation of the GUI based emailEncryptor program
# Written and designed by Hayden Riewe
# hrcyber.tech
# github.com/hriewe/

import PySimpleGUI as sg
import yagmail
import os
import random
import sys
import string
import getpass

# For windows
# sg.ChangeLookAndFeel('dark')

# This funciton will encrypt numbers with a special character
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

# Determine if a char is a number or not
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

# Encrypt the users string and return the new one
def encrypt(string):
  shift = random.randint(5,25)
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif char == '.' or char == ',':
      cipher = cipher + char
    elif char == '\n':
      cipher = cipher + '$'
    elif is_number(char):
      cipher = cipher + encryptNumber(char)
    elif char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

  cipher = cipher[::-1]
  cipher += ' '
  cipher += str(shift)
  return cipher

# Decrypt the string based on the key
def decrpyt(string, key):
  shift = int(key)
  cipher = ''
  string = string[::-1]
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif char == '.' or char == ',':
      cipher = cipher + char
    elif char == '$':
      cipher = cipher + '\n'
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

#What the user sees when they choose to send mail
def sendMailButton():
  # Design the layout of the interface the user sees when sending mail
	layout = [
          [sg.Text('Please enter your information', auto_size_text=False, justification='left', font=('Helvetica', 20))],
          [sg.Text('Your E-Mail address', size=(20, 1)), sg.InputText()],
          [sg.Text('Your Password', size=(20, 1)), sg.InputText(password_char='*')],
          [sg.Text('Who to send this to?', size=(20,1)), sg.InputText()],
          [sg.Text('Subject (not encrypted)', size=(20,1)), sg.InputText()],
          [sg.Text('The body of your email', size=(20, 1)), sg.Multiline(size=(45,5), autoscroll=True, background_color='grey')],
          [sg.ReadButton('Send',font=('Helvetica',15), auto_size_button=True, bind_return_key=True), 
          sg.Button('Home',font=('Helvetica',15), auto_size_button=True), 
          sg.ReadButton('Exit',font=('Helvetica',15), auto_size_button=True)]
         ]
  # Show the window to the user
	window = sg.Window('emailEncryptor').Layout(layout)

  # Send the mail
	while True:
		button, values = window.Read()
		if button == 'Send':
			encryptedContent = encrypt(values[4])
			yag = yagmail.SMTP(values[0], values[1])
			yag.send(values[2], values[3], encryptedContent)
			sg.Popup('Email sent succesfully!')
		elif button == 'Home':
			home()
		else:
			sys.exit()

#What thet user sees when they choose to decode mail
def decodeMailButton():

  # Design the layout of the interface when the user is entering decode info
	layout = [
			[sg.Text('Enter the key found at the end of your emailEncryptor message'), sg.InputText(do_not_clear=True, size=(10,1))],
			[sg.Text('Paste the contents of the emailEncryptor message here'), sg.InputText(do_not_clear=True, size=(15,2))],
			[sg.ReadButton('Decode',font=('Helvetica',15), auto_size_button=True, bind_return_key=True), 
			sg.Button('Home',font=('Helvetica',15), auto_size_button=True), sg.Exit(font=('Helvetica',15), auto_size_button=True)]
			]
  # Show the window to the user
	window = sg.Window('emailEncryptor').Layout(layout)

  # Determine what to do with the data just given to us
	while True:
		button, values = window.Read()
		if button == 'Decode':
			decodedContent = decrpyt(values[1], values[0])
			layout2 = [
			[sg.Multiline(decodedContent, size=(55,20), auto_size_text=True)],
			[sg.Text('', size=(30,1)), sg.Button('Back')]]
			window2 = sg.Window('Decoded message').Layout(layout2)
			button2 = window2.Read()
		elif button == 'Home':
			home()
		else:
			sys.exit()

# Initial screen and home location
def home():

  # Set custom, system wide options to the entire interface
	sg.SetOptions(scrollbar_color=None,
           button_color=('white','#475841'),
           font=('Helvetica', 20),     
           input_elements_background_color='#F7F3EC') 

  # Design the layout of the home window
	layout = [[sg.Text('Welcome to emailEncryptor', auto_size_text=False, justification='center', font=('Helvetica', 20))],
			  [sg.Text('')],
			  [sg.Text('Written by Hayden Riewe', auto_size_text=False, justification='center', font=('Helvetica', 20))],
			  [sg.Text('')],
	          [sg.Text('',size=(12,1)), sg.Button('Send', font = ('Helvetica',15), auto_size_button=True), 
	          sg.Button('Decode', font=('Helvetica',15), auto_size_button=True), sg.Quit(font=('Helvetica',15),auto_size_button=True)]]

	# Show the Window to the user
	window = sg.Window('Welcome to emailEncryptor!').Layout(layout)

	# Event loop. Read buttons, make callbacks
	while True:
	  # Read the Window
	  button, value = window.Read()
	  # Take appropriate action based on button
	  if button == 'Send':
	        sendMailButton()
	        window.Hide()
	  elif button == 'Decode':
	        decodeMailButton()
	  elif button =='Quit' or button is None:
	    break

# Function call to start the program
home()