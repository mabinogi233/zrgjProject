import myDjango.kmeans.yuChuLi


class outputFactory():
    @staticmethod
    def getOutputMethod(outputMethodName):
        #在工厂类中加入自己的方法
        if(outputMethodName == "Test"):
            return testOutputMethod()

        if (outputMethodName == 'kmeansTrain'):
            return KmeansTrainOutputMethod()

        if (outputMethodName == 'kmeansDev'):
            return KmeansDevOutputMethod()

        if (outputMethodName == 'kmeansTest'):
            return KmeansTestOutputMethodo()

        return base_OutputMethod()


#method基类
class base_OutputMethod():
    def doOutput(self):
        return None

#实现doOutput方法
class testOutputMethod(base_OutputMethod):
    def doOutput(self,test_y):
        output = test_y + "这是处理运算后的数据"
        return output

#训练
class KmeansTrainOutputMethod(base_OutputMethod):
    def doOutput(self,flag):
        if(flag):
            return "训练成功"
        else:
            return "训练失败"


#验证
class KmeansDevOutputMethod(base_OutputMethod):
    def doOutput(self,outputData):
        #返回字典，字典内部有两个二维列表,每行有两个预测标签或者两个真实标签
        print(type(outputData[0]))
        (outputData[0])['x_data'] = outputData[1]
        return outputData[0]


#运行
class KmeansTestOutputMethodo(base_OutputMethod):
    def doOutput(self,outputData):
        #返回二维列表,每行有两个预测标签
        outputData = myDjango.kmeans.yuChuLi.make_up(outputData)
        return outputData