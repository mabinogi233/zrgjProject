import myDjango.mysql_mapper.database_mapper
import random
import myDjango.myCSV.addCSV
import myDjango.kmeans.yuChuLi

class inputFactory():
    @staticmethod
    def getInputMethod(inputMethodName):
        #在工厂类中加入自己的方法
        if(inputMethodName == "Test"):
            return testInputMethod()

        if(inputMethodName =='kmeansTrain'):
            return KmeansTrainInputMethod()

        if(inputMethodName =='kmeansDev'):
            return KmeansDevInputMethod()

        if(inputMethodName =='kmeansTest'):
            return KmeansTestInputMethod()
        return base_InputMethod()

#method基类
class base_InputMethod():
    def doInput(self):
        return None

#实现doInput方法
class testInputMethod(base_InputMethod):
    def doInput(self,inputData):
        test_x = inputData + "这是一个测试"
        return test_x

#训练
class KmeansTrainInputMethod(base_InputMethod):
    def __init__(self):
        #使用database_mapper
        self.dataBaseMapper = myDjango.mysql_mapper.database_mapper.databaseMapper()
    def doInput(self,path=None):
        #可通过path指定训练文件，默认使用数据库
        #默认二维list类型
        data = []
        if(path!=None):
            #加载训练csv文件
            data = myDjango.myCSV.addCSV.load_csv(path)
        else:
            #加载数据库训练文件
            data = self.dataBaseMapper.selectAll()


        #预处理，字符串类型转化为数字类型
        #返回训练集
        print("加载成功")
        return myDjango.kmeans.yuChuLi.yuchuli(data)

#验证
class KmeansDevInputMethod(base_InputMethod):
    def __init__(self):
        #使用database_mapper
        self.dataBaseMapper = myDjango.mysql_mapper.database_mapper.databaseMapper()

    def doInput(self,path=None):
        #默认使用数据库随机生成验证集,inputData指定验证文件
        dev_data = []
        if(path!=None):
            # 加载训练csv文件
            dev_data = myDjango.myCSV.addCSV.load_csv(path)
        else:
            data = self.dataBaseMapper.selectAll()
            #1/5作为验证集
            for i in random.sample(range(0, len(data)), len(data)//5):
                dev_data.append(data[i])

        # 预处理，字符串类型转化为数字类型

        return [myDjango.kmeans.yuChuLi.yuchuli(dev_data),dev_data]

#运行
class KmeansTestInputMethod(base_InputMethod):
    #输入一条特征向量（人的信息）
    def doInput(self,dict_data):
        list_data = [0 for i in range(36)]
        print(dict_data)
        list_data[0] = 0
        list_data[1] = int(dict_data['h1n1_concern'])
        list_data[2] = int(dict_data['h1n1_knowledge'])
        list_data[3] = int(dict_data['behavioral_antiviral_meds'])
        list_data[4] = int(dict_data['behavioral_avoidance'])
        list_data[5] = int(dict_data['behavioral_face_mask'])
        list_data[6] = int(dict_data['behavioral_wash_hands'])
        list_data[7] = int(dict_data['behavioral_large_gatherings'])
        list_data[8] = int(dict_data['behavioral_outside_home'])
        list_data[9] = int(dict_data['behavioral_touch_face'])
        list_data[10] = int(dict_data['doctor_recc_h1n1'])
        list_data[11] = int(dict_data['doctor_recc_seasonal'])
        list_data[12] = int(dict_data['chronic_med_condition'])
        list_data[13] = int(dict_data['child_under_6_months'])
        list_data[14] = int(dict_data['health_worker'])
        list_data[15] = int(dict_data['health_insurance'])
        list_data[16] = int(dict_data['opinion_h1n1_vacc_effective'])
        list_data[17] = int(dict_data['opinion_h1n1_risk'])
        list_data[18] = int(dict_data['opinion_h1n1_sick_from_vacc'])
        list_data[19] = int(dict_data['opinion_seas_vacc_effective'])
        list_data[20] = int(dict_data['opinion_seas_risk'])
        list_data[21] = int(dict_data['opinion_seas_sick_from_vacc'])
        list_data[22] = str(dict_data['age_group'])
        list_data[23] = str(dict_data['education'])
        list_data[24] = str(dict_data['race'])
        list_data[25] = str(dict_data['sex'])
        list_data[26] = str(dict_data['income_poverty'])
        list_data[27] = str(dict_data['marital_status'])
        list_data[28]= str(dict_data['rent_or_own'])
        list_data[29] = str(dict_data['employment_status'])
        list_data[30] = str(dict_data['hhs_geo_region'])
        list_data[31] = str(dict_data['census_msa'])
        list_data[32] = int(dict_data['household_adults'])
        list_data[33] = int(dict_data['household_children'])
        list_data[34] = str(dict_data['employment_industry'])
        list_data[35] = str(dict_data['employment_occupation'])
        #预处理，str类型转化为数字类型
        return  myDjango.kmeans.yuChuLi.yuchuli_test([list_data])
