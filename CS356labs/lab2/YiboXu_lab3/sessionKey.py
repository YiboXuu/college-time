from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
import random
import base64
import hashlib

hash = "SHA-256"
class AESCipher(object):

    # initialize the class instance and creating a key from user's password
    def __init__(self, passPhrase): 
        self.bs = AES.block_size
        print ("block size", self.bs)
        # get a 256 bit key by hashing your password
        self.key = hashlib.sha256(passPhrase.encode()).digest()
        print ("256 bit key derived from password:\n", self.key)
        print ()

    # method to perform AES encryption
    def encrypt(self, plainText):
        # the plaintext length must be a multiple of blocksize
        # Pad the data if necessary
        padded = self._pad(plainText)
        # Each time we encrypt we will need a random initialization vector
        iv = Random.new().read(AES.block_size)
        # Instantiate a cipher object from the AES library
        # Give it the key, set it to cipher-block-chaining mode, and
        # give it the initialization vector
        cipherObject = AES.new(self.key, AES.MODE_CBC, iv)
        # Encrypt the data/padding after converting to byte array
        encrypted = cipherObject.encrypt(padded.encode('utf-8'))
        # concatenate the iv and the ciphertext and convert to base64                                 
        encoded = base64.b64encode(iv + encrypted)
        return encoded

    # method to perform AES decryption
    def decrypt(self, cipherText):
        # decode the base64 string which contains the IV and ciphertext
        encrypted = base64.b64decode(cipherText) 
        # strip off the initialization vector
        iv = encrypted[:AES.block_size]
        # instantiate an AES cipher object with same parameters as before
        cipherObject = AES.new(self.key, AES.MODE_CBC, iv)
        # decrypt the string, strip off the padding and return the plaintext
        return self._unpad(cipherObject.decrypt(encrypted[AES.block_size:]))

    # method to pad a string to an even multiple of block size
    # the pad character is a hex digit indicating the length of the padding
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    # method to strip the padding
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
    
def newkeys(keysize):
   random_generator = Random.new().read
   key = RSA.generate(keysize, random_generator)
   private, public = key, key.publickey()
   return public, private

def importKey(externKey):
   return RSA.importKey(externKey)

def getpublickey(priv_key):
   return priv_key.publickey()

def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

def sign(message, priv_key, hashAlg = "SHA-256"):
   global hash
   hash = hashAlg
   signer = PKCS1_v1_5.new(priv_key)
   
   if (hash == "SHA-512"):
      digest = SHA512.new()
   elif (hash == "SHA-384"):
      digest = SHA384.new()
   elif (hash == "SHA-256"):
      digest = SHA256.new()
   elif (hash == "SHA-1"):
      digest = SHA.new()
   else:
      digest = MD5.new()        
   digest.update(message)
   return signer.sign(digest)

def verify(message, signature, pub_key):
   signer = PKCS1_v1_5.new(pub_key)
   if (hash == "SHA-512"):
      digest = SHA512.new()
   elif (hash == "SHA-384"):
      digest = SHA384.new()
   elif (hash == "SHA-256"):
      digest = SHA256.new()
   elif (hash == "SHA-1"):
      digest = SHA.new()
   else:
      digest = MD5.new()
   digest.update(message)
   return signer.verify(digest, signature)

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

#
#    The rest is up to you....  make sure to print out appropriate values as necessary
#
#### Generate keypairs for Bob and Alice
#### Generate keypairs for Bob and Alice
Bob_publicKey, Bob_privateKey = newkeys(2048)
Alice_publicKey, Alice_privateKey = newkeys(2048)

#Alice tasks
#### Hash a pass phrase to create a 256 bit (32 byte) session key
digest = SHA256.new()
digest.update(b"Yibo Xu")
sessionKey = digest.digest()
print("The session key Alice have to send: \n",sessionKey)
print ()
print ()
#### Generate a public and private keypair

#### encrypt the session key with Bob's public key, convert to base64 and send the encoded, encrypted key to Bob
encrypted_msg = encrypt(sessionKey, Bob_publicKey)
print ("encrypted session key: \n", encrypted_msg)
print ()
encoded_encrypted_msg = b64encode(encrypted_msg)#convert to base64

#print(priv.exportKey(format='PEM', passphrase="Yibo Xu"))
#print ()
#with open("cs356key.pem","wb") as fd:
    #fd.write(priv.exportKey(format="PEM"))

#### EXTRA CREDIT:  Use AES and the session key to encrypt a long message to Bob
Alice_msg = "Bob, I love you. mailman:Yibo Xu"
print("This is the message have to send: ",Alice_msg)
print()
myCipher = AESCipher(str(sessionKey))
cipherText = myCipher.encrypt(Alice_msg)
#print ("The base64 encoding of the IV and cipherText:\n", cipherText)
#print ()

#with open("lab3Cipher.txt", "wb") as fd:  # note the use of "wb"
    #fd.write(cipherText)
    
#     The message should give a good "soap opera" ending to our story of love and encryption

#### EXTRA CREDIT:  Create a digital signature for the AES-encrypted file
signature = sign(cipherText, Alice_privateKey)
encoded_signature = b64encode(signature)
print ()
print ("this is the base64 version of the signature that would be sent in an email:\n", encoded_signature)
print()
#### "send the file to Bob" (basically do nothing, the info will be stored in program variables.

#msg = b"Bob, I'm not good enough for you.  You deserve someone better.  Someone like Eve!"
#Bob tasks
#### EXTRA CREDIT:  verify the message is intact and came from Alice
#msg = Alice_msg.encode('utf-8')
verification = verify(cipherText, b64decode(encoded_signature), Alice_publicKey)
print ("\nThe verification proved to be", verification)
print()

#### decrypt the session key and decode it from base64
decoded_encrypted_msg = b64decode(encoded_encrypted_msg)
print ("decoded from base64:\n", decoded_encrypted_msg)
print ()
decrypted_sessionkey = decrypt(decoded_encrypted_msg, Bob_privateKey)
print ("The session key that Bob received:\n", decrypted_sessionkey)
print ()

#assert decrypted_msg == sessionKey
#### EXTRA CREDIT: use the session key to decrypt Alice's message
#with open("lab3Cipher.txt","r") as fd:
    #cipherText = fd.read()
myCipher1 = AESCipher(str(decrypted_sessionkey))

# decrypt the file

plainText1 = myCipher1.decrypt(cipherText)
print ("The Alice's message:\n",plainText1)

