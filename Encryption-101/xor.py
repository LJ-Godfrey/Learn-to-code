# This code takes an input string and encrypts it with a given value

inp = input("Enter a string: ").lower()
num = int(input("Enter a number: "))
enc = ''

for letter in inp:
	enc += chr(ord(letter) ^ num)

print(enc)