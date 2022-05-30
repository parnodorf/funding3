import pandas as pd
import reg_region

X_which="CpxR_pssm_annotation_CP009273.1_n15.csv"
size=reg_region.cpxR_size

pssm=pd.read_csv("data/"+X_which,encoding='gbk').set_index("pos")

result=pssm.to_dict(orient ='index')

#print (type(result))
for i in result:
    pos_num=-1
    if i.endswith("_c"):
        pos_num=int(i[:-2])
    else:
        pos_num=int(i)
    result[i]["pos_num"]=pos_num

#for i in result:
    #print(i,result[i])

#2649 {'pos+-': 2648, 'score': 9.339323, 'seq': 'GAAAAATGGCGAAAA', 'location': 'in thrA', 'tail': 'deep in the gene', 'pos_num': 2649}
