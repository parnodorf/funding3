import random
seq_NGG=''
seq_CCN=''
seq_result=''

base=['A','T','G','C']
#N20=random.choices(base,k=20)
#print (str(N20))

def random_seq(n=20):
    linshi=random.choices(base,k=n)
    N20=''
    for i in linshi:
        N20=N20+i
    return N20
#seq=random_seq(n=21)
#print (seq)

i=0
while i<10:
    seq_NGG=random_seq(n=21)+'GG'
    seq_CCN='CC'+ random_seq(n=21)
    seq_result=seq_result+random.choice([seq_NGG,seq_CCN])
    print (random.choice([seq_NGG,seq_CCN]))
    i=i+1

print (seq_result)

