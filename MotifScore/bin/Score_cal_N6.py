import Score_func_N6
import comlementary

lujing=r'D:\coding\MotifScore\\'
#sub_lujing=r'source\test\\'
sub_lujing=r'source\\'

seq=''#全基因组序列

file=open(lujing+sub_lujing+"MG1655_zhao.fasta")
for line in file.readlines():
    if line.startswith(">"):
        pass
    else:
        seq=seq+line[:-1]

score_all={}
i=0
lenth=Score_func_N6.lenth
while i<len(seq)-lenth:
    item=seq[i:i+lenth]
    #print (item)
    score=Score_func_N6.score_func_N6(item)
    score_all[str(i)+','+item]=score
    i=i+1

seq_c=comlementary.complementary(seq)
i=0
lenth=Score_func_N6.lenth
while i<len(seq_c)-lenth:
    item=seq_c[i:i+lenth]
    #print (item)
    score=Score_func_N6.score_func_N6(item)
    score_all['c'+str(len(seq)-i-lenth)+','+item]=score
    i=i+1

score_sorted=sorted(score_all.items(),key=lambda item:item[1],reverse=True)

'''
for i in score_all:
    print (i,score_all[i])
'''

'''
for i in score_sorted:
    print (i)
'''

result_print=open(lujing+"\output\\"+"Motif_Score.csv",'w')
i=0
for item in score_sorted:
    line=item[0]+','+str(item[1])+'\n'
    result_print.write(line)
result_print.close()
