###############################################################################
print ("先将质谱结果放在input文件夹，可修改文件名，勿修改内容。")
print ("按照提示输入文件名，注意包含正确的扩展名，如xx.txt。")
print ("输入后回车可进行下一次输入，如想结束输入q后回车。")
print ('*'*66)
filex=''
file_set=[]
while filex!='q':  
    filex=input("请输入文件名或者输入q结束输入：")
    if filex=='q':
        pass
    elif filex[-4:]=='.txt':
        file_set.append(filex)
    else:
        print ("输入正确的扩展名！")
#print (file_set)
print ("共输入 %d 个文件" %len(file_set))
###############################################################################、
up_path=r'/PromicsWJC/'
path=up_path+'input/'
need=[0,1,9,24,25,26]#如果修改，请注意修改xx01处的偏移量
need_title=["Majority protein IDs","Unique peptides","Intensity","Intensity L","Intensity H","H/L"]

def filt(promicsx):
    filex=open(path+promicsx)
    pro_data_v1=[]
    linex=1
    while linex:
        linex=filex.readline()
        pro_data_v1.append(linex.split('\t'))
    filex.close()
    #v1读取结束，原始数据

    pro_data_v2=[]
    linev2=[]
    for linex in pro_data_v1[1:]:
        if len(linex)<28:
            pass #去除可能的最后一行
        else:
            for num in need:
                linev2.append(linex[num])
            pro_data_v2.append(linev2)
            #print (linev2)
        linev2=[]
    #v2结束，保留need中指定的数据列。
#xx01
    pro_data_v3=[]
    for linex in pro_data_v2:
        if int(linex[2])>2:
            #print (linex[4:6])
            yL=float(linex[4])
            yH=float(linex[5])
            if yL==0:
                yL=1
            if yH==0:
                yH=1
            linex.append(yL/yH)
            if len(linex[1])>5:
                linex[1]=linex[1][:6]
            pro_data_v3.append(linex[1:])
    #v3结束，去除unique<=2,计算H/L并添加，删除第一列。
            #同时如果majiority有两个以上，保留第一个。
    return pro_data_v3

def write(promicsx):
#直接调用promics_filter
    out_path=up_path+'filted/'+promicsx[:-4]+'.wjc'
    output=open(out_path,'w')
    output_line=''
    for word in need_title:
        output_line=output_line+word+'_'+promicsx[:-4]+'\t'
    output.write(output_line+'\n')
    output.close()
#写入标题行
    
    add=open(out_path,'a')
    promicsx_filted=filt(promicsx)
    for linex in promicsx_filted:
        for word in linex:
            add.write(str(word)+'\t')
        add.write('\n')
    add.close()
#写入数据行

for file in file_set:
    write(file)

print ('*'*66)
print ("过滤完成，结果在filted目录下。")
print ("wjc文件可以用excel或文本编辑器打开,请核对!")
print ('$'*66)
input("按任意键退出")
