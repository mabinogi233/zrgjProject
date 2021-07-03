#核心方法工厂，获取执行流程
class runFactory():
    @staticmethod
    def get_run(inputMethod,algroithmMethod,outputMethod,runMethodName="default"):

        return base_run_algroithm(inputMethod,algroithmMethod,outputMethod)

class base_run_algroithm():
    #构造方法,输入inputMethod类，algroithmMethod类，outputMethod类
    def __init__(self,inputMethod,algroithmMethod,outputMethod):
        self.inputMethod=inputMethod
        self.algroithmMethod=algroithmMethod
        self.outputMethod=outputMethod
    #子类可以重写run
    def run(self,inputData):
        #inputData，outputData使用key-value字典
        test_x = self.inputMethod.doInput(inputData)
        test_y = self.algroithmMethod.doAlgroithm(test_x)
        outputData = self.outputMethod.doOutput(test_y)
        return outputData


