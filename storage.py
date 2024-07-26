from Crypto.Cipher import AES # type: ignore
from Crypto.Protocol.KDF import PBKDF2 # type: ignore

def encrypt_private_key(private_key, password):
    salt = b'some_salt'  # salt used to add randomness to the encryption key, making it harder to guess.
    key = PBKDF2(password, salt, dkLen=32)  #Uses the password and the salt to create a strong encryption key.
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce# nonce ensures that even if the same data is encrypted multiple times, the output will be different each time.
    ciphertext, tag = cipher.encrypt_and_digest(private_key)#: Encrypts the private key to produce ciphertext and an authentication tag
    return nonce + ciphertext

def decrypt_private_key(encrypted_private_key, password):
    salt = b'some_salt'
    key = PBKDF2(password, salt, dkLen=32)  #Password-Based Key Derivation Function 2
    nonce = encrypted_private_key[:16]
    ciphertext = encrypted_private_key[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    private_key = cipher.decrypt(ciphertext)
    return private_key


#PBKDF2(Password-Based Key Derivation Function 2)
#to generate secure password storage we use password + salt which gives hash function
#in PBKDF2 we have salt + password +no. of iteration(no. of times it will be hashed)
#also make harder to brute force