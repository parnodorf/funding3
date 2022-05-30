lujing=r'C:\\JC_files\\Motif_pwm\\'
seq_genome="ATGC"
from Bio import motifs
from Bio.Seq import Seq

instances=[]
known=open(lujing+"data\\known.csv","r")
for line in known.readlines():
    motif_ins=line.split(",")[1][:-1]
    instances.append(Seq(motif_ins))
known.close()

m=motifs.create(instances)
#print (m.anticonsensus)
pwm=m.counts.normalize(pseudocounts=0.5)
pssm = pwm.log_odds()

print("mean = %0.2f, standard deviation = %0.2f" % (pssm.mean(), pssm.std()))
#mean is equal to relative entropy
#print (pssm)

