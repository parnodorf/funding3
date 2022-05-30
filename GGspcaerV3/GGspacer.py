import comlementary
def GGspacer(spacer,prefix="tagt",sufix="gttt"):

    '''
    prefix和sufix，四个碱基，不包括垫着的一个碱基
    prefix="tagt"
    sufix="gttt"
    spacer="tttctccacttatgccatcg"
    '''
    seq_len=len(spacer)
    print ("lenth is %d"%seq_len)
    PrimerF=prefix+spacer
    PrimerR_comp=spacer+sufix
    PrimerR=comlementary.complementary(PrimerR_comp)
    result={}
    result["PrimerF"]=PrimerF
    result["PrimerR"]=PrimerR
    #print (PrimerF)
    #print (PrimerR)
    return (result)

#print (GGspacer())