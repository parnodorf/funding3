lujing=r"D:\coding\ORFcompare\\"
lujing_sub=r"source\\"

def get_dic(file_name):
    ORF_dic={}
    file=open(lujing+lujing_sub+file_name)
    for line in file.readlines():
        if line.startswith(">"):
            ORF_dic[line[:-1]]=''
            temp=line[:-1]
        else:
            ORF_dic[temp]=ORF_dic[temp]+line[:-1]
    file.close()
    return (ORF_dic)


ORF1="ORF_Jichao.txt"   #被减数
ORF2="ORF_real.txt"     #减数
ORF1_dic=get_dic(ORF1)
ORF2_dic=get_dic(ORF2)

ORF2_value_set=[]
for item in ORF2_dic:
    ORF2_value_set.append(ORF2_dic[item])
print (len(ORF2_value_set))

ORF1new_dic=ORF1_dic.copy()
jiaoji_dic={}
#从ORF1_dic把交集摘出来，key使用ORF1_dic的
i=0
for item in ORF1_dic:
    if ORF1_dic[item] in ORF2_value_set:
        jiaoji_dic[item]=ORF1_dic[item]
        ORF1new_dic.pop(item)
    i=i+1
    #print (i)
print (len(jiaoji_dic))
print (len(ORF1new_dic))
#至此找出交集了

result=open(lujing+"output\\"+ORF1[:-4]+"-"+ORF2[:-4]+".txt","w")
for item in ORF1new_dic:
    result.write(item+"\n")
    result.write(ORF1_dic[item]+"\n")
result.close()
#########################################################################
'''
jiaoji_value_set=[]
for item in jiaoji_dic:
    jiaoji_value_set.append(jiaoji_dic[item])

ORF2new_dic=ORF2_dic.copy()
for item in ORF2_dic:
    if ORF2_dic[item] in jiaoji_value_set:
        ORF2new_dic.pop(item)
print ("*****************************************")
print (len(ORF2new_dic))

file=open(lujing+"output\\"+ORF2[:-4]+'-'+ORF1[:-4]+".txt","w")
for i in ORF2new_dic:
    if "*" in ORF2new_dic[i]:
        pass
    elif "join" in i:
        pass
    elif ORF2new_dic[i].startswith("-"):
        pass
    else:
        file.write(i+"\n")
        file.write(ORF2new_dic[i]+"\n")
file.close()
'''

'''
for i in ORF2new_dic:
    print (i)
    print (ORF2new_dic[i])
'''