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
  layout = [
          [sg.Text('Please enter your information', auto_size_text=False, justification='left', font=('Helvetica', 20))],
          [sg.Text('Your E-Mail address', size=(20, 1)), sg.InputText()],
          [sg.Text('Your Password', size=(20, 1)), sg.InputText(password_char='*')],
          [sg.Text('Who to send this to?', size=(20,1)), sg.InputText()],
          [sg.Text('Subject (not encrypted)', size=(20,1)), sg.InputText()],
          [sg.Text('The body of your email', size=(20, 1)), sg.Multiline(size=(45,5), autoscroll=True, background_color='grey')],
          [sg.Text('Please choose a cipher', size=(20,1)), sg.Radio('Caesar', 'ciphers', default=True), sg.Radio('Hidden-in-Image', 'ciphers')],
          [sg.ReadButton('Send',font=('Helvetica',15), auto_size_button=True, bind_return_key=True), 
          sg.Button('Home',font=('Helvetica',15), auto_size_button=True), 
          sg.ReadButton('Exit',font=('Helvetica',15), auto_size_button=True)]
         ]
  layout2 = [
            [sg.Text("Please choose a cipher", justification='center', auto_size_text = False)],
            [sg.Radio('Caesar', 'ciphers', default=True), sg.Radio('Steg', 'ciphers')],
            [sg.Button('Next'), sg.Button('Home'), sg.Button('Exit')]
            ]
  layout3 = [
            [sg.Text('Welcome to the Stegonagraphy encryptor', justification='center', auto_size_text=True)],
            [sg.Text('Your E-Mail address', size=(20, 1)), sg.InputText()],
            [sg.Text('Your Password', size=(20, 1)), sg.InputText(password_char='*')],
            [sg.Text('Who to send this to?', size=(20,1)), sg.InputText()],
            [sg.Text('Subject (not encrypted)', size=(20,1)), sg.InputText()],
            [sg.Text('The body of your email', size=(20, 1)), sg.Multiline(size=(45,5), autoscroll=True, background_color='grey')],
            [sg.Text('Your \"before\" Image File-Name'), sg.InputText(), sg.FileBrowse()],
            [sg.Button('Send'), sg.Button('Home'), sg.Button('Exit')]]
  # Show the window to the user
  window = sg.Window('emailEncryptor').Layout(layout)
  window2 = sg.Window('Cipher Selector').Layout(layout2)
  window3 = sg.Window('Stegonagraphy encryptor').Layout(layout3)
  # Send the mail
  while True:
    button, values = window2.Read()
    if button == 'Next':
      if values[0] == True:
        # Determine if Caesar radio button is selected
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
      elif values[1] == True:
        window2.Hide()
        while True:
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
  layout = [
      [sg.Text('Paste the contents of the emailEncryptor message here'), sg.InputText(do_not_clear=True, size=(15,2))],
      [sg.Text('If steg image, add here:'), sg.InputText(do_not_clear=True), sg.FileBrowse()],
      [sg.Text('Please choose a cipher', size=(20,1)), sg.Radio('Caesar', "cipher", default=True), sg.Radio('Stegonagraphy', 'cipher')],
      [sg.ReadButton('Decode',font=('Helvetica',15), auto_size_button=True, bind_return_key=True), 
      sg.Button('Home',font=('Helvetica',15), auto_size_button=True), sg.Exit(font=('Helvetica',15), auto_size_button=True)]
      ]
  # Show the window to the user
  window = sg.Window('emailEncryptor').Layout(layout)

  # Determine what to do with the data just given to us
  while True:
    button, values = window.Read()
    if button == 'Decode':
      # Determine if Caesar radio button is selected
      if values[2] == True:
        decodedContent = caesar.decrpyt(values[0])
        window.Hide()
        displayMessage(decodedContent)
      elif values[3] == True:
        realSteg.decrypt(values[1])
        file = open('hidden_file.txt', 'r')
        decodedMessage = file.read()
        os.remove('hidden_file.txt')
        window.Hide()
        displayMessage(decodedMessage)

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

# Function call to create instance of classes and to start the program
realSteg = realSteg()
caesar = caesar()
home()
