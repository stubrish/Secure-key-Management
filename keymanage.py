from Crypto.PublicKey import RSA # type: ignore

def generate_rsa_keys():
    key = RSA.generate(2048)
#RSA.generate(2048): Calls the generate method of the RSA class to create a new RSA key pair with a length of 2048 bits. 
# This size is commonly used because it provides a good balance between security and performance.
    private_key = key.export_key()#This method converts the private key into a byte string, which can then be saved or transmitted over a network.
    
    public_key = key.publickey().export_key()
    #This method extracts the public key from the RSA key pair.
    return private_key, public_key



#RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest widely used for secure data transmission