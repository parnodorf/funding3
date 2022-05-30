import GetScore
import Score_func

lujing=r'D:\coding\MotifScore\\'
#sub_lujing=r'source\test\\'
sub_lujing=r'source\\'

score={}
for gene in GetScore.collect:
    score[gene]=Score_func.score_func(GetScore.collect[gene])
'''
for item in score:
    print (item,score[item])
'''

result_print=open(lujing+"\output\\"+"Motif_Score_source.csv",'w')
i=0
for item in score:
    line=item+','+str(score[item])+'\n'
    result_print.write(line)
result_print.close()