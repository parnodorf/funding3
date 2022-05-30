import pandas as pd
#import numpy as np
lujing=r'D:\coding\SNP_diff_split\\'

##num_samples=6

PGX=[]
for i in range(1,7):
    PGX.append("PG"+str(i)+"_summary.xls")
WT="WT_summary.xls"
print (PGX)

WT=pd.read_csv(lujing+r"data\\"+WT,sep="\t",index_col=1,encoding="gbk")
WT_POS=WT.index
#column=WT.columns

def diff_split(file_i):
 
    PGi=pd.read_csv(lujing+r"data\\"+file_i,sep="\t",index_col=1,encoding="gbk") 
    PGi_POS=PGi.index

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


    result=PGi.loc[POS_PGi_not_WT]  #PGX+ WT- 部分结果 即所有行

    #print (lujing+r"output\SNP_"+file_i+"_scored.csv")

    result.to_csv(path_or_buf=lujing+r"output\SNP_"+file_i[:-12]+"_diff_split.csv",encoding="utf-8-sig")
 
for i in PGX:
    diff_split(i)