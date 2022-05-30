def complementary(seq_input):
    '''
    用于获取互补链,全大写，不考虑非法字符
    '''
    seq_output=''
    seq=seq_input[::-1]
    for i in seq:
        if i=="A":
            seq_output=seq_output+"T"
        elif i=="T":
            seq_output=seq_output+"A"
        elif i=="G":
            seq_output=seq_output+"C"
        elif i=="C":
            seq_output=seq_output+"G"
    #print ("hello")
    return (seq_output)