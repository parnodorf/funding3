def str2DNA (txtstr):
    #txtstr="ZhaoG"
    dictx={"00":"A","01":"G","10":"C","11":"T"}
    #https://www.aleph.se/Trans/Individual/Body/ascii.html
    for c in txtstr:
        binaryx=ord(c)
        print (binaryx)

    binary = ''.join('{:08b}'.format(ord(c)) for c in txtstr)

    result=''
    i=0
    while i<len(binary):
        code=binary[i:i+2]
        result=result+dictx[code]
        i=i+2

    return (result)

text_A9=["ZhaoG","∞CNS¥","SDUer","China","Ecoli"]
text_GU19=["WangJ","XieXY","@USTC","Tesla","π3.14"]

#str2DNA("π3.14")
t=227
s=chr(t).encode('latin1')
x=s.encode('utf-8')

#text=t.encode('latin1')

print (s)