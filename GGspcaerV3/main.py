#本程序仅适用于BsaI和BsmI酶切位点的序列插入
from GGspacer import *

SeqName=input("Input the seq name:")

Seq=input("Input the seq:").upper()

FR=GGspacer(spacer=Seq,prefix="cgcc",sufix="gttt")
#在换启动子的时候需要修改prefix和sufix，四个碱基，不包括垫着的一个碱基

print (SeqName+"F"+","+FR["PrimerF"])
print (SeqName+"R"+","+FR["PrimerR"])