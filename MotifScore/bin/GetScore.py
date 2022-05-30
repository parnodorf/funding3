lujing=r'D:\coding\MotifScore\\'
#sub_lujing=r'source\test\\'
sub_lujing=r'source\\'

lenth=15
collect={}
file=open(lujing+sub_lujing+"sites.csv")
for line in file.readlines():
    if line.startswith(">"):
        pass
    else:
        item=line.split(",")
        #print (item[0])
        collect[item[0]]=item[1][:-1]
        #{gene:seq,}
#print (collect)

baseX_num={}
#{0:{"A":num,……}，}
posation=0
while posation<lenth:
    baseX_num[posation]={'A':0,'T':0,"G":0,"C":0}#total空着先不用
    posation=posation+1

for gene in collect:
    posation=0
    for base in collect[gene]:
        if base=='A':
            baseX_num[posation]['A']=baseX_num[posation]['A']+1
        elif base=='T':
            baseX_num[posation]['T']=baseX_num[posation]['T']+1
        elif base=='G':
            baseX_num[posation]['G']=baseX_num[posation]['G']+1
        elif base=='C':
            baseX_num[posation]['C']=baseX_num[posation]['C']+1
        else:
            print ("error base")
        posation=posation+1
'''
for posation in baseX_num:
    print (posation, baseX_num[posation])
#print (baseX_num)
'''

score={}
#{posation,{base:freq,……},……}
for posation in baseX_num:
    total_posation=0
    score[posation]={}
    for base in baseX_num[posation]:
        total_posation=total_posation+baseX_num[posation][base]
    for base in baseX_num[posation]:
        score[posation][base]=baseX_num[posation][base]/total_posation

'''
for posation in score:
    print (posation,score[posation])
'''