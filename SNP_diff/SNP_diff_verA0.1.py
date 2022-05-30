import pandas as pd
#import numpy as np
lujing=r'D:\coding\SNP_diff\\'

num_samples=6

WT=pd.read_csv(lujing+r"data\WT_SNP.xls",sep="\t",index_col=1,encoding="gbk")
PGX=pd.read_csv(lujing+r"data\PGX_SNP.xls",sep="\t",index_col=1,encoding="gbk")

WT_POS=WT.index
PGX_POS=PGX.index
column=WT.columns


POS_WT_and_PGX=list(set(WT_POS).intersection(set(PGX_POS)))
POS_WT_plus_PGX=list(set(WT_POS).union(set(PGX_POS)))
POS_WT_not_PGX=list(set(WT_POS).difference(set(PGX_POS)))
POS_PGX_not_WT=list(set(PGX_POS).difference(WT_POS))

#print (len(POS_PGX_not_WT))
#print (len(POS_WT_not_PGX))


'''
hang1=WT.loc[WT_POS[0]]
hang1x=list(hang1)
hang1y=dict(hang1)
print (hang1x)
'''
result=PGX.loc[POS_PGX_not_WT]  #PGX+ WT- 部分结果
#print (result)
#result["Jichao_score"]=[]
#result["Jichao_soure"]=[]
Jichao_score=[]
for POS in result.index:
    strain=result.loc[POS]["Samples"].split(",")
    score_num=len(strain)
    Jichao_score.append(20+score_num)
result["Jichao_score"]=Jichao_score

#print (result)

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

#PGX- WT+ 的结果，根据以上长度显示，结果数为零，暂不考虑。

result_total=pd.concat([result,result_and])
result_total_V2=result_total.sort_values(by="Jichao_score",ascending=False)

columns=list(result_total_V2.columns)
order=columns[0:4]+[columns[-1],]+columns[4:-1]

result_total_V3=result_total_V2[order]

print (result_total_V3)

result_total_V3.to_csv(path_or_buf=lujing+r"output\SNP_PGX_scored.csv",encoding="utf-8-sig")