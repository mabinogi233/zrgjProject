import myDjango.myFream.runFactory as run_algroithm
from myDjango.myFream.inputFactory import inputFactory
from myDjango.myFream.outputFactory import outputFactory
from myDjango.myFream.algroithmFactory import algroithmFactory
from myDjango.myFream.runFactory import runFactory
#执行算法主函数


#method为字典，存在三个参数，对应三个名称
def run_main(inputData,methodName):
    #获取输入，输出，算法类
    inputMethod = inputFactory.getInputMethod(methodName['inputName'])
    outputMethod = outputFactory.getOutputMethod(methodName['outputName'])
    algroithmMethod = algroithmFactory.getInputMethod(methodName['algroithmName'])
    #获取执行方法类
    my_run_algroithm = runFactory.get_run(inputMethod,algroithmMethod,outputMethod)
    #执行算法
    output = my_run_algroithm.run(inputData)
    return output