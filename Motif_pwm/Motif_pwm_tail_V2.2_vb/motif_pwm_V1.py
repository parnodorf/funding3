#lujing=r'/Motif_pwm/'
which="CP009273.1"
#which="NC_000913.3"

#which_len="n15"
which_len="n16"
fasta="data/"+which+".fasta"

from Bio import motifs
from Bio.Seq import Seq
import comlementary

instances=[]
lujingx="data/"+which_len+".csv"
known=open(lujingx,"r")
for line in known.readlines():
    motif_ins=line.split(",")[1][:-1]
    motif_ins=motif_ins.upper()
    print ((motif_ins),len(motif_ins))
    instances.append(Seq(motif_ins))
known.close()

m=motifs.create(instances)
len_motif=len(m)
#print (m.anticonsensus)
pwm=m.counts.normalize(pseudocounts=0.5)
pssm = pwm.log_odds()

print("mean = %0.2f, standard deviation = %0.2f" % (pssm.mean(), pssm.std()))
print("max = %0.2f, min = %0.2f" % (pssm.max, pssm.min))
#mean is equal to relative entropy
threshold=pssm.mean()-pssm.std()
print("threshold = %0.2f" % threshold)
print (pssm)


#****************************************************************************************

seq_genome=''
file=open(fasta)
for line in file.readlines():
    if line.startswith(">"):
        pass
    else:
        seq_genome=seq_genome+line[:-1]
file.close()
len_genome=len(seq_genome)
seq_genome_V1=Seq(seq_genome)

#****************************************************************************************
result={}
for pos, score in pssm.search(seq_genome_V1, threshold=threshold):
    result[pos]={}
    result[pos]["score"]=score
    if pos>0:
        seq_item=seq_genome[pos:pos+len_motif]
        pos_item=str(pos+1) #index+1
    else:
        seq_item=comlementary.complementary(seq_genome[pos:pos+len_motif])
        pos_item=str(pos+len_genome+1)+"_c" #index+1
    result[pos]["pos"]=pos_item
    result[pos]["seq"]=seq_item
#print ((result))

