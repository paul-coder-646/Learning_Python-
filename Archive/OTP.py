import os


def encrypt(filename):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename + ".key", "wb") as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)


def decrypt(filename, key):
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open("d_" + filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)


def reverse(filename):
    file = open(filename, "r").read()
    reversedd = file[::-1]
    reversedoutput = ''.join(reversedd)
    with open("r_" + filename, "w") as reversed_out:
        reversed_out.write(reversedoutput)


if __name__ == '__main__':
    reverse("key.txt")
    filename1 = 'encrypted.txt'
    filename2 = 'r_key.txt'
    decrypt(filename1, filename2)
