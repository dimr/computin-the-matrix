# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from vec import Vec
from independence import *


## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    u=Vec(a0.D,{})
    while True:
        u=list2vec([randGF2() for x in a0.D])
        if a0*u==s and b0*u==t:
            return u




#while True:
#    secret_a4=list2vec([randGF2() for x in secret_a0.D])
#    secret_b4=list2vec([randGF2() for x in secret_a0.D])
#    vecs.append((secret_a4,secret_b4))
#    if all(is_independent(list(sum(x,()))) for x in combinations(vecs,3)):
#        print(secret_a4,secret_b4)
#        break
#    else:
#        vecs.pop()



## Problem 2
# Give each vector as a Vec instancesecret_
secret_a0 = list2vec([one,one,0,one,0,one])
secret_b0 = list2vec([one,one,0,0,0,one])
secret_a1 = list2vec([one,0,one,0,0,0])
secret_b1 = list2vec([0,0,0,one,one,one])
secret_a2 = list2vec([one,one,0,0,one,one])
secret_b2 = list2vec([one,0,0,0,one,0])

secret_a3 = list2vec([one, one,one,one,one, one])
secret_b3 = list2vec([ 0,0,one,one,one,one])

secret_a4 = list2vec([one,0,one,0,one,0])
secret_b4 = list2vec([0,0, one,  0, 0, one])

