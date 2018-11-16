# This is the first implementation of the GUI based emailEncryptor program
# Written and designed by Hayden Riewe
# hrcyber.tech
# github.com/hriewe/

import random
import string

# This class encrypts with a caesar rotation cipher
class caesar():

  # constructor for caesar cipher
  def __init__(self):
    self.specialList = ['!', '?', '.', ',', '@', '#', '$', '%', '&', '*', '(', ')', '+', '=', '-', '/', '\'']

  # Encrypt the users string and return the new one
  def encrypt(self, string):
      self.shift = random.randint(5,100)
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
      self.cipher += str(self.shift)
      return self.cipher

  # Decrypt the string based on the key
  def decrpyt(self, string, key):
      self.shift = int(key)
      self.cipher = ''
      self.string = string[::-1]
      for char in self.string: 
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