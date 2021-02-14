""" 
    This is the main function for RSA encryption.
    This includes all the math that are used to create keys and encrypt messages
    in RSA.

    concepts:

    e = public key
    d = private key
    N = modulus of q * p
    p = prime number 1
    q = prime number 2

 """



import random



class RSA:
    def __init__(self):
        pass

    def rabinMiller(self, n, c):
        a = random.randint(2, (n - 2) -2)
        x = pow(int(a), int(c), int(n))
        if x == 1 or x == n - 1:
            return True
        while c != n - 1:
            x = pow(x, 2, n)
            c *= 2 

            if x == 1:
                return False
            elif x == n - 1:
                return True

        return False

    def isPrime(self, n):
        # checks if n is prime number
        # fall back to rabinMiller if uncertain

        if n < 2:
            return False        
        lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        if n in lowPrimes:
            return True
        for prime in lowPrimes:
            if n % prime == 0:
                return False
        c = n - 1
        while c % 2 == 0:
            c /= 2

        for i in range(128):
            if not self.rabinMiller(n, c):
                return False 

        return True

    def genereateKeys(self, keysize=1024):
        e = d = N = 0
        p = self.generateLargePrime(keysize)
        q = self.generateLargePrime(keysize)
        N = p * q # RSA Modulus
        phiN = (p - 1) * (q - 1) # totient
        # e is coprime with phiN & 1 < e <= phiN
        while True:
            e = random.randrange(2 ** (keysize -1), 2 ** keysize -1)
            if (self.isCoPrime(e, phiN)):
                break
        # d is mod inv of e with respect of phiN, e * d (mod phiN) = 1
        d = self.modularInv(e, phiN)    
        
        return e, d, N

    def generateLargePrime(self, keysize):
        while True:
            num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
            if (self.isPrime(num)):

                return num

    def isCoPrime(self, p, q):
        # return True if gcd(p, q) is 1 relatively prime 

        return self.gcd(p, q) == 1

    def gcd(self, p, q): 
        # eclidean algorithm to find gcd of p and q
        while q:
            p, q = q, p % q

        return p

    # the extended Euclidean algorithm
    def egcd(self, a, b):
        s = 0; old_s = 1
        t = 1; old_t = 0
        r = b; old_r = a
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        return old_r, old_s, old_t

    def modularInv(self, a, b):
        gcd, x, y = self.egcd(a, b)
        if x < 0:
            x += b

        return x

    def encrypt(self, e, N, msg):
        cipher = ""
        for c in msg:
            m = ord(c)
            cipher += str(pow(m, e, N)) + " "

        return cipher

    def decrypt(self, d, N, cipher):
        msg = ""
        parts = cipher.split()
        for part in parts:
            if part:
                c = int(part)
                msg += chr(pow(c, d, N))

        return msg

    def main(self):
        keysize = 32
        e, d, N = self.genereateKeys(keysize)
        keys = {"pk":e,
                "d":d,
                "N":N
                }

        return keys

