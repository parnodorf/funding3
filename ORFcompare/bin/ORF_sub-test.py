lujing=r"D:\coding\ORFcompare\\"
lujing_sub=r"source\\"

def get_dic(file_name):
    ORF_dic={}
    file=open(lujing+lujing_sub+file_name)
    for line in file.readlines():
        if line.startswith(">"):
            ORF_dic[line[:-1]]=''
            temp=line[:-1]
        else:
            ORF_dic[temp]=ORF_dic[temp]+line[:-1]
    file.close()
    return (ORF_dic)

#print (len(get_dic("ORF30.txt")))
ORF1="ORF_NCBI.txt"
ORF2="ORF_Jichao.txt"
ORF1_dic=get_dic(ORF1)
ORF2_dic=get_dic(ORF2)

i=0
for item in ORF2_dic:
    if len(ORF2_dic[item])<10:
        i=i+1
        #print (ORF2_dic[item])

print (i)