def encrypt_message(message, key):
    ret = ""
    for i in message:
        if i == " ":
            ret = ret + " "
        else:
            print((ord(i) + 1 - 97) % 26)
            ret = ret + chr((ord(i) + 1 - 97) % 26)
    return ret

s = "abcde"
print((543 - (543 % 100)) / 100)