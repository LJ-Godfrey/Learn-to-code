# This code rotates each word in the string half the word length
inp = input("Enter a string: ")
out = ''

for letter in inp:
	out = letter + out

print(out)