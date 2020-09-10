# Pennywise cypher
# 1300100920

inp = input("Message: ")
out = str()

for letter in inp:
    if letter.lower() >= 'a' and letter.lower() <= 'm':
        out = out + chr(ord(letter) + 13)
    elif letter.lower() >= 'n' and letter.lower() <= 'z':
        out = out + chr(ord(letter) - 13)
    else:
        out = out + letter

print(out)
