import GetScore

sites=[0,1,2,3,4,11,12,13,14,15]
lenth=16

def score_func_N6(seq):
    score=0
    for i in sites:
        if i<5:
            score=score+GetScore.score[i][seq[i]]
        else:
            score=score+GetScore.score[i-1][seq[i]]
    #print (score)
    return score

#score_func("GGATTAAAAAAAGAG")