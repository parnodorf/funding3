import random

def random_seq(n):
    i=0
    random_seq=""
    while i<n:
        random_seq=random_seq+random.choice("ATGC")
        i=i+1
    return random_seq

#print (random_seq(20))
