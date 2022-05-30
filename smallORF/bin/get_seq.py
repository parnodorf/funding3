import space_num

seq=''

file=open(space_num.lujing+space_num.sub_lujing+"fasta.fasta")
for line in file.readlines():
    if line.startswith(">"):
        pass
    else:
        seq=seq+line[:-1]
        #print (line)
#print (len(seq))

file.close()
i=0
seq_wjc={}
for wjc in space_num.space_num:
    #temp=[]
    begin=(space_num.space_num[wjc][0])
    end=(space_num.space_num[wjc][1])
    seq_item=seq[begin:end+1]
    temp=[str(begin),str(end),seq_item]
    seq_wjc[wjc]=temp

'''
for temp in seq_wjc:
    print (seq_wjc[temp]
''''
##['4635995', '4636006', 'AGAGGCGATTTA']


'''
    if len(seq_item)==0:
        i=i+1
print (i)
'''

#return seq_wjc

###############################################
#长度为零的seq_wjc应该是重叠基因导致的，一共806个#
###############################################