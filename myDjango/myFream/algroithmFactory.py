import myDjango.kmeans.keansMy as kmeans
import numpy as np

class algroithmFactory():
    @staticmethod
    def getInputMethod(algroithmMethodName):
        #在工厂类中加入自己的方法
        if(algroithmMethodName == "Test"):
            return testAlgroithmMethod()

        if(algroithmMethodName == 'kmeansTrain'):
            return KmeansTrainAlgroithmMethod()

        if(algroithmMethodName =='kmeansDev'):
            return KmeansDevAlgroithmMethod()

        if(algroithmMethodName =='kmeansTest'):
            return KmeansTestAlgroithmMethod()

        return base_AlgroithmMethod()

#method基类
class base_AlgroithmMethod():
    def doAlgroithm(self):
        return None

#实现doInput方法
class testAlgroithmMethod(base_AlgroithmMethod):
    def doAlgroithm(self,test_x):
        test_y = test_x + "这是运算过程"
        return test_y


#训练
class KmeansTrainAlgroithmMethod(base_AlgroithmMethod):
    #训练算法，根据一个人特征向量判断这个人是否接种过两种疫苗
    def doAlgroithm(self,train_data):
        try:
            #训练模型并存储模型参数
            #输入：第一列为序号，不用，倒数一二列为label，其余为test
            print('预处理成功')
            for i in range(1):
                kmeans.train(train_data)
            print("算法训练成功")
            return True
        except Exception:
            return False
        #表示训练完成
        return False

class KmeansTestAlgroithmMethod(base_AlgroithmMethod):
    #运行算法
    def doAlgroithm(self,data):
        #加载参数
        #传入数据集
        #输出结果
        return kmeans.run(data)

#验证
class KmeansDevAlgroithmMethod(base_AlgroithmMethod):
    #运行算法
    def doAlgroithm(self,data):
        # 划分test和真实label
        # 输入：第一列为序号，不用，倒数一二列为label，其余为test
        #加载参数
        #传入数据集
        #输出结果
        print(kmeans.dev(data[0]))
        return [kmeans.dev(data[0]),data[1]]