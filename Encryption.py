from cryptography.fernet import Fernet
message = input("Enter something secret:")

def encryptMessage(key, message):
    # Maakt een Fernet-object aan dat met deze sleutel werkt.
    f = Fernet(key)
    return f.encrypt(message.encode())

def decryptMessage(key, token):
    f = Fernet(key)
    return f.decrypt(token).decode()

key = Fernet.generate_key()
token = encryptMessage(key, message)
print(f"Encrypted message: {token.decode()}")
print(f"Decrypted message: {decryptMessage(key, token)}")

