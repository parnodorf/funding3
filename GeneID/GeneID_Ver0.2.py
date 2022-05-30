lujing=r'D:\coding\GeneID\\'
name1="NZ_CP009273.1.gb"

from Bio import SeqIO

gb_seq=SeqIO.read(lujing+"data\\"+name1,"genbank")
#print (gb_seq)

#print ("features:",gb_seq.features)
result={}
for feature in gb_seq.features:
    if "gene" in feature.type:
        #print (feature.qualifiers)
        #item.append(feature.location)
        result[feature.qualifiers["locus_tag"][0]]=feature.qualifiers

result_CDS={}
for feature in gb_seq.features:
    if ("gene" not in gb_seq.features) and ("source" not in gb_seq.features):
        if "locus_tag" in feature.qualifiers:
            result_CDS[feature.qualifiers["locus_tag"][0]]=feature.qualifiers

'''
for i in result_CDS:
    print (result_CDS[i])
'''

#print (result["ECD_RS00005"])

for item in result:
    if item in result_CDS:
        result[item].update(result_CDS[item])
'''
for item in result:
    print (item)
    print (result[item])
    print ()
'''

output_item=["locus_tag","old_locus_tag","gene","product"]


#output
file_output=name1[:-3]+"_ID.csv"
result_print=open(lujing+"\output\\"+file_output,'w')

item_head=["tag_Jichao"]+output_item

for i in item_head:
    result_print.write(i+",")
result_print.write('\n')


for tag in result:
    first=[tag]
    line=[first,]
    for item in output_item:
        if item in result[tag]:
            line.append(result[tag][item])
        else:
            line.append(["NULL"])
    print (line)
    for i in line:
        result_print.write(i[0]+",")
    result_print.write('\n')

result_print.close()

'''
for name in result_set[file]:
    result_print.write(name+'\n')
    result_print.write(result_set[file][name]+'\n')
'''

