#This code encrypts the input with an xor
# NOTE: This code does not work and won't run
key = input("Enter your key: ")
inp = input("Enter your message: ")

print(int(inp,base=8) ^ int(key,base=8))