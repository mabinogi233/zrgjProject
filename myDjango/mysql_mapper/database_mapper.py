

import myDjango.myCSV.addCSV
import os
import django
os.environ.setdefault('DJANGO_SETTING_MODULE', 'xiaoxueqi_project.settings')
django.setup()



import myDjango.models
from django.db import transaction
from django.db import connection
import csv
import random
import traceback

#数据库管理，DAO层
class databaseMapper():
    def __init__(self):
        pass
    #输入字典格式测试数据（包含标签）
    #插入数据，不需要 id
    def insert(self,dict_data):
        try:
            with transaction.atomic():
                id = myDjango.models.SetFeatures.objects.count() + 1
                new_row = myDjango.models.SetFeatures.objects.create(
                    test_id=id,
                    h1n1_concern=int(dict_data['h1n1_concern']),
                    h1n1_knowledge=int(dict_data['h1n1_knowledge']),
                    behavioral_antiviral_meds=int(dict_data['behavioral_antiviral_meds']),
                    behavioral_avoidance=int(dict_data['behavioral_avoidance']),
                    behavioral_face_mask=int(dict_data['behavioral_face_mask']),
                    behavioral_wash_hands=int(dict_data['behavioral_wash_hands']),
                    behavioral_large_gatherings=int(dict_data['behavioral_large_gatherings']),
                    behavioral_outside_home=int(dict_data['behavioral_outside_home']),
                    behavioral_touch_face=int(dict_data['behavioral_touch_face']),
                    doctor_recc_h1n1=int(dict_data['doctor_recc_h1n1']),
                    doctor_recc_seasonal=int(dict_data['doctor_recc_seasonal']),
                    chronic_med_condition=int(dict_data['chronic_med_condition']),
                    child_under_6_months=int(dict_data['child_under_6_months']),
                    health_worker=int(dict_data['health_worker']),
                    health_insurance=int(dict_data['health_insurance']),
                    opinion_h1n1_vacc_effective=int(dict_data['opinion_h1n1_vacc_effective']),
                    opinion_h1n1_risk=int(dict_data['opinion_h1n1_risk']),
                    opinion_h1n1_sick_from_vacc=int(dict_data['opinion_h1n1_sick_from_vacc']),
                    opinion_seas_vacc_effective=int(dict_data['opinion_seas_vacc_effective']),
                    opinion_seas_risk=int(dict_data['opinion_seas_risk']),
                    opinion_seas_sick_from_vacc=int(dict_data['opinion_seas_sick_from_vacc']),
                    age_group=str(dict_data['age_group']),
                    education=str(dict_data['education']),
                    race=str(dict_data['race']),
                    sex=str(dict_data['sex']),
                    income_poverty=str(dict_data['income_poverty']),
                    marital_status=str(dict_data['marital_status']),
                    rent_or_own=str(dict_data['rent_or_own']),
                    employment_status=str(dict_data['employment_status']),
                    hhs_geo_region=str(dict_data['hhs_geo_region']),
                    census_msa=str(dict_data['census_msa']),
                    household_adults=int(dict_data['household_adults']),
                    household_children=int(dict_data['household_children']),
                    employment_industry=str(dict_data['employment_industry']),
                    employment_occupation=str(dict_data['employment_occupation'])
                )
                new_row.save()
                # 修改标签
                label_key = int(dict_data['h1n1_vaccine']) * 2 + int(dict_data['seasonal_vaccine']) + 1
                test_key = id
                label_test = myDjango.models.TestLabel.objects.create(
                    label=myDjango.models.SetLabels.objects.get(label_id=label_key),
                    test=myDjango.models.SetFeatures.objects.get(test_id=test_key)
                )
                label_test.save()
        except Exception:
            #回滚并继续
            print("插入失败")
            pass

    #查询全部训练数据
    def selectAll(self):
        return self.runSQL("SELECT * FROM set_features NATURAL JOIN test_label NATURAL JOIN  set_labels");


    def update(self,id,dict_data):
        try:
            with transaction.atomic():
                with transaction.atomic():
                    myDjango.models.SetFeatures.objects.filter(test_id=int(id)).update(
                        h1n1_concern = int(dict_data['h1n1_concern']),
                        h1n1_knowledge = int(dict_data['h1n1_knowledge']),
                        behavioral_antiviral_meds = int(dict_data['behavioral_antiviral_meds']),
                        behavioral_avoidance = int(dict_data['behavioral_avoidance']),
                        behavioral_face_mask = int(dict_data['behavioral_face_mask']),
                        behavioral_wash_hands = int(dict_data['behavioral_wash_hands']),
                        behavioral_large_gatherings = int(dict_data['behavioral_large_gatherings']),
                        behavioral_outside_home = int(dict_data['behavioral_outside_home']),
                        behavioral_touch_face = int(dict_data['behavioral_touch_face']),
                        doctor_recc_h1n1 = int(dict_data['doctor_recc_h1n1']),
                        doctor_recc_seasonal = int(dict_data['doctor_recc_seasonal']),
                        chronic_med_condition = int(dict_data['chronic_med_condition']),
                        child_under_6_months = int(dict_data['child_under_6_months']),
                        health_worker = int(dict_data['health_worker']),
                        health_insurance = int(dict_data['health_insurance']),
                        opinion_h1n1_vacc_effective = int(dict_data['opinion_h1n1_vacc_effective']),
                        opinion_h1n1_risk = int(dict_data['opinion_h1n1_risk']),
                        opinion_h1n1_sick_from_vacc = int(dict_data['opinion_h1n1_sick_from_vacc']),
                        opinion_seas_vacc_effective = int(dict_data['opinion_seas_vacc_effective']),
                        opinion_seas_risk = int(dict_data['opinion_seas_risk']),
                        opinion_seas_sick_from_vacc = int(dict_data['opinion_seas_sick_from_vacc']),
                        age_group = str(dict_data['age_group']),
                        education = str(dict_data['education']),
                        race = str(dict_data['race']),
                        sex = str(dict_data['sex']),
                        income_poverty = str(dict_data['income_poverty']),
                        marital_status = str(dict_data['marital_status']),
                        rent_or_own = str(dict_data['rent_or_own']),
                        employment_status = str(dict_data['employment_status']),
                        hhs_geo_region = str(dict_data['hhs_geo_region']),
                        census_msa = str(dict_data['census_msa']),
                        household_adults = int(dict_data['household_adults']),
                        household_children = int(dict_data['household_children']),
                        employment_industry = str(dict_data['employment_industry']),
                        employment_occupation = str(dict_data['employment_occupation'])
                    )
                with transaction.atomic():
                    #修改标签
                    label_key = int(dict_data['h1n1_vaccine'])*2 + int(dict_data['seasonal_vaccine']) + 1
                    test_key = id
                    label_test = myDjango.models.TestLabel.objects.filter(test=test_key).update(
                        label = myDjango.models.SetLabels.objects.get(label_id=label_key),
                        test = myDjango.models.SetFeatures.objects.get(test_id=test_key)
                    )
        except Exception:
            print("修改失败")
            pass

    #根据ID删除
    def delete(self,id):
        try:
            with transaction.atomic():
                #使用了外键，级联删除
                myDjango.models.TestLabel.objects.get(test_id=int(id)).delete()
                myDjango.models.SetFeatures.objects.get(test_id=int(id)).delete()
        except Exception:
            print("删除失败")
            pass

    def runSQL(self,strSQL):
        #返回二维list对象为结果集合
        try:
            return_list = []
            # 定义原子操作
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(strSQL)
                    for line in cursor.fetchall():
                        #变为二维list对象
                        return_list.append(list(line))
            return return_list
        except Exception:
            #输出错误sql日志
            print("SQL运行失败")
            pass

    def getCount(self):
        return myDjango.models.SetFeatures.objects.count()


    # 将csv加入数据库（禁止使用）
    def insert_data_csv(self,path):
        print()
        #使用csv模块
        # 读取csv文件,返回的是迭代类型
        i = 0
        with open(path,'r',encoding='utf-8') as fin:
            reader2 = csv.reader(fin)
            for list_data in reader2:
                if(i!=0):
                    dict_data = {}
                    #随机填充空白
                    for i in range(len(list_data)):
                        if(list_data[i]==''):
                            list_data[i]=random.randint(0,1)
                    dict_data['h1n1_concern'] = int(list_data[1])
                    dict_data['h1n1_knowledge'] = int(list_data[2])
                    dict_data['behavioral_antiviral_meds'] = int(list_data[3])
                    dict_data['behavioral_avoidance'] = int(list_data[4])
                    dict_data['behavioral_face_mask'] = int(list_data[5])
                    dict_data['behavioral_wash_hands'] = int(list_data[6])
                    dict_data['behavioral_large_gatherings'] = int(list_data[7])
                    dict_data['behavioral_outside_home'] = int(list_data[8])
                    dict_data['behavioral_touch_face'] = int(list_data[9])
                    dict_data['doctor_recc_h1n1'] = int(list_data[10])
                    dict_data['doctor_recc_seasonal'] = int(list_data[11])
                    dict_data['chronic_med_condition'] = int(list_data[12])
                    dict_data['child_under_6_months'] = int(list_data[13])
                    dict_data['health_worker'] = int(list_data[14])
                    dict_data['health_insurance'] = int(list_data[15])
                    dict_data['opinion_h1n1_vacc_effective'] = int(list_data[16])
                    dict_data['opinion_h1n1_risk'] = int(list_data[17])
                    dict_data['opinion_h1n1_sick_from_vacc'] = int(list_data[18])
                    dict_data['opinion_seas_vacc_effective'] = int(list_data[19])
                    dict_data['opinion_seas_risk'] = int(list_data[20])
                    dict_data['opinion_seas_sick_from_vacc'] = int(list_data[21])
                    dict_data['age_group'] = str(list_data[22])
                    dict_data['education'] = str(list_data[23])
                    dict_data['race'] = str(list_data[24])
                    dict_data['sex'] = str(list_data[25])
                    dict_data['income_poverty'] = str(list_data[26])
                    dict_data['marital_status'] = str(list_data[27])
                    dict_data['rent_or_own'] = str(list_data[28])
                    dict_data['employment_status'] = str(list_data[29])
                    dict_data['hhs_geo_region'] = str(list_data[30])
                    dict_data['census_msa'] = str(list_data[31])
                    dict_data['household_adults'] = int(list_data[32])
                    dict_data['household_children'] = int(list_data[33])
                    dict_data['employment_industry'] = str(list_data[34])
                    dict_data['employment_occupation'] = str(list_data[35])
                    dict_data['h1n1_vaccine'] = int(list_data[36])
                    dict_data['seasonal_vaccine']= int(list_data[37])
                    # 加入
                    self.insert(dict_data)
                i+=1

