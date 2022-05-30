lujing=r'D:\coding\MotifSearch\\'
#sub_lujing=r'source\test\\'
sub_lujing=r'source\\'

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

result={}

Num_N=[5,6]
for N in Num_N:
    pass

####################################
#def一个函数，输入N，序列，以及是否互补的标签
N=5
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
                result[str(site_start)+":"+str(site_end)]=found #global?
            else:
                pass
            seq_new=seq_new[start+1:]

print (len(result))
#####################################

