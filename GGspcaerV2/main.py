#本程序仅适用于BsaI和BsmI酶切位点的N20插入
from GGspacer import *

N20name="N20name" 
#N20的名字，可以不改

N20seq="GCGATAATCCAATTAGTAGA" 
#N20序列，需要修改

FR=GGspacer(spacer=N20seq,prefix="tagt",sufix="gttt")
#在换启动子的时候需要修改prefix和sufix

print (N20name+"F"+","+FR["PrimerF"])
print (N20name+"R"+","+FR["PrimerR"])
