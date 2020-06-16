SECRET_KEY = 12


def crypt(password):
    return ''.join([chr(ord(c) + SECRET_KEY) for c in password])


def decrypt(password):
    return ''.join([chr(ord(c) - SECRET_KEY) for c in password])


print(crypt('Dima'))
print(decrypt('Ejnb'))
