import sys

# Calculating multiplicative inverse using Extended Euclidean Algorithm 
def modular_multiplicative_inverse(a, b):
    m, x0, x1 = b, 0, 1
    while a > 1:
        quotient = a // b
        b, a = a % b, b
        x0, x1 = x1 - quotient * x0, x0
    return x1 + m if x1 < 0 else x1

#Computing the input values into the numbers p,q,e
def combine(pe,pc,qe,qc,ee,ec):
	l = []
	p = 2**pe - pc
	q = 2**qe - qc
	e = 2**ee - ec
	N = p * q
	l = [p,q,e,N]
	return l

#Generating Private Key for being used for RSA algorithm
def generatePrivateKey (e,p,q):	
	phi = (p - 1) * (q - 1)
	d = modular_multiplicative_inverse(e,phi)
	return d
	
#Decrypting the Cipher text into plain text
def decrypt (ciphertext, key, N):
	enc_msg = int(ciphertext)
	plaintext = pow(enc_msg, key, N)
	return plaintext

#Encrypting Plain text into cipher text
def encrypt ( plaintext, key, N):
	dec_msg = int(plaintext)
	ciphertext = pow(dec_msg, key, N)
	return ciphertext

#Taking input from the user as one complete string containing all the arguments.
l = []
z = input()
l = z.split(" ")

pe = int(l[0])
pc = int(l[1])
qe = int(l[2])
qc = int(l[3])
ee = int(l[4])
ec = int(l[5])
c = int(l[6])
d = int(l[7])


#Calculating given input into numbers and printing encrypted and decrypted text
D = []
D = combine(pe,pc,qe,qc,ee,ec)
key = generatePrivateKey(D[2],D[0],D[1])
dec = decrypt(c,key,D[-1])
enc = encrypt(d,D[2],D[-1])
print (str(dec) + ',' + str(enc))











