import time
from keymanage import generate_rsa_keys
from storage import encrypt_private_key, decrypt_private_key
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def main():
    print("===== Secure Key Management =====\n")

    #step 1: User enters data
    user_data = input("Enter the data you want to encrypt: ")
    print("[1]Original Data:", user_data)
    print()

    # step 2: Generate RSA keys
    print("[2] Generating RSA key pair...")
    private_key, public_key = generate_rsa_keys()#function call (keymanage.py)
    print("RSA key pair generated successfully\n")
    time.sleep(1)

    # Password for encrypting the private key , value can be changed
    password = b'mypassword'

    # Step 3: Encrypt and store the private key
    print("[3] Encrypting the private key...")
    encrypted_private_key = encrypt_private_key(private_key, password) #function called (storage.py)
    print("Encrypted Private Key (First 10 chars):", encrypted_private_key[:10], "...") # can remove
    print("Private key encrypted and stored successfully\n")
    time.sleep(1)

    # Step 4: Encrypt the user data using the public key (RSA)
    print("[4] Encrypting user data using the public key...")
    rsa_public_key = RSA.import_key(public_key)  #imports the RSA public key from the byte string public_key 
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)  #PKCS1_OAEP= encryption scheme use RSA to encrypt data using Optimal Asymmetric Encryption Padding (OAEP).
    encrypted_data = cipher_rsa.encrypt(user_data.encode())#his line encrypts the user data  after encoding it into bytes 
    print("Encrypted Data (First 10 chars):", encrypted_data[:10], "...") #can remove
    print("Data encrypted successfully\n")
    time.sleep(1)

    # Step 5: Decrypt the private key
    print("[5] Decrypting the private key...")
    decrypted_private_key = decrypt_private_key(encrypted_private_key, password)#function call (storage.py)
    print("Decrypted Private Key (First 10 chars):", decrypted_private_key.decode()[:10], "...")#can remove
    print("Private key decrypted successfully\n")
    time.sleep(1)

    # Step 6: Decrypt the user data using the private key (RSA)
    print("[6] Decrypting the user data using the private key...")
    rsa_private_key = RSA.import_key(decrypted_private_key) #convert from byte string representation into an RSA key objec
    cipher_rsa = PKCS1_OAEP.new(rsa_private_key) #creates new cipher object for RSA encryption using OAEP padding scheme
    decrypted_data = cipher_rsa.decrypt(encrypted_data).decode()
    print("Decrypted Data:", decrypted_data)
    print("Data decrypted successfully\n")


if __name__ == "__main__":
    main()



#This function imports an RSA public key from a byte string (public_key).
#Use: It allows you to convert the byte representation of a public key into a format that Python's cryptography library 
# (Crypto.PublicKey.RSA) can understand and use for encryption operations.
