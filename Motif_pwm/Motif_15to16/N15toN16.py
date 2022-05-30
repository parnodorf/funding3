lujing=r'/Motif_15to16/'

n15=open("data/n15.csv","r")
n16={}
for line in n15.readlines():
    ins_n15=line.split(",")
    n16[ins_n15[0]]=ins_n15[1][:7]+ins_n15[1][7]+ins_n15[1][7:]
n15.close()

#print (n16)

#output **************************************************************
file=open("output/n16.csv","w")
for i in n16:
    line=i+","+n16[i]
    file.write(line)
    print (line)
file.close()
