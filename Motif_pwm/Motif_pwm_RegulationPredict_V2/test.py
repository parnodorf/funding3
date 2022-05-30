from Bio import SeqIO
genbank="data/CP009273.1.gb"
genbank_read=SeqIO.read(genbank,"genbank")
for feature in genbank_read.features:
    print (feature.location.strand)