import pandas as pd 
import re
#import xlrd

path=r'D:\coding\GenomePOS\\'
path_sub=r'source\\'
path_full=path+path_sub

WT_SNP="BL21DE3q_snp_indel.xls"

WT_SNP_read=pd.read_csv(path_full+WT_SNP,sep="\t")

WT_SNP_read_INDEL=WT_SNP_read[WT_SNP_read["TYPE"]=="INDEL"]

print (WT_SNP_read_INDEL)

#print (WT_SNP_read)
