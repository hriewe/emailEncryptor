from ciphers import caesar

caesar = caesar()
# This is the start of the main function, user determines if they want to encode or decode
print("\nWelcome to emailEncryptor!\n")
print("Writen by Hayden Riewe  \n")
while True:
	decision = input("Would you like to send, or decode mail? ")

	if decision == "send" or decision == "Send":
		caesar.CLIsendMail()
		break

	elif decision == "decode" or decision == "Decode":
		caesar.CLIdecodeMail()
		break