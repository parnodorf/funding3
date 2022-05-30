from os import linesep
import pandas as pd
import numpy as np
import GGspacer
df=pd.read_csv (r"data/sgRNAcas9_report.xls", sep="\t", encoding="gbk")
x=df.iloc[:,[0,3]]
y=x.to_dict(orient="records")
spacer={}
for item in y:
    name=item["sgRID"]
    seq=item["Protospacer_sequence+PAM(5'-3')"]
    spacer[name]=seq
#print (spacer)

primer={}
for i in spacer:
    FR=GGspacer.GGspacer(spacer=spacer[i][:-3],prefix="tagt",sufix="gttt")
    primer[i+"F"]=FR["PrimerF"]
    primer[i+"R"]=FR["PrimerR"]

filex=open("output/primer.csv","w")
for i in primer:
    line=i+","+primer[i]+"\n"
    print (line)
    filex.write(line)
filex.close()
