#This code encrypts the input with an xor
key = input("Enter your key: ")
inp = input("Enter your message: ")

print(int(inp,base=8) ^ int(key,base=8))