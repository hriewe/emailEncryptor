# This is the second implementation of the GUI based emailEncryptor program
# Written and designed by Hayden Riewe
# hrcyber.tech
# github.com/hriewe/
from steg import common, steg_img
import yagmail
import sys
import getpass
import random
import string

# This class encrypts with a caesar rotation cipher
class caesar():

  # constructor for caesar cipher
  def __init__(self):
    self.specialList = ['!', '?', '.', ',', '@', '#', '$', '%', '&', '*', '(', ')', '+', '=', '-', '/', '\'', '^',
                        '_', '[', ']', '{', '}', '|', '\"', '<', '>']

  # Encrypt the users string and return the new one
  def encrypt(self, string):
      self.shift = random.randint(10,99)
      self.cipher = ''
      for char in string: 
          if char == ' ':
              self.cipher = self.cipher + char
          elif char in self.specialList:
              self.cipher = self.cipher + char
          elif char == '\n':
              self.cipher = self.cipher + 'ç'
          elif self.is_number(char):
              self.cipher = self.cipher + self.encryptNumber(char)
          elif char.isupper():
              self.cipher = self.cipher + chr((ord(char) + self.shift - 65) % 26 + 65)
          else:
              self.cipher = self.cipher + chr((ord(char) + self.shift - 97) % 26 + 97)

      self.cipher = self.cipher[::-1]
      self.cipher += ' '
      self.charShift = str(self.shift)
      self.encodedKey = ''
      for char in self.charShift:
        self.encodedKey = self.encodedKey + self.encryptNumber(char)
      self.cipher += self.encodedKey
      return self.cipher

  # Decrypt the string based on the key
  def decrpyt(self, string):
      self.decodedKey = string[-2:]
      self.message = string[:-3]
      self.shift = self.decryptNumber(self.decodedKey)
      self.cipher = ''
      self.message = self.message[::-1]
      for char in self.message:
          if char == ' ':
              self.cipher = self.cipher + char
          elif char in self.specialList:
              self.cipher = self.cipher + char
          elif char == 'ç':
              self.cipher = self.cipher + '\n'
          elif char == 'ß':
              self.cipher = self.cipher + '0'
          elif char == 'š':
              self.cipher = self.cipher + '1'
          elif char == 'œ':
              self.cipher = self.cipher + '2'
          elif char == 'ø':
              self.cipher = self.cipher + '3'
          elif char == 'ł':
              self.cipher = self.cipher + '4'
          elif char == 'ñ':
              self.cipher = self.cipher + '5'
          elif char == 'ÿ':
              self.cipher = self.cipher + '6'
          elif char == 'ę':
              self.cipher = self.cipher + '7'
          elif char == 'å':
              self.cipher = self.cipher + '8'
          elif char == 'ž':
              self.cipher = self.cipher + '9'
          elif  char.isupper():
              self.cipher = self.cipher + chr((ord(char) - self.shift - 65) % 26 + 65)
          else:
              self.cipher = self.cipher + chr((ord(char) - self.shift - 97) % 26 + 97)
      return self.cipher

  # Determine if a char is a number or not
  def is_number(self, s):
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

  # This funciton will encrypt numbers with a special character
  def encryptNumber(self, char):
      if char == '0':
          return 'ß'
      elif char == '1':
          return 'š'
      elif char == '2':
          return 'œ'
      elif char == '3':
          return 'ø'
      elif char == '4':
          return 'ł'
      elif char == '5':
          return 'ñ'
      elif char == '6':
          return 'ÿ'
      elif char == '7':
          return 'ę'
      elif char == '8':
          return 'å'
      else:
          return 'ž'

  # This is used for getting the key out of the encrypted message
  def decryptNumber(self, string):
      self.key = ''
      for char in string:
        if char == 'ß':
            self.key = self.key + '0'
        elif char == 'š':
            self.key = self.key + '1'
        elif char == 'œ':
            self.key = self.key + '2'
        elif char == 'ø':
            self.key = self.key + '3'
        elif char == 'ł':
            self.key = self.key + '4'
        elif char == 'ñ':
            self.key = self.key + '5'
        elif char == 'ÿ':
            self.key = self.key + '6'
        elif char == 'ę':
            self.key = self.key + '7'
        elif char == 'å':
            self.key = self.key + '8'
        elif char == 'ž':
            self.key = self.key + '9'
      return int(self.key)

  # Get encoded message and decrypt it based on key (Command Line)
  def CLIdecodeMail(self):
    key = input("Enter the key found at the end of your emailEncryptor message: ")
    content = input("Paste the email contents here: ")
    decodedContent = self.decrpyt(content, key)
    print("\n")
    print(decodedContent)
    print("\n")

    again = input("Decode another message? (yes/no) ")
    if again == 'yes' or again == 'Yes':
      self.CLIdecodeMail()
    else:
      print("Goodybye!")
      sys.exit(0)

  # Encrypt a message and send an email (Command Line)
  def CLIsendMail(self):
    usrEmail = input("Great! What is your e-mail address? ")
    usrPass = getpass.getpass(prompt = "What is your password: ")
    yag = yagmail.SMTP(usrEmail, usrPass)
    content = input("Please enter the body of the e-mail: ")
    cryptContent = self.encrypt(content)

    sendTo = input("Who do you want to send this to? ")
    subject = input("Subject line? ")

    yag.send(sendTo, subject, cryptContent)

    print("Message sent successfully!!!")
    again = input("Send another message? (yes/no) ")
    if again == 'yes' or again == 'Yes':
      self.CLIsendMail()
    else:
      print("Goodybye!")
      sys.exit(0)

class realSteg():


  def __init__(self):
    pass

  def encrypt(self, message, image):
    self.s = steg_img.IMG(payload_path=message, image_path=image)
    self.s.hide()
  def decrypt(self, image):
    self.s_prime = steg_img.IMG(image_path=image)
    self.s_prime.extract()