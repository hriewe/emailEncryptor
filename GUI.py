# This is the second implementation of the GUI based emailEncryptor program
# Written and designed by Hayden Riewe
# github.com/hriewe/emailEncryptor
# hrcyber.tech

import PySimpleGUI as sg
import yagmail
import os
import sys
import string
from ciphers import caesar

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
          [sg.Text('Please choose a cipher', size=(20,1)), sg.Radio('Caesar', "cipher", default=True)],
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
      if values[5] == True:
        encryptedContent = caesar.encrypt(values[4])
        yag = yagmail.SMTP(values[0], values[1])
        yag.send(values[2], values[3], encryptedContent)
        sg.Popup('Email sent succesfully!')
    elif button == 'Home':
      window.Hide()
      home()
    else:
      sys.exit()

#What thet user sees when they choose to decode mail
def decodeMailButton():

  # Design the layout of the interface when the user is entering decode info
  layout = [
      [sg.Text('Paste the contents of the emailEncryptor message here'), sg.InputText(do_not_clear=True, size=(15,2))],
      [sg.Text('Please choose a cipher', size=(20,1)), sg.Radio('Caesar', "cipher", default=True)],
      [sg.ReadButton('Decode',font=('Helvetica',15), auto_size_button=True, bind_return_key=True), 
      sg.Button('Home',font=('Helvetica',15), auto_size_button=True), sg.Exit(font=('Helvetica',15), auto_size_button=True)]
      ]
  # Show the window to the user
  window = sg.Window('emailEncryptor').Layout(layout)

  # Determine what to do with the data just given to us
  while True:
    button, values = window.Read()
    if button == 'Decode':
      if values[1] == True:
        decodedContent = caesar.decrpyt(values[0])
        window.Hide()
        displayMessage(decodedContent)
    elif button == 'Home':
      window.Hide()
      home()
    else:
      sys.exit()

def displayMessage(string):
  layout = [
        [sg.Multiline(string, size=(55,20), auto_size_text=True)],
        [sg.Text(''), sg.Button('Back', auto_size_button=True)]]
  window = sg.Window('Decoded message').Layout(layout)
  while True:
    button, values = window.Read()
    if button == 'Back':
      window.Hide()
      decodeMailButton()
    else:
      break

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
           [sg.Text('',size=(11,1)), sg.Button('Send', font = ('Helvetica',15), auto_size_button=True), 
           sg.Button('Decode', font=('Helvetica',15), auto_size_button=True), sg.Quit(font=('Helvetica',15),auto_size_button=True)]]

  # Show the Window to the user
  window = sg.Window('Welcome to emailEncryptor!').Layout(layout)

  # Event loop. Read buttons, make callbacks
  while True:
    # Read the Window
    button, value = window.Read()
    # Take appropriate action based on button
    if button == 'Send':
          window.Hide()
          sendMailButton()
    elif button == 'Decode':
          window.Hide()
          decodeMailButton()
    elif button =='Quit' or button is None:
      sys.exit()
      break

# Function call to start the program
caesar = caesar()
home()
