lujing=r"D:\coding\ORFfinder\coding\\"
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

#print (len(get_dic("ORF30.txt")))

ORF30=get_dic("ORF30.txt")
ORFreal=get_dic("ORFreal.txt")

ORFreal_set=[]
for item in ORFreal:
    ORFreal_set.append(ORFreal[item])
#print (len(ORFreal_set))

sub={}
for item in ORF30:
    if ORF30[item] in ORFreal_set:
        sub[item]=ORF30[item]
        #ORF30.pop(item)
sub_set=[]
for i in sub:
    sub_set.append(sub[i])

#print (len(sub)) #1232

ORFreal_key=[]
for i in ORFreal:
    ORFreal_key.append(i)

for i in ORFreal_key:
    if ORFreal[i] in sub_set:
        ORFreal.pop(i)
        #print (i)

for i in ORFreal:
    print (i)
    #pass

print (len(ORFreal))