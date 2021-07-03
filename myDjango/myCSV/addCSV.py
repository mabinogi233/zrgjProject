


#加载csv文件，带标签
def load_csv(path):
    retrun_list=[]
    with open(path,'r',encoding='utf-8')as fin:
        for line in fin.readlines():
            line_list = line.strip('').strip('\n').split(',')
            for i in range(0,len(line_list)):
                if(not(22<=i<=31)):
                    line_list[i] = int(line_list[i])
    return retrun_list




