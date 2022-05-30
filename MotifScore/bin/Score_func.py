import GetScore

sites=[0,1,2,3,4,10,11,12,13,14]
lenth=15

def score_func(seq):
    score=0
    for i in sites:
        score=score+GetScore.score[i][seq[i]]
    #print (score)
    return score

#score_func("GGATTAAAAAAAGAG")