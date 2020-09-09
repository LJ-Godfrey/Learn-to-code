# This code demonstrates a caesar cypher

inp = input("Enter your string: ").lower()
out = ''

for letter in inp:
	if letter >= 'a' and letter <= 'm':
		out += chr(ord(letter) + 13)
	elif letter >= 'n' and letter <= 'z':
		out += chr(ord(letter) - 13)
	else:
		out += letter

print(out)