# This is the second implementation of the GUI based emailEncryptor program
# Written and designed by Hayden Riewe
# github.com/hriewe/emailEncryptor
# hrcyber.tech

import PySimpleGUI as sg
import yagmail
import os
import sys
import string
from ciphers import caesar, realSteg

#What the user sees when they choose to send mail
def sendMailButton():

  # Design the layout of the interface the user sees when sending mail
  SelectorLayout = [
            [sg.Text("Please choose a cipher", justification='center', auto_size_text = False)],
            [sg.Radio('Caesar', 'ciphers', default=True), sg.Radio('Steg', 'ciphers')],
            [sg.Button('Next'), sg.Button('Home'), sg.Button('Exit')]
            ]

  CaesarLayout = [
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

  StegLayout = [
            [sg.Text('Welcome to the Stegonagraphy encryptor', justification='center', auto_size_text=True)],
            [sg.Text('Your E-Mail address', size=(20, 1)), sg.InputText()],
            [sg.Text('Your Password', size=(20, 1)), sg.InputText(password_char='*')],
            [sg.Text('Who to send this to?', size=(20,1)), sg.InputText()],
            [sg.Text('Subject (not encrypted)', size=(20,1)), sg.InputText()],
            [sg.Text('The body of your email', size=(20, 1)), sg.Multiline(size=(45,5), autoscroll=True, background_color='grey')],
            [sg.Text('Select image', size=(20,1)), sg.InputText(size=(35,1)), sg.FileBrowse()],
            [sg.Button('Send'), sg.Button('Home'), sg.Button('Exit')]]
  # Show the window to the user
  window = sg.Window('emailEncryptor').Layout(CaesarLayout)
  window2 = sg.Window('Cipher Selector').Layout(SelectorLayout)
  window3 = sg.Window('Stegonagraphy Encryptor').Layout(StegLayout)
  # Send the mail
  while True:
    button, values = window2.Read()
    if button == 'Next':
      if values[0] == True: #Caesar has been selected
        window2.Hide()
        button2, values2 = window.Read()
        if button2 == 'Send':
          encryptedContent = caesar.encrypt(values2[4])
          yag = yagmail.SMTP(values2[0], values2[1])
          yag.send(values2[2], values2[3], encryptedContent)
          sg.Popup('Email sent succesfully!')
        if button2 == 'Home':
          window.Hide()
          home()
        else:
          sys.exit()
      elif values[1] == True: #Steg has been selected
        window2.Hide()
        button3, values3 = window3.Read()
        if button3 == 'Send':
          if values3[4] == '':
            sg.Popup("Please enter a message!")
            break
          file = open('temp.txt', 'w')
          file.write(values3[4])
          file.close()
          encryptedImage = realSteg.encrypt('temp.txt', values3[5])
          os.remove('temp.txt')
          yag = yagmail.SMTP(values3[0], values3[1])
          yag.send(values3[2], values3[3], 'new.png')
          sg.Popup('Email sent succesfully!')
          os.remove('new.png')
        elif button3 == 'Home':
            window3.Hide()
            home()
        else:
            sys.exit()

    elif button == 'Home':
      window2.Hide()
      home()
    else:
      sys.exit()


#What thet user sees when they choose to decode mail
def decodeMailButton():

  # Design the layout of the interface when the user is entering decode info
  DecryptSelector = [
            [sg.Text("Please choose a cipher", justification='center', auto_size_text = False)],
            [sg.Radio('Caesar', 'ciphers', default=True), sg.Radio('Steg', 'ciphers')],
            [sg.Button('Next', bind_return_key=True), sg.Button('Home'), sg.Button('Exit')]
            ]

  CaesarLayout = [
      [sg.Text('Paste the contents of the emailEncryptor message here'), sg.InputText(do_not_clear=True, size=(15,2))],
      [sg.ReadButton('Decode',font=('Helvetica',15), auto_size_button=True, bind_return_key=True), 
      sg.Button('Home',font=('Helvetica',15), auto_size_button=True), sg.Exit(font=('Helvetica',15), auto_size_button=True)]
      ]

  StegLayout = [
          [sg.Text('Welcome to the Stegonagraphy decryptor', justification='center')],
          [sg.Text('Select the image you recieved'), sg.InputText(), sg.FileBrowse()],
          [sg.Button('Decode'), sg.Button('Home'), sg.Button('Exit')]
          ]
  # Show the window to the user
  window = sg.Window('emailEncryptor').Layout(DecryptSelector)
  window2 = sg.Window('emailEncryptor').Layout(CaesarLayout)
  window3 = sg.Window('emailEncryptor').Layout(StegLayout)

  # Determine what to do with the data just given to us
  while True:
    button, values = window.Read()
    if button == 'Next':
      # Determine if Caesar radio button is selected
      if values[0] == True:
        window.Hide()
        button2, values2 = window2.Read()
        if button2 == 'Decode':
          decodedContent = caesar.decrpyt(values2[0])
          window2.Hide()
          displayMessage(decodedContent)
        elif button2 == 'Home':
          window2.Hide()
          home()
        else:
          sys.exit()
      if values[1] == True:
        window.Hide()
        button3, values3 = window3.Read()
        if button3 == 'Decode':
          realSteg.decrypt(values3[0])
          file = open('hidden_file.txt', 'r')
          decodedMessage = file.read()
          os.remove('hidden_file.txt')
          window3.Hide()
          displayMessage(decodedMessage)
        elif button3 == 'Home':
          window3.Hide()
          home()
        else:
          sys.exit()
    elif button == 'Home':
      window.Hide()
      home()
    else:
      sys.exit()

# This function will display the decoded message to the user after decrypting
def displayMessage(string):
  # Layout design
  layout = [
        [sg.Multiline(string, size=(55,20), auto_size_text=True)],
        [sg.Text(''), sg.Button('Back', auto_size_button=True)]]
  # Show window to the user
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
           [sg.Text('',size=(14,1)), sg.Button('Send', font = ('Helvetica',15), auto_size_button=True), 
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

# Function call to create instance of classes and to start the program
realSteg = realSteg()
caesar = caesar()
home()
