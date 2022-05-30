'''
用于生成spacer（基因组中扣除CDS序列）在基因组中的位置
'''

lujing=r'D:\coding\smallORF\\'
#sub_lujing=r'source\test\\'
sub_lujing=r'source\\'

gene_num=[]

file=open(lujing+sub_lujing+'gb.gb')
for line in file.readlines():
    #print (line)
    if line.startswith("LOCUS"):
        headline=line.split()
        whole_lenth=int(headline[2])
        #print (whole_lenth)
    if line.startswith("     gene"):
        region=line[21:-1]
        if region.startswith("join"):
            num=region[5:-1].split(",")
            for i in num:
                gene_num.append(i)
                #print (i)
        elif region.startswith("complement(join"):
            num=region[16:-2].split(",")
            for i in num:
                gene_num.append(i)
            #print (i)
        elif region.startswith("complement"):
            region=region[11:-1]
            gene_num.append(region)
        else:
            gene_num.append(region)
        #print (region)
file.close()

#print (gene_num)
#['190..255', '337..2799', '2801..3000']


begin=1
end=1
space_num={} ###
name="wjc"
item=0

for i in gene_num:
    CDS=i.split("..")
    #print (CDS[0])
    CDS_begin=int(CDS[0])
    CDS_end=int(CDS[1])
    item_name=name+str(item)
    #print (temp)
    if CDS_begin>end:
        end=CDS_begin-1
        space_num[item_name]=[begin,end]
        begin=CDS_end+1    
    item=item+1
##下面添加最后一个元素，即最后一个cds的end到最后
item_name=name+str(item)
end=whole_lenth
space_num[item_name]=[begin,end]

#print (item)
#print (space_num["wjc4584"])
#print (space_num['wjc4585'])
#{'wjc0': [1, 189], 'wjc1': [256, 336], 'wjc2': [2800, 2800]}

#return space_num

