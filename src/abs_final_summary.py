def abs_final_summ():
    ans = ""
    file_path = '/home/ztl/nlp/PreSumm/logs/abs_bert_cnndm.-1.candidate'
    with open(file_path,'r') as f:
        lines=f.readlines()
        for line in lines:
            ans += line
    return ans