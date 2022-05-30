import motif_pwm_V1
import copy
from Bio import SeqIO

refseq="data/NZ_CP009273.1.gb"
genbank="data/CP009273.1.gb"

genbank_read=SeqIO.read(genbank,"genbank")
refseq_read=SeqIO.read(refseq,"genbank")

##########################refseq reading#start##########################
genes_refseq={}
tag_dic={} #old_locus_tag:locus_tag
for feature in refseq_read.features:
    if "gene" in feature.type:
        if "locus_tag" in feature.qualifiers:
            locus_tag=feature.qualifiers["locus_tag"][0]
        else:
            locus_tag="NULL_rs_0"
        if "old_locus_tag" in feature.qualifiers:
            old_locus_tag=feature.qualifiers["old_locus_tag"][0]
        else:
            old_locus_tag="NULL_rs_1"
        start=int(feature.location.start)
        genes_refseq[start]={"locus_tag":locus_tag,"old_locus_tag":old_locus_tag}
        tag_dic[old_locus_tag]=locus_tag
#print (genes_refseq)
##########################refseq reading#end#############################

genes_genbank={}
sense_gene={}
comp_gene={}
sense_start=[]
comp_start=[]
#item=["gene","locus_tag","strand","start","end"]

for feature in genbank_read.features:
    #print (feature.type)
    if "gene" in feature.type:
        if "gene" in feature.qualifiers:
            gene=feature.qualifiers["gene"][0]
        else:
            gene="NULL"
        if "locus_tag" in feature.qualifiers:
            locus_tag=feature.qualifiers["locus_tag"][0]
        else:
            locus_tag="NULL"
        strand=int(feature.location.strand)
        start=int(feature.location.start)
        end=int(feature.location.end)
        genes_genbank[start]={"gene":gene,"locus_tag":locus_tag,"start":start,"end":end,"strand":strand}
for start in genes_genbank:
    if genes_genbank[start]["strand"]>0:
        #sense_start.append(genes_genbank[start]["start"])
        sense_gene[start]=genes_genbank[start]
    else:
        comp_gene[genes_genbank[start]["end"]]=genes_genbank[start]    #note: end as the key
        #comp_start.append(genes_genbank[start]["end"])



for key in sense_gene:
    sense_start.append(key)
    #print (key)
#print (xx)
sense_start.sort() #real start  as the key
#print (sense_start)


for key in comp_gene:
    comp_start.append(key)
comp_start.sort() #end as the key

#for start in genes_genbank:

#print (xx)

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


motif_result_s={}
motif_result_c={}
#sense gene
motif_result=copy.deepcopy(motif_pwm_V1.result)
motif_result2=copy.deepcopy(motif_pwm_V1.result)
for pos in motif_result:
    new_pos=str(pos)+"s"
    if pos>0:
        real_pos=pos+1 #pos is from 0
    else:
        real_pos=pos+motif_pwm_V1.len_genome+1 #pos is from 0
    low=find_close_low(sense_start,real_pos)
    high=low+1
    if low==-1:
        motif_result[pos]['regulate']="end;please check mannually"
        motif_result[pos]['regulation_site']="end;please check mannually"
        motif_result_s[new_pos]=motif_result[pos].copy()
    elif sense_start[high]-(real_pos+motif_pwm_V1.len_motif)<=200:
        motif_result[pos]['regulate']=sense_gene[sense_start[high]]["gene"]
        motif_result[pos]['regulation_site']=real_pos+motif_pwm_V1.len_motif-sense_start[high]
        motif_result_s[new_pos]=motif_result[pos].copy()
        motif_result_s[new_pos]["gb_locus_tag"]=sense_gene[sense_start[high]]["locus_tag"]
    elif real_pos-sense_start[low]<=100:
        motif_result[pos]["regulate"]=sense_gene[sense_start[low]]["gene"]
        motif_result[pos]["regulation_site"]=real_pos-sense_start[low]
        motif_result_s[new_pos]=motif_result[pos].copy()
        motif_result_s[new_pos]["gb_locus_tag"]=sense_gene[sense_start[low]]["locus_tag"]
    else:
        motif_result[pos]["regulate"]="NULL1"
        motif_result[pos]["regulation_site"]="NULL2"
#compl gene
#motif_result2=copy.deepcopy(motif_pwm_V1.result)
for pos in motif_result2:
    new_pos=str(pos)+"c"
    if pos>0:
        real_pos=pos+1 #pos is from 0
    else:
        real_pos=pos+motif_pwm_V1.len_genome+1 #pos is from 0
    low=find_close_low(comp_start,real_pos)
    high=low+1
    if low==-1:
        motif_result2[pos]['regulate']="end;please check mannually"
        motif_result2[pos]['regulation_site']="end;please check mannually"
        motif_result_c[new_pos]=motif_result2[pos].copy()
    elif real_pos-comp_start[low]<=200:
        motif_result2[pos]["regulate"]=comp_gene[comp_start[low]]["gene"]
        motif_result2[pos]["regulation_site"]=comp_start[low]-real_pos
        motif_result_c[new_pos]=motif_result2[pos].copy()
        motif_result_c[new_pos]["gb_locus_tag"]=comp_gene[comp_start[low]]["locus_tag"]
    elif comp_start[high]-(real_pos+motif_pwm_V1.len_motif)<=100:
        motif_result2[pos]["regulate"]=comp_gene[comp_start[high]]["gene"]
        motif_result2[pos]["regulation_site"]=comp_start[high]-(real_pos+motif_pwm_V1.len_motif)
        motif_result_c[new_pos]=motif_result2[pos].copy()
        motif_result_c[new_pos]["gb_locus_tag"]=comp_gene[comp_start[high]]["locus_tag"]
    else:
        motif_result2[pos]["regulate"]="NULL3"
        motif_result2[pos]["regulation_site"]="NULL4"

result_output={}

for key in motif_result_c:
    result_output[key]=motif_result_c[key]
    #result_output[key]["ref_seq locus_tag"]=tag_dic[result_output[key]["locus_tag"]]

for key in motif_result_s:
    result_output[key]=motif_result_s[key]
    #result_output[key]["ref_seq locus_tag"]=tag_dic[result_output[key]["locus_tag"]]

for key in result_output:
    if "gb_locus_tag" in result_output[key]:
        if result_output[key]["gb_locus_tag"] in tag_dic:
            result_output[key]["ref_seq locus_tag"]=tag_dic[result_output[key]["gb_locus_tag"]]
        else:
            result_output[key]["ref_seq locus_tag"]="NULL_no_new_tag"
    else:
         result_output[key]["ref_seq locus_tag"]="NULL_no_old_tag"

filex=open("output/CpxR_pssm_RegulationPredict_"+genbank.split("/")[-1][:-3]+'.csv',"w")
items=["pos+-","pos","score","seq","regulate","regulation_site","ref_seq locus_tag"]
head=""
for i in items:
    head=head+","+i
head=head[1:]+"\n"
filex.write(head)
for item in result_output:
    line=str(item)
    for i in items[1:]:
        line=line+","+str(result_output[item][i])
    line=line+"\n"
    filex.write(line)
filex.close()

