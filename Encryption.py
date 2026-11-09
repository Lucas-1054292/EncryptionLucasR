from cryptography.fernet import Fernet
# Maakt een willekeurige, unieke sleutel aan.
key = Fernet.generate_key()
# Maakt een Fernet-object aan dat met deze sleutel werkt.
f = Fernet(key)
message = input("Enter something secret:")
# Versleutelt het bericht.
token = f.encrypt(message.encode())
print(token)
# Ontsleutelt de token weer met dezelfde sleutel.
print(f.decrypt(token))