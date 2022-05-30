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
    pass
    #return seq_complementary

def findORF(seq_input,ORF_dic):
    index=len(seq_input)    #index即发现start codon的地方
    region_initial=0        #序列缩短后重新计算位置
    for i in start_codon:
        j=seq_input.find(i)
        if j!=-1 and j<index:
            index=j
            start=i         #start是start codon的类型

    if index==len(seq_input):   #后面没有start codon了
        seq_new=""

    '''
    else: 
        for stop in stop_codon:
            i_index=0
            while i_index<low:

        if zai

        else 不在 就是下面的else 整体向右缩进


    '''
    else:   #找到start codon的情况下
        seq_new=seq_input[index+3:] #seq缩短，扣除到发现的start codon之后
        ######################################
        region_initial=region_initial+index+3  #可能需要全局参数 
        index_end=low-3 #开始搜stop codon
        i=0
        while i+3<len(seq_new): #搜索stop codon
            #具体需要微调
            if seq_new[index_end+i*3:index_end+i*3+3] in stop_codon:
                CDS=start+seq_new[:index_end+i*3+3]  #找到的DNA序列，加到结果dic里，后续可以直接def翻译成氨基酸序列
                region_end=region_initial+(index_end+i*3+3)
                region=str(region_initial)+":"+str(region_end)  #region,可以作为key的一部分
                AA=translate(CDS)
                ORF_dic[region]=[CDS,AA]
                break   #找到则跳出循环
            else:
                i=i+1   #没找到继续找，直到找完

    return (seq_new,ORF_dic)

#############################################
#读取fasta文件生成seq
lujing=r"D:\coding\smallORF\\"
lujing_sub=r"source\test\\"

file=open(lujing+lujing_sub+"fasta.fasta")
seq=""
for line in file.readlines():
    if line.startswith(">"):
        pass
    else:
        seq=seq+line[:-1]
file.close()
##############################################


###递归
ORF_dic={}
while len(seq)>low-1:
    (seq,ORF_dic)=findORF(seq,ORF_dic)

#print (ORF_dic)

result=open(lujing+"\output\\"+"output.txt",'w')
i=0
for item in ORF_dic:
    line_head=">"+'Jichao'+str(i)+"_"+item+"\n"
    line_CDS=ORF_dic[item][0]+"\n"
    line_AAseq=ORF_dic[item][1][:-1]+"\n"
    result.write(line_head)
    result.write(line_CDS)
    result.write(line_AAseq)
    i=i+1
result.close()