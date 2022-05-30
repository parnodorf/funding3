def complementary(seq_input):
    '''
    用于获取互补链,转成大写，不考虑非法字符
    '''
    seq_input_upper=seq_input.upper()
    seq_output=''
    seq=seq_input_upper[::-1]
    #DFprint (seq)
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