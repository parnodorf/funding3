lujing=r'D:\coding\GeneID\\'
name1="test.gb"

from Bio import SeqIO

gb_seq=SeqIO.read(lujing+"data\\"+name1,"genbank")
#print (gb_seq)

#print ("features:",gb_seq.features)

item=[]
for feature in gb_seq.features:
    if "gene" in feature.type:
        #print (feature.qualifiers)
        #item.append(feature.location)
        item.append(feature.qualifiers["locus_tag"])
        if "gene" in feature.qualifiers:
            item.append(feature.qualifiers["gene"])
        else:
            item.append(["no gene name found"])
        print (item)
        item=[]
