from Bio import SeqIO
from Bio.SeqIO.SffIO import _check_eof

X_which="CP009273.1"

genbank="data/"+X_which+".gb"
cpxR_size=15
up_dis=700
down_dis=100
#print (genbank)

genbank_read=SeqIO.read(genbank,"genbank")

genome_size=len(genbank_read.seq)


gene_region={}
# gene:dict, dict包含每个基因起始、终止、正负链、长度
for feature in genbank_read.features:
    if "gene" in feature.type:
        ##print (feature.type)
        xx_gene={}
        xx_gene['start']=int(feature.location.start)
        #print (xx_gene['start'])
        xx_gene['end']=int(feature.location.end)
        xx_gene['strand']=int(feature.location.strand)
        xx_gene['size']=xx_gene['start']-xx_gene['end']+1
        gene_name=(feature.qualifiers['gene'][0])
        gene_region[gene_name]=xx_gene
    else:
        pass
for item in gene_region:
    #print (item,gene_region[item])
    pass

gene_reg={}
# gene:dict, 调控区域，dict包含每个基因调控区的起始、终止、正负链、基因长度
for gene_yy in gene_region:
    gene_reg_item={}
    check="in"    
    #print (gene_region[gene_yy]['strand'])
    if gene_region[gene_yy]['strand']==1:
        up=gene_region[gene_yy]['start']-up_dis
        down=gene_region[gene_yy]['start']+(down_dis-1)
    elif gene_region[gene_yy]['strand']==-1:
        up=gene_region[gene_yy]['end']-(down_dis-1)
        down=gene_region[gene_yy]['end']+up_dis
    else:
        print ("error!")

    if up<1:
        check="out"
        up=1
    elif down>genome_size:
        check="out"
        down=genome_size
    else:
        gene_reg_item["up"]=up
        gene_reg_item["down"]=down
    gene_reg_item['up']=up
    gene_reg_item['down']=down
    gene_reg_item["check"]=check    #"in" or "out"
    gene_reg_item["size"]=gene_region[gene_yy]['size']
    gene_reg_item["strand"]=gene_region[gene_yy]['strand']
    gene_reg[gene_yy]=gene_reg_item

#for i in gene_reg:
    #print (i,gene_reg[i])

#yaaJ {'up': 7860, 'down': 8659, 'check': 'in', 'size': -1430, 'strand': -1}

