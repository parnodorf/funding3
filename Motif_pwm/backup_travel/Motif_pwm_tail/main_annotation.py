import motif_pwm_V1

from Bio import SeqIO

genbank="data/CP009273.1.gb"
tail=100    #both left and right
genbank_read=SeqIO.read(genbank,"genbank")

gene_location={}
gene_start=[]

for feature in genbank_read.features:
    #print (feature.type)
    if "gene" in feature.type:
        gene_start.append(int(feature.location.start))
        gene_location[feature.location.start]={}
        gene_location[feature.location.start]['start']=feature.location.start
        gene_location[feature.location.start]['end']=feature.location.end
        gene_location[feature.location.start]['strand']=feature.location.strand
        if "gene" in feature.qualifiers:
            gene_location[feature.location.start]['gene']=feature.qualifiers['gene'][0]
        else:
            gene_location[feature.location.start]['gene']=feature.qualifiers['locus_tag'][0]
        #print (feature.location.start-feature.location.end)
gene_start.sort()

#print (gene_start)


#*********************************************************************************************
def find_close_low(listx,numx):
    i=0
    result=-1
    mark=1
    while listx[i]<numx:
        i=i+1
        if i>len(listx)-1:
            mark=-1
            break
    if mark==-1:
        result=mark
    else:
        result=i-1

    return (result)

#***********************************************************************************************
motif_result=motif_pwm_V1.result
for pos in motif_result:
    if pos>0:
        motif_pos_real=pos+1 #pos is from 0
    else:
        motif_pos_real=pos+motif_pwm_V1.len_genome+1 #pos is from 0
    #motif_pos_real=motif_result[pos]["pos"]
    gene_low_index=find_close_low(gene_start,motif_pos_real)
    #print (gene_low_index)
    gene_start_item=gene_start[gene_low_index]
    gene_location_item=gene_location[gene_start_item]
    start=gene_location_item["start"]
    end=gene_location_item["end"]
    if motif_pos_real>start and motif_pos_real<end:
        motif_result[pos]["location"]="in "+gene_location_item["gene"]
        if (end-start)<=tail*2:
            motif_result[pos]["tail"]="gene shorter than 200"
        elif (motif_pos_real-start)<=tail:
            motif_result[pos]["tail"]="left 100bp"
        elif end-(motif_pos_real+motif_pwm_V1.len_motif)<=tail:
            motif_result[pos]["tail"]="right 100bp"
        else:
            motif_result[pos]["tail"]="deep in the gene"
    elif motif_pos_real>end:
        motif_result[pos]["location"]="between "+gene_location_item["gene"]+" and "+gene_location[gene_start[gene_low_index+1]]["gene"]
        motif_result[pos]["tail"]="NULL"
    else:
        motif_result[pos]["location"]="error!"
        motif_result[pos]["tail"]="NULL"
'''
for item in motif_result:
    print (item)
    print (motif_result[item])
'''

filex=open("output/CpxR_pssm_annotation_"+genbank.split("/")[-1][:-3]+"_tail"+'.csv',"w")
items=["pos+-","pos","score","seq","location","tail"]
head=""
for i in items:
    head=head+","+i
head=head[1:]+"\n"
filex.write(head)
for item in motif_result:
    line=str(item)
    for i in items[1:]:
        line=line+","+str(motif_result[item][i])
    line=line+"\n"
    filex.write(line)
filex.close()



