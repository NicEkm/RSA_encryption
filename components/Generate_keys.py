""" 
This file generates key using Encryption.py file,
that includes all the math for the RSA calculations and 
tools for creating the public and private key
 """



from components.Encryption import RSA
from components.Keys import Keys as k



class Generate_keys:
    def __init__(self):
        pass

    def Generate_keys(self):
        keys = RSA().main()
        pk = keys['pk']
        pr_k = keys['d']
        N = keys['N']
        k().save(pk, pr_k, N)
        data = {'pk':pk,
                'N':N}
        return data