""" 
This is file that saves the keys that were generated in temporary storage for further use
 """


saved_keys = {'p_k':'',
              'pr_k':'',
              'N':''}

class Keys:
    def __init__(self):
        pass
        

    def save(self, pk, pr_k, N):
        saved_keys['p_k'] = pk
        saved_keys['pr_k'] = pr_k
        saved_keys['N'] = N
        return saved_keys
    
    def load(self):
        pk = saved_keys['p_k']
        pr_k = saved_keys['pr_k']
        N = saved_keys['N']
        return pk, pr_k, N