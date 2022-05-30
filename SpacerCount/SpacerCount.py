
up="caggctgcgcaactgttgggaagggcgatcggtgcgggcctcttcgctattacgccagctggcgaaagggggatgtgctgcaaggcgattaagttgggtaacgccagggttttcccagtcacgacgttgtaaaacgacggccagtgaatt"
down="aggtaaatctctttccagcatctcttcctactagagtcgacctgcaggcatgcaagcttggcgtaatcatggtcatagctgtttcctgtgtgaaattgttatccgctcacaattccacacaacatacgagccggaagcataaagtgtaaagcctggggtgcctaatgagtgagctaactcacattaattgcgttgcgctcactgcccgctttccagtcgggaaacctgtcgtgccag"

up=up.upper()
down=down.upper()



lujing=r'D:\coding\SpacerCount\\'
sub_lujing=r'data\\'
#sub_lujing=r'data\test\\'
file_set=["result.txt","result2.txt"]
seq_set={}

for file_X in file_set:
    seq_set[file_X]={}
    file=open(lujing+sub_lujing+file_X)
    line_set=[]
    for line in file.readlines():
        line_set.append(line[:-1])
    file.close()

    i=0
    while i<len(line_set):
        if line_set[i].startswith(">"):
            seq_set[file_X][line_set[i]]=line_set[i+1]
        else:
            pass
        i=i+1

set=[20,40,60,80,100]
up_set={}
down_set={}
for i in set:
    up_set[str(i)]=up[-1*i:-1*i+19]
    down_set[str(i)]=down[i-19:i]

'''
for i in up_set:
    print (len(up_set[i]))
'''
'''
for i in down_set:
    print (len(down_set[i]))
'''

def find_spacer(seq):
    result_up={}
    result_down={}
    j=0
    k=0
    for i in up_set:
        site=seq.find(up_set[i])
        if site==-1:
            pass
        else:
            newsite=site+int(i)
            result_up[str(j)]=seq[newsite:newsite+7]
           # print (seq[newsite:newsite+7]+"**up")
            j=j+1
    for i in down_set:
        site=seq.find(down_set[i])
        if site==-1:
            pass
        else:
            newsite=site-int(i)+19
            result_down[str(k)]=seq[newsite-7:newsite]
            #print (seq[newsite-7:newsite]+"**down")
            #print (k)
            k=k+1
    if len(result_up)+len(result_down)==0:
        spacer_seq="*****************NOT FOUND*********************"
    elif len(result_up)==0:
        spacer_seq==result_down["0"]+"_please check"
    elif len(result_down)==0:
        spacer_seq=result_up["0"]+"_please check"
    elif result_up["0"]==result_down["0"]:
        spacer_seq=result_up["0"]
    else:
        #print (result_up["0"],result_down["0"])
        spacer_seq='**differrent**'+result_up["0"]+"#####"+result_down["0"]

    return spacer_seq

'''
for seq_name in seq_set['result.txt']:
    find_spacer(seq_set['result.txt'][seq_name])
'''

result_set={}
for i in file_set:
    result_set[i]={}

def GetResult(file):
    for seq_name in seq_set[file]:
        result_set[file][seq_name]=find_spacer(seq_set[file][seq_name])
for file in seq_set:
    GetResult(file)

#print (len(seq_set["result.txt"]))
#print (len(result_set["result.txt"]))
#至此数目还是对的


'''
for i in result_set['result.txt']:
    print (result_set['result.txt'][i])
'''

def WriteFile(file):
    file_output="output_"+file
    result_print=open(lujing+"\output\\"+file_output,'w')
    #for X_file in result_set:
    for name in result_set[file]:
        result_print.write(name+'\n')
        result_print.write(result_set[file][name]+'\n')
    result_print.close()

WriteFile("result.txt")
WriteFile("result2.txt")

'''
for file in file_set:
    WriteFile(file)
'''

    
'''
    file_output="output_"+file
    result_print=open(lujing+"\output\\"+file_output,'w')
    for X_file in result_set:
        for name in result_set[X_file]:
            result_print.write(name+'\n')
            result_print.write(result_set[X_file][name]+'\n')
    result_print.close()
'''