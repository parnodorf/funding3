import pandas as pd
#import reg_region

X_which="CpxR_pssm_annotation_CP009273.1_n15.csv"
#X_which="test.csv"

#size=reg_region.cpxR_size

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

for i in result:
    #print(i,result[i]["pos_num"])
    pass

#2649 {'pos+-': 2648, 'score': 9.339323, 'seq': 'GAAAAATGGCGAAAA', 'location': 'in thrA', 'tail': 'deep in the gene', 'pos_num': 2649}

'''
384_c {'pos+-': -4631086, 'score': 9.086007, 'seq': 'GCAACACGCAGAAAA', 'location': 'in thrA', 'tail': 'left 100bp', 'pos_num': 384}
408 {'pos+-': 407, 'score': 7.630286, 'seq': 'GGAAAGCAATGCCAG', 'location': 'in thrA', 'tail': 'left 100bp', 'pos_num': 408}
2649 {'pos+-': 2648, 'score': 9.339323, 'seq': 'GAAAAATGGCGAAAA', 'location': 'in thrA', 'tail': 'deep in the gene', 'pos_num': 2649}
3680_c {'pos+-': -4627790, 'score': 8.828733, 'seq': 'GCAAATATGAACAAA', 'location': 'in thrB', 'tail': 'right 100bp', 'pos_num': 3680}
4164_c {'pos+-': -4627306, 'score': 9.950153, 'seq': 'GTAAACCGTAGAAAG', 'location': 'in thrC', 'tail': 'deep in the gene', 'pos_num': 4164}
4391_c {'pos+-': -4627079, 'score': 9.338232, 'seq': 'GCAAATCTGCGCCAG', 'location': 'in thrC', 'tail': 'deep in the gene', 'pos_num': 4391}
4686 {'pos+-': 4685, 'score': 8.280733, 'seq': 'GCAAAATCTGGCAAC', 'location': 'in thrC', 'tail': 'deep in the gene', 'pos_num': 4686}
4948_c {'pos+-': -4626522, 'score': 7.2763095, 'seq': 'GAAAGCAAGGGTAAA', 'location': 'in thrC', 'tail': 'right 100bp', 'pos_num': 4948}
7815_c {'pos+-': -4623655, 'score': 7.8083806, 'seq': 'GCAAAAGTCTTAAAA', 'location': 'in yaaJ', 'tail': 'deep in the gene', 'pos_num': 7815}
'''