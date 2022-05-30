import pandas as pd
#import numpy as np
lujing=r'D:\coding\SNP_diff_split\\'

##num_samples=6

PGX=[]
for i in (1,7):
    PGX.append("PG"+str(i)+"_summary.xls")
WT="WT_summary.xls"

PGi=PGX[0]

PGi=pd.read_csv(lujing+r"data\\"+PGi,sep="\t",index_col=1,encoding="gbk") 
WT=pd.read_csv(lujing+r"data\\"+WT,sep="\t",index_col=1,encoding="gbk")

WT_POS=WT.index
PGi_POS=PGi.index
column=WT.columns


POS_WT_and_PGi=list(set(WT_POS).intersection(set(PGi_POS)))
POS_WT_plus_PGi=list(set(WT_POS).union(set(PGi_POS)))
POS_WT_not_PGi=list(set(WT_POS).difference(set(PGi_POS)))
POS_PGi_not_WT=list(set(PGi_POS).difference(set(WT_POS)))

if len(POS_WT_not_PGi)==0:
    print ("OK! All WT mutations mutated!")
else:
    print ("Error! ")

#print (len(POS_WT_not_PGi))
#print (len(POS_WT_plus_PGi))


'''
hang1=WT.loc[WT_POS[0]]
hang1x=list(hang1)
hang1y=dict(hang1)
print (hang1x)
'''
result=PGi.loc[POS_PGi_not_WT]  #PGX+ WT- 部分结果 即所有行
#print (result)

'''
Jichao_score=[]
for POS in result.index:
    strain=result.loc[POS]["Samples"].split(",")
    score_num=len(strain)
    Jichao_score.append(20+score_num)
result["Jichao_score"]=Jichao_score

#print (result)
'''

'''
result_and=PGX.loc[POS_WT_and_PGX]  #PGX+ WT+ 部分结果
Jichao_score_and=[]
for POS in result_and.index:
    if WT.loc[POS]['REF']==PGX.loc[POS]['REF'] and WT.loc[POS]['ALT']==PGX.loc[POS]['ALT']:
        Jichao_score_and.append(0)
    else:
        score_num=len(PGX.loc[POS]["Samples"].split(","))
        Jichao_score_and.append(num_samples-score_num)
result_and["Jichao_score"]=Jichao_score_and
#print (result_and)
'''
#split结果直接不分析PGX+ WT+ 


#PGX- WT+ 的结果，根据以上长度显示，结果数为零，暂不考虑。


#result_total=pd.concat([result,result_and])
#result_total_V2=result_total.sort_values(by="Jichao_score",ascending=False)
'''
columns=list(result_total_V2.columns)
order=columns[0:4]+[columns[-1],]+columns[4:-1]

result_total_V3=result_total_V2[order]

print (result_total_V3)
'''

result.to_csv(path_or_buf=lujing+r"output\SNP_PGX_scored.csv",encoding="utf-8-sig")