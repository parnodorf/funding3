# coding=utf-8

file=open("all3.csv",encoding='utf-8')
data_all={}
#{time:{char:['data',……]，……}，……}
lieset="ABCDEFGH"
for line in file.readlines():
    line=line[:-1]
    hang=line.split(',')
    if not line.startswith(","):
        data_all[hang[0]]={}
        time=hang[0]
        i=0
    else:
        data_all[time][lieset[i]]=hang[1:]
        i=i+1

'''
for item in data_all:
    print (item,data_all[item])
'''

curve={}
#{'A1':{},……}
hang=1
lie=0
while lie<len(lieset):
    while hang<13:
        well=lieset[lie]+str(hang)
        curve[well]={}
        hang=hang+1
    lie=lie+1
    hang=1

#print (curve)

for well in curve:
    char=well[0]
    num=int(well[1:])-1
    #print (char,num)
    for time in data_all:
        #print (time,char)
        #print (data_all[time][char][num])
        curve[well][time]=data_all[time][char][num]

'''       
for well in curve:
    print (well,curve[well])
'''
well_set=[]
#提供孔的列输出的序号索引
j=1
while j<13:
    for i in lieset:
        well_set.append(i+str(j))
    j=j+1
#print (well_set)


result_print=open("all_sorted.csv",'w')
headline="time"+','
for well in well_set:
    headline=headline+well+','
result_print.write(headline+'\n')
for time in data_all:
    line=str(time)+','
    for well in well_set:
        line=line+str(curve[well][time])+","
    line=line+'\n'
    print (line)
    result_print.write(line)
result_print.close()
    #print (line)




