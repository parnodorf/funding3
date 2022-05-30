import reg_region
import pssm_info
def whether_reg (gene_reg,gene_item,pos_c,pos_item):
    pos_left=pos_item["pos_num"]
    pos_right=pos_left+reg_region.cpxR_size #不包括
    result={}
    distance=10000
    #等于-10000，代表on
    if pos_left>=gene_item["up"] and pos_right<=gene_item["down"]:
        in_or_not=1
    else:
        in_or_not=-1

    if in_or_not==1:
        if gene_item["strand"]==1:
            if pos_right<=gene_item['gene_start']:
                distance=pos_right-gene_item['gene_start']-1
            elif pos_left>=gene_item['gene_start']:
                distance=pos_left-gene_item['gene_start']+1
            else:
                distance=-10000
        elif gene_item["strand"]==-1:
            if pos_left>=gene_item['gene_start']:
                distance=gene_item['gene_start']-pos_left
            elif pos_right<=gene_item['gene_start']:
                distance=gene_item['gene_start']-pos_right+1
            else:
                distance=-10000
    else:
        pass
        
    result["has"]=in_or_not
    result["gene_reg"]=gene_reg
    result["pos_c"]=pos_c
    result["pos_int"]=pos_item["pos_num"]
    result["seq"]=pos_item['seq']
    result["score"]=pos_item['score']
    if distance==-10000:
        result['distance']="on"
    else:
        result['distance']=distance

    return (result)

##########################################################################################
#
resultV2={}
for gene_reg in reg_region.gene_reg:
    for pos_c in pssm_info.result:
        result=whether_reg(gene_reg,reg_region.gene_reg[gene_reg],pos_c,pssm_info.result[pos_c])
        if result["has"]==-1:
            pass
        else:
            #print (result)
            name=result['gene_reg']+"_"+result["pos_c"]
            resultV2[name]=result
for item in resultV2:
    #print (item, resultV2)
    pass

##########################################################################################
#write:
filex=open("output/"+"RegGene"+pssm_info.X_which[:-4]+"_"+str(reg_region.cpxR_size)+"_"+'.csv',"w")
line=["pos_int","seq","score","gene_reg","distance"]
head="name"
for x in line:
    head=head+","+x
head=head+"\n"
#print (head)
filex.write(head)
for x in resultV2:
    linex=x
    for i in line:
        linex=linex+","+str(resultV2[x][i])
    linex=linex+"\n"
    #print (linex)
    filex.write(linex)
filex.close()