from Bio import SeqIO
from Bio.SeqIO.SffIO import _check_eof

X_which="CP009273.1"
#pssm_info里还有一个X——which要修改
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
        xx_gene['start']=int(feature.location.start)+1
        #print (xx_gene['start']),Biopython的start自动减去了1
        xx_gene['end']=int(feature.location.end)+1
        xx_gene['strand']=int(feature.location.strand)
        xx_gene['size']=xx_gene['end']-xx_gene['start']
        #print(xx_gene['end'],xx_gene['start'])
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
        up=gene_region[gene_yy]['start']-up_dis-1
        down=gene_region[gene_yy]['start']+down_dis
        gene_plus1=gene_region[gene_yy]['start']
    elif gene_region[gene_yy]['strand']==-1:
        up=gene_region[gene_yy]['end']-down_dis
        down=gene_region[gene_yy]['end']+up_dis
        gene_plus1=gene_region[gene_yy]['end']-1
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
    #gene_reg_item['up']=up
    if up<0:
        gene_reg_item['up']=0
    else:
        gene_reg_item['up']=up
    #gene_reg_item['down']=down
    if down>genome_size:
        gene_reg_item['down']=genome_size
    else:
        gene_reg_item['down']=down 
    gene_reg_item["check"]=check    #"in" or "out"
    gene_reg_item["size"]=gene_region[gene_yy]['size']
    gene_reg_item["strand"]=gene_region[gene_yy]['strand']
    gene_reg_item["gene_start"]=gene_plus1
    gene_reg[gene_yy]=gene_reg_item

for i in gene_reg:
    #print (i,gene_reg[i])
    pass

#"check"最后没用


'''
thrL {'up': 1, 'down': 290, 'check': 'out', 'size': 66, 'strand': 1, 'gene_start': 191}
thrA {'up': 1, 'down': 437, 'check': 'out', 'size': 2463, 'strand': 1, 'gene_start': 338}
thrB {'up': 2100, 'down': 2901, 'check': 'in', 'size': 933, 'strand': 1, 'gene_start': 2802}
thrC {'up': 3033, 'down': 3834, 'check': 'in', 'size': 1287, 'strand': 1, 'gene_start': 3735}
yaaX {'up': 4533, 'down': 5334, 'check': 'in', 'size': 297, 'strand': 1, 'gene_start': 5235}
yaaA {'up': 6360, 'down': 7160, 'check': 'in', 'size': 777, 'strand': -1, 'gene_start': 6460}
yaaJ {'up': 7860, 'down': 8660, 'check': 'in', 'size': 1431, 'strand': -1, 'gene_start': 7960}
talB {'up': 7537, 'down': 8338, 'check': 'in', 'size': 954, 'strand': 1, 'gene_start': 8239}
mog {'up': 8605, 'down': 9406, 'check': 'in', 'size': 588, 'strand': 1, 'gene_start': 9307}
satP {'up': 9901, 'down': 10000, 'check': 'out', 'size': 73, 'strand': -1, 'gene_start': 10001}'''