lujing=r'D:\coding\MotifSearch\\'
sub_lujing=r'source\test\\'
#sub_lujing=r'source\\'

def complementary(seq_input):
    '''
    用于获取互补链
    '''
    seq_output=''
    seq=seq_input[::-1]
    for i in seq:
        if i=="A":
            seq_output=seq_output+"T"
        elif i=="T":
            seq_output=seq_output+"A"
        elif i=="G":
            seq_output=seq_output+"C"
        elif i=="C":
            seq_output=seq_output+"G"
    #print ("hello")
    return (seq_output)

seq=''#全基因组序列

file=open(lujing+sub_lujing+"fasta.fasta")
for line in file.readlines():
    if line.startswith(">"):
        pass
    else:
        seq=seq+line[:-1]
#print (len(seq))

seq=complementary(seq)
######################################################################
def mut_one (seq_origin):
    #seq_origin="GTAAAGTAAA"
    #产生一个突变的序列，本函数可考虑迭代
    seq_origin=seq_origin.upper()
    mut_one=[]
    lenth=len(seq_origin)
    i=0
    while i < lenth:
        if i==0:
            for base in "ATGC":
                mut=base+seq_origin[1:]
                mut_one.append(mut)
        elif i==lenth:
            for base in "ATGC":
                mut=seq_origin[:-1]+base
                mut_one.append(mut)
        else:
            for base in "ATGC":
                mut=seq_origin[0:i]+base+seq_origin[i+1:] 
                mut_one.append(mut)
        i=i+1
    
    return mut_one
#####################################################################

seq_solid="GTAAAGTAAA"
pattern_collect=mut_one(seq_solid)
pattern_collect_v2=[]
for item in pattern_collect:
    if item[0]=="G" and item[5]=="G":
        pattern_collect_v2.append(item)
    else:
        pass
#print (len(pattern_collect_v2))

####################################
#def一个函数，输入N，序列，以及是否互补的标签
def motif_search (seq,N,comple="N"):
    result={}
    for pattern in pattern_collect_v2:
        #print (pattern)
        seq_new=seq
        pattern_1=pattern[:5]
        pattern_2=pattern[5:]
        #print (pattern_1,pattern_2)

        check=1
        while check!=-1:
            #print ("wangxiaoying")
            start_all=0
            start=seq_new.find(pattern_1)
            if start==-1:
                check=-1
                #print ("none")
            else:
                start_all=start_all+start
                if seq_new[start+len(pattern_1)+N:start+len(pattern_1)+N+len(pattern_2)]==pattern_2:
                    found=seq_new[start:start+len(pattern_1)+N+len(pattern_2)]
                    site_start=start_all+start
                    site_end=start_all+start+len(pattern_1)+N+len(pattern_2)
                    if comple=="N":
                        result[str(site_start)+":"+str(site_end)]=found 
                    elif comple=="Y":
                        site_start_c=len(seq)-(site_end)
                        site_end_c=len(seq)-(site_start)
                        key="complement("+str(site_start_c)+":"+str(site_end_c)+")"
                        result[key]=found #
                else:
                    pass
                seq_new=seq_new[start+1:]
    return result
#####################################

result_all=[]
#所有结果放一起
N_set=[5,6]
seq_c=complementary(seq)
for N in N_set:
    result_all.append(motif_search(seq,N))
    result_all.append(motif_search(seq_c,N,"Y"))

result_output={}
#输出格式
jichao_num=0
for dic in result_all:
    for item in dic:
        result_output[">Jichao"+str(jichao_num)+"_"+item]=dic[item]
        jichao_num=jichao_num+1
#print (result_output)

result_print=open(lujing+"\output\\"+"Motif_Jichao.txt",'w')
i=0
for item in result_output:
    line_head=item+"\n"
    line_motif=result_output[item]+"\n"
    result_print.write(line_head)
    result_print.write(line_motif)
result_print.close()
