low=30
start_codon=['ATG','GTG','TTG']
stop_codon=['TAA','TAG','TGA']

def translate(DNA_seq):
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }
    i=0
    AA_seq=''
    while i<len(DNA_seq):
        AA_seq=AA_seq+codontable[DNA_seq[i:i+3]]
        i=i+3
    return AA_seq

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


def findORF_first(seq_input,ORF_dic,region_initial=0):
    #ORF_dic={}
    index=len(seq_input)    #index即发现start codon的地方
    #region_initial=0        #序列缩短后重新计算位置
    for i in start_codon:
        j=seq_input.find(i)
        #start=i
        if j!=-1 and j<index:
            index=j
            start=i         #start是start codon的类型


    if index==len(seq_input):   #后面没有start codon了（找到最后了）
        seq_new=""

    else:   #找到start codon的情况下
        seq_new=seq_input[index+2:] #seq缩短，扣除到发现的start codon之后
        #严格来说应该一个碱基做一次迭代，但是只考虑ATG GTG TTG的情况下，可以2个碱基迭代一次
        region_initial=region_initial+index+3   
        #index_end=low-3 #开始搜stop codon
        #index_end=0
        i=0
        while i*3<len(seq_new)-1: #搜索stop codon
            #具体需要微调
            if seq_new[i*3+1:i*3+3+1] in stop_codon:
                if (i+1)*3<low:   #过短的ORF,考虑已经去除的start codon
                    pass
                else:
                    #print (i)
                    CDS=start+seq_new[1:i*3+3+1]  #找到的DNA序列，加到结果dic里，后续可以直接def翻译成氨基酸序列
                    region_end=region_initial+(i*3+3)
                    region=str(region_initial-3+1)+":"+str(region_end)  #region,可以作为key的一部分
                    #-3,因为region_initial从start codon下一个开始算，+1，因为偏移量从0开始，而DNA序列从1开始。
                    item_num=len(ORF_dic)
                    head=">Jichao"+str(item_num)+'_'+region
                    AA="M"+translate(CDS[3:])
                    ORF_dic[head]=[CDS,AA]
                    #break   #找到则跳出循环
                break
            else:
                i=i+1   #没找到继续找，直到找完

    return (seq_new,ORF_dic,region_initial)


#############################################
#读取fasta文件生成seq
lujing=r"D:\coding\smallORF\\"
#lujing_sub=r"source\test\\"
lujing_sub=r"source\\"

file=open(lujing+lujing_sub+"fasta.fasta")
seq_input=""
for line in file.readlines():
    if line.startswith(">"):
        pass
    else:
        seq_input=seq_input+line[:-1]
file.close()
##############################################


def ORFfind_sense(seq):
    ###递归
    ORF_dic={}
    region_initial=0
    while len(seq)>low-1:
        (seq,ORF_dic,region_initial)=findORF_first(seq,ORF_dic,region_initial)
    #print (ORF_dic)
    return (ORF_dic)
'''
def ORFfind_antisense(seq,ORF_dic):
    seq=complementary(seq)
    ORF_dic={}
    while len(seq)>low-1:
        (seq,ORF_dic)=findORF_first(seq,ORF_dic)
    return (ORF_dic)
'''

def ORFfind_both(seq):
    ORF_dic=ORFfind_sense(seq)
    com_seq=complementary(seq)
    ORF_dic_com=ORFfind_sense(com_seq)
    i=len(ORF_dic)
    lenth=len(seq)
    for item in ORF_dic_com:
        head=item.split("_")
        #print (head)
        num=int(head[0][7:])
        num_new=i+num
        offset=head[1].split(":")
        offset_up=int(offset[0])
        offset_down=int(offset[1])
        offset_up_new=lenth-offset_down+1
        offset_down_new=lenth-offset_up+1
        #就是该+1，不信你在纸上画1-10看看。
        offset_new="complementary"+str(offset_up_new)+":"+str(offset_down_new)
        head_new=">Jichao"+str(num_new)+'_'+offset_new
        ORF_dic[head_new]=ORF_dic_com[item]
    
    return (ORF_dic)

ORF_dic=ORFfind_both(seq_input)


#######################################################
result=open(lujing+"\output\\"+"ORF_Jichao.txt",'w')
#result=open(lujing+"\output\\"+"output_test.txt",'w')
i=0
for item in ORF_dic:
    line_head=item+"\n"
    line_CDS=ORF_dic[item][0]+"\n"
    line_AAseq=ORF_dic[item][1][:-1]+"\n"
    result.write(line_head)
    #result.write(line_CDS)
    result.write(line_AAseq)
    i=i+1
result.close()
#######################################################