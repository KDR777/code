

###### TOP SECRET INFORMATION #########
###### NO TRUDY'S ALLOWED #############
###### FOR  BOB'S EYES ONLY ###########
######   =)  =)  =)   =)   ############           



# This code will take a document, encrypt it, decrypt it, and ensure integrity. 
# This is useful when you and another are sending sensitive information and want
# to ensure you and the recipient are the only two whom can read the file. 


# Step 1. Hash Functions and Data Digests.

# SHA256:

from Crypto.Hash import SHA256
fh = open('/Users/kris/TopSecret.txt', 'rb')
dataSHA = fh.read()
hash_object = SHA256.new(data=dataSHA)
print(hash_object.hexdigest())




# Poly1305: 

from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
fh = open('/Users/kris/TopSecret.txt', 'rb')
dataPoly = fh.read()
secret = b'\xa4\x84\x85\xe6\xf1\xc8\xfe\x81\xb8\r~\x13\x94\xc7\xc4\x7f\xab\xbf5%\xdc\x00\xd8\xffS\x80\xccO\xc6J\xb1\x83'
mac = Poly1305.new(key=secret, cipher=AES)
mac.update(dataPoly)
print("Nonce: ", mac.nonce.hex())
print("MAC: ", mac.hexdigest())

hex_tag = Poly1305.new(key=secret, cipher=AES, data=dataPoly).hexdigest()





# Encryption w/ AES CBC Mode:

import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
cbc = open('/Users/kris/TopSecret.txt', 'rb')
data = cbc.read()
key = b'\xff\xf5W\x1b|\x8bn\xbey\xe0a\xdai\xe0\x11k'
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct})
print(result)
saveFile = open('/Users/kris/Documents/R00825050_AEScbc.txt', 'w')
saveFile.write(result)
saveFile.close()



# Decryption with AES CBC Mode:

new = open('/Users/kris/Documents/R00825050_AEScbc.txt', 'rb')
AESencData = new.read()
#filepath = ('/Users/kris/Documents/')
#in_file = open(AESencData, 'rb')
#out_file = open(filepath + '.Decrypted.docx', 'wb')
data = (bytes(AESencData))
key = b'\xff\xf5W\x1b|\x8bn\xbey\xe0a\xdai\xe0\x11k'
import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
try:
    b64 = json.loads(data)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    ciphertext = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(ciphertext.decrypt(ct), AES.block_size)
    print("The message was: ", pt)
except ValueError:
    print("Incorrect decryption")
# Successful decryption!!! 

saveFile = open('/Users/kris/Documents/R00825050_AES_decrypted.txt', 'wb')
saveFile.write(pt)
saveFile.close()



# Encryption with ChaCha20:

fh = open('/Users/kris/TopSecret.txt', 'rb')
dataChaCha = fh.read()
import json
from base64 import b64encode
from Crypto.Cipher import ChaCha20
plaintext = dataChaCha
key = b'\x046j\x98o\xb9\xdf2\x12\xe8\x1d\xa7k\xc3\xd8\xde\x03\xba\xbb\xe2(O@\xa70r=nr\x1e\xeb\x8d'
cipher = ChaCha20.new(key=key)
ciphertext = cipher.encrypt(plaintext)
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ciphertext).decode('utf-8')
result = json.dumps({'nonce':nonce, 'ciphertext':ct})
#print(result)
saveFile = open('/Users/kris/Documents/R00825050_ChaCha.txt', 'w')
saveFile.write(result)
saveFile.close()









# Decrypt ChaCha20:

import json
from base64 import b64decode
from Crypto.Cipher import ChaCha20   
Cbin = open('/Users/kris/Documents/R00825050_ChaCha.txt', 'rb')
cipherCHA = Cbin.read()
from Crypto.Random import get_random_bytes
nonce = get_random_bytes(12)
key = b'\x046j\x98o\xb9\xdf2\x12\xe8\x1d\xa7k\xc3\xd8\xde\x03\xba\xbb\xe2(O@\xa70r=nr\x1e\xeb\x8d'
try:
    b64 = json.loads(cipherCHA)
    nonce= b64decode(b64['nonce'])
    ciphertext = b64decode(b64['ciphertext'])
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    print("The message was ",  plaintext)
except ValueError:
    print("Incorrect decryption" )


saveFile = open('/Users/kris/Documents/R00825050_ChaCha20_decrypted.txt', 'wb')
saveFile.write(plaintext)
saveFile.close()







# Step 4 Integrity Verification:

# AES Encryption/Decription Hash SHA256 Comparison:

from Crypto.Hash import SHA256
decrypt = open('/Users/kris/Documents/R00825050_AEScbc.txt', 'rb')
integritytest = decrypt.read()

hash_object = SHA256.new(data=integritytest)
print(hash_object.hexdigest())


from Crypto.Hash import SHA256
decrypt = open('/Users/kris/Documents/R00825050_AES_decrypted.txt', 'rb')
integritytest = decrypt.read()

hash_object = SHA256.new(data=integritytest)
print(hash_object.hexdigest())






# AES Encryption/Decription Hash Poly1305 Comparison:

decrypt = open('/Users/kris/Documents/R00825050_AEScbc.txt', 'rb')
from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
secret = b'\xa4\x84\x85\xe6\xf1\xc8\xfe\x81\xb8\r~\x13\x94\xc7\xc4\x7f\xab\xbf5%\xdc\x00\xd8\xffS\x80\xccO\xc6J\xb1\x83'
mac = Poly1305.new(key=secret, cipher=AES)
mac.update(integritytest)
print("Nonce: ", mac.nonce.hex())
print("MAC: ", mac.hexdigest())

hex_tag = Poly1305.new(key=secret, cipher=AES, data=integritytest).hexdigest()



decrypt = open('/Users/kris/Documents/R00825050_AES_decrypted.txt', 'rb')
from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
secret = b'\xa4\x84\x85\xe6\xf1\xc8\xfe\x81\xb8\r~\x13\x94\xc7\xc4\x7f\xab\xbf5%\xdc\x00\xd8\xffS\x80\xccO\xc6J\xb1\x83'
mac = Poly1305.new(key=secret, cipher=AES)
mac.update(integritytest)
print("Nonce: ", mac.nonce.hex())
print("MAC: ", mac.hexdigest())

hex_tag = Poly1305.new(key=secret, cipher=AES, data=integritytest).hexdigest()


















