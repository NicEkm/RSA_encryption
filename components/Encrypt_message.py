""" 
This is file that handles the encryption of the access token.
This uses the public key and the N gained from the health care app,
and encrypts the access token with those. 
"""



class Encryption:
    def __init__(self):
        pass
    def encrypt(self, e, N, msg):
        cipher = ""
        for c in msg:
            m = ord(c)
            cipher += str(pow(m, e, N)) + " "

        return cipher