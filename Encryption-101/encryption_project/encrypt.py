# This file contains various encryption methods, for use in an encryption / decryption program

def caesar(string):
    res = str()
    for letter in string:
        if letter.lower() >= 'a' and letter.lower() <= 'm':
            res += chr(ord(letter) + 13)
        elif letter.lower() >= 'n' and letter.lower() <= 'z':
            res += chr(ord(letter) - 13)
        else:
            res += letter
    return res

def reverse(string):
    res = str()
    for letter in string:
        res = letter + res
    return res

def xor(string, key):
    res = str()
    for letter in string:
        res += chr(ord(letter) ^ key)
    return res

def rotate(string):
    res = str()
    if len(string) % 2 > 0:
        mid = string[len(string)/2 + 1]
        res = string[:mid] + string[mid+1:]
        res = rot_sub(res)
        res = res[:len(res)/2] + mid + res[len(res)/2:]
    else:
        res = rot_sub(string)
    return res

# This function is used in the 'rotate' function
def rot_sub(string):
    res = string
    # pylint: disable=unused-variable
    for letter in range(int(len(string)/2)):
        last = len(res) - 1
        res = res[last] + res[:last]
    return res