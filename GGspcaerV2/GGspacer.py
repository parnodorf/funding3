import comlementary
def GGspacer(spacer,prefix="tagt",sufix="gttt"):
    '''
    prefix="tagt"
    sufix="gttt"
    spacer="tttctccacttatgccatcg"
    '''
    if len(spacer)==20:
        pass
    else:
        print ("lenth is not 20")
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