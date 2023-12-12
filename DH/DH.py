import sys
from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad, unpad

#Calculating Shared Key according to Diffie Hellman Key Exchange Algorithm.
def calculateSharedKey(g_e,g_c,N_e,N_c,x,gy_modN):
    g = 2**g_e - g_c
    n = 2**N_e - N_c
    key = pow(gy_modN,x,n)
    return key

#Using in-built function to encrypt by AES block cipher.
def encrypt(plaintext, key, IV):
    cipher = AES.new(key.to_bytes((key.bit_length() + 7) // 8, byteorder='little'), AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ciphertext

#Using in-built function to decrypt by AES block cipher.
def decrypt(ciphertext, key, IV):
    cipher = AES.new(key.to_bytes((key.bit_length() + 7) // 8, byteorder='little'), AES.MODE_CBC, IV)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')

#Input

IV = bytes.fromhex(sys.argv[1])
g_e = int(sys.argv[2])
g_c = int(sys.argv[3])
N_e = int(sys.argv[4])
N_c = int(sys.argv[5])
x = int(sys.argv[6])
gy_modN = int(sys.argv[7])
ciphertext = bytes.fromhex(sys.argv[8])
plaintext = sys.argv[9]


#Calculating Key using above defined method
key = calculateSharedKey(g_e, g_c, N_e, N_c, x, gy_modN)
    
#Performing decryption and encryption using above defined methods.
d = decrypt(ciphertext, key, IV) 
e = encrypt(plaintext, key, IV)

#Printing out result
print(str(d) + ',' + binascii.hexlify(e).decode('utf-8').upper()) 




