import comlementary
import random
base=['A','T','G','C']
#dictx={"00":"A","01":"G","10":"C","11":"T"}
#https://www.aleph.se/Trans/Individual/Body/ascii.html

def random_seq(n=20):
    seqn=random.choices(base,k=n)
    result=''
    for i in seqn:
        result=result+i

    return result

def txt2DNA (txt):
    dictx={"00":"A","01":"G","10":"C","11":"T"}
    #https://www.aleph.se/Trans/Individual/Body/ascii.html

    binary = ''.join('{:08b}'.format(ord(c)) for c in txt)
    result=''
    i=0
    while i<len(binary):
        code=binary[i:i+2]
        result=result+dictx[code]
        i=i+2

    return result    


#******************************************************************************
def txt_c2N23 (text_collect):
    #text_A9=["ZhaoG","∞CNS¥","SDUer","China","Ecoli"]
    result_dic={}
    #result_N23=[]
    for i in text_collect:
        seq_N23=txt2DNA(i)+random.choice(base)+"GG"
        result_dic[i]=seq_N23
        #result_N23.append(seq_N23)
    #return (result_N23, result_dic)
    return result_dic

def random2N23(n=5):
    i=0
    result=[]
    while i<n:
        seq_N23=random_seq(n=21)+"GG"
        result.append(seq_N23)
        i=i+1
    return result
#******************************************************************************


def all_output(num_random,text_collect,file_name):
    #num_random=5,text_collect=text_A9,file_name="seq_A9.txt"
    randomN23_collect=random2N23(num_random) #random N23 ***output
    txtN23_dic=txt_c2N23(text_collect) #***output
    txtN23_collect=[] #txt N23
    for i in txtN23_dic:
        txtN23_collect.append(txtN23_dic[i])
    allN23_collect=randomN23_collect+txtN23_collect
    #print (allN23_collect)
    random.shuffle(allN23_collect) #shuffled
    #print (allN23_collect)
    allN23_final=[] #***output
    com_choice=random.choice([0,1])
    for N23 in allN23_collect:
        if random.choice([0,1]):
            linshi=comlementary.complementary(N23)
            print ("****"*10)
        else:
            linshi=N23
            print ("xxxx"*10)
        print (linshi)
        allN23_final.append(linshi)
    #output:
    filex=open("output/"+file_name,'w')
    for i in txtN23_dic:
        line=i+"\t"+txtN23_dic[i]+"\n"
        #print (line)
        filex.write(line)
    for i in randomN23_collect:
        line="random"+"\t"+i+"\n"
        filex.write(line)
    filex.write("The whole seq in random order and strand:\n")
    linex=""
    for i in allN23_final:
        linex=linex+i
    filex.write(linex+"\n")
    filex.close()
#******************************************************************************

text_GU19=["ZhaoG","Ecoli"]  
text_A9=["WangJ","=42!_"] 

all_output(num_random=7,text_collect=text_GU19,file_name="GU19.txt")
all_output(num_random=7,text_collect=text_A9,file_name="A9.txt")


        
