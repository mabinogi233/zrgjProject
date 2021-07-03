from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import myDjango.myFream.run_by_multprocess as runDemo
import myDjango.mysql_mapper.database_mapper as databaseMapper
import json
import random

# Create your views here.

# 训练模型
def run_train(request):
    # 参数设置
    methodName = {}
    methodName['inputName'] = 'kmeansTrain'
    methodName['outputName'] = 'kmeansTrain'
    methodName['algroithmName'] = 'kmeansTrain'
    # 调用数据库数据训练模型

    result = runDemo.run_main(None, methodName=methodName)
    # result返回字符串，表示训练成功或失败

    result_json = {'msg': result}

    print(result_json)

    return JsonResponse(result_json)


# 验证模型
def run_dev(request):
    methodName = {}
    methodName['inputName'] = 'kmeansDev'
    methodName['outputName'] = 'kmeansDev'
    methodName['algroithmName'] = 'kmeansDev'
    # 调用数据库数据验证模型

    result = runDemo.run_main(None, methodName=methodName)

    # result为字典，有3个key，为y_true和y_pre和x_data，表示真实标签和预测标签和信息，每个标签对应的值是
    # 一个二维数组，一行2列
    # result['y_true'][i]和 result['y_pre'][i]表示一个人的真实标签和预测标签
    # {'y_true':Y_true,'y_pre':Y_pre,'x_data'}
    print(type(result))
    # 输出正确率
    int0 = 0
    int1 = 0
    for i in range(len(result['y_true'])):
        print("真实：", result['y_true'][i][0], '\t', result['y_true'][i][0], "预测", result['y_pre'][i][0], '\t',
              result['y_pre'][i][0])
        # 计算h1n1标签错误个数
        if (result['y_true'][i][0] != result['y_pre'][i][0]):
            int0 += 1
        # 计算season标签错误个数
        if (result['y_true'][i][1] != result['y_pre'][i][1]):
            int1 += 1
    print("h1n1：", 1 - int0 / len(result['y_true']))
    print("season：", 1 - int1 / len(result['y_true']))

    # 返回一维列表，列表每个成员是一个字典，每个字典格式为：
    # {'h1n1_true': '真实标签，, 'h1n1_pre': '预测标签,
    # 'season_true':'真实标签','season_pre':'预测标签'}
    #  每个标签为0 1

    # 格式转化
    json_list = []
    for i in range(len(result['y_true'])):
        dict_data={}
        dict_data['h1n1_concern'] = result['x_data'][i][2]
        dict_data['h1n1_knowledge'] = result['x_data'][i][3]
        dict_data['behavioral_antiviral_meds'] = result['x_data'][i][4]
        dict_data['behavioral_avoidance'] = result['x_data'][i][5]
        dict_data['behavioral_face_mask'] = result['x_data'][i][6]
        dict_data['behavioral_wash_hands'] = result['x_data'][i][7]
        dict_data['behavioral_large_gatherings'] = result['x_data'][i][8]
        dict_data['behavioral_outside_home'] = result['x_data'][i][9]
        dict_data['behavioral_touch_face'] =result['x_data'][i][10]
        dict_data['doctor_recc_h1n1'] = result['x_data'][i][11]
        dict_data['doctor_recc_seasonal'] = result['x_data'][i][12]
        dict_data['chronic_med_condition'] = result['x_data'][i][13]
        dict_data['child_under_6_months'] = result['x_data'][i][14]
        dict_data['health_worker'] = result['x_data'][i][15]
        dict_data['health_insurance'] = result['x_data'][i][16]
        dict_data['opinion_h1n1_vacc_effective'] = result['x_data'][i][17]
        dict_data['opinion_h1n1_risk'] = result['x_data'][i][18]
        dict_data['opinion_h1n1_sick_from_vacc'] = result['x_data'][i][19]
        dict_data['opinion_seas_vacc_effective'] = result['x_data'][i][20]
        dict_data['opinion_seas_risk'] = result['x_data'][i][21]
        dict_data['opinion_seas_sick_from_vacc'] = result['x_data'][i][22]
        dict_data['age_group'] = result['x_data'][i][23]
        dict_data['education'] = result['x_data'][i][24]
        dict_data['race'] = result['x_data'][i][25]
        dict_data['sex'] = result['x_data'][i][26]
        dict_data['income_poverty'] = result['x_data'][i][27]
        dict_data['marital_status'] = result['x_data'][i][28]
        dict_data['rent_or_own'] = result['x_data'][i][29]
        dict_data['employment_status'] =result['x_data'][i][30]
        dict_data['hhs_geo_region'] = result['x_data'][i][31]
        dict_data['census_msa'] = result['x_data'][i][32]
        dict_data['household_adults'] = result['x_data'][i][33]
        dict_data['household_children'] = result['x_data'][i][34]
        dict_data['employment_industry'] = result['x_data'][i][35]
        dict_data['employment_occupation'] = result['x_data'][i][36]
        dict_data['h1n1_true'] = float(result['y_true'][i][0])
        dict_data['h1n1_pre'] = float(result['y_pre'][i][0])
        dict_data['season_true'] = float(result['y_true'][i][1])
        dict_data['season_pre'] = float(result['y_pre'][i][1])
        json_list.append(dict_data)


    # 定义需要的统计量######################################################
    # opinion_h1n1_vacc_effective的h1n1疫苗统计量  #1
    opinion_h1n1_vacc_effective_1_score_h1n1_count = 0
    opinion_h1n1_vacc_effective_2_score_h1n1_count = 0
    opinion_h1n1_vacc_effective_3_score_h1n1_count = 0
    opinion_h1n1_vacc_effective_4_score_h1n1_count = 0
    opinion_h1n1_vacc_effective_5_score_h1n1_count = 0
    # opinion_h1n1_vacc_effective的season疫苗统计量
    opinion_h1n1_vacc_effective_1_score_season_count = 0
    opinion_h1n1_vacc_effective_2_score_season_count = 0
    opinion_h1n1_vacc_effective_3_score_season_count = 0
    opinion_h1n1_vacc_effective_4_score_season_count = 0
    opinion_h1n1_vacc_effective_5_score_season_count = 0

    # opinion_h1n1_risk的h1n1疫苗统计量 #2
    opinion_h1n1_risk_1_score_h1n1_count = 0
    opinion_h1n1_risk_2_score_h1n1_count = 0
    opinion_h1n1_risk_3_score_h1n1_count = 0
    opinion_h1n1_risk_4_score_h1n1_count = 0
    opinion_h1n1_risk_5_score_h1n1_count = 0
    # opinion_h1n1_risk的season疫苗统计量
    opinion_h1n1_risk_1_score_season_count = 0
    opinion_h1n1_risk_2_score_season_count = 0
    opinion_h1n1_risk_3_score_season_count = 0
    opinion_h1n1_risk_4_score_season_count = 0
    opinion_h1n1_risk_5_score_season_count = 0

    # opinion_h1n1_sick_from_vacc的h1n1疫苗统计量 #3
    opinion_h1n1_sick_from_vacc_1_score_h1n1_count = 0
    opinion_h1n1_sick_from_vacc_2_score_h1n1_count = 0
    opinion_h1n1_sick_from_vacc_3_score_h1n1_count = 0
    opinion_h1n1_sick_from_vacc_4_score_h1n1_count = 0
    opinion_h1n1_sick_from_vacc_5_score_h1n1_count = 0
    # opinion_h1n1_sick_from_vacc的season疫苗统计量
    opinion_h1n1_sick_from_vacc_1_score_season_count = 0
    opinion_h1n1_sick_from_vacc_2_score_season_count = 0
    opinion_h1n1_sick_from_vacc_3_score_season_count = 0
    opinion_h1n1_sick_from_vacc_4_score_season_count = 0
    opinion_h1n1_sick_from_vacc_5_score_season_count = 0

    # opinion_seas_vacc_effective的h1n1疫苗统计量 #4
    opinion_seas_vacc_effective_1_score_h1n1_count = 0
    opinion_seas_vacc_effective_2_score_h1n1_count = 0
    opinion_seas_vacc_effective_3_score_h1n1_count = 0
    opinion_seas_vacc_effective_4_score_h1n1_count = 0
    opinion_seas_vacc_effective_5_score_h1n1_count = 0
    # opinion_seas_vacc_effective的season疫苗统计量
    opinion_seas_vacc_effective_1_score_season_count = 0
    opinion_seas_vacc_effective_2_score_season_count = 0
    opinion_seas_vacc_effective_3_score_season_count = 0
    opinion_seas_vacc_effective_4_score_season_count = 0
    opinion_seas_vacc_effective_5_score_season_count = 0

    # opinion_seas_risk的h1n1疫苗统计量 #5
    opinion_seas_risk_1_score_h1n1_count = 0
    opinion_seas_risk_2_score_h1n1_count = 0
    opinion_seas_risk_3_score_h1n1_count = 0
    opinion_seas_risk_4_score_h1n1_count = 0
    opinion_seas_risk_5_score_h1n1_count = 0
    # opinion_seas_risk的season疫苗统计量
    opinion_seas_risk_1_score_season_count = 0
    opinion_seas_risk_2_score_season_count = 0
    opinion_seas_risk_3_score_season_count = 0
    opinion_seas_risk_4_score_season_count = 0
    opinion_seas_risk_5_score_season_count = 0
    # END########################################################################

    # 1
    opinion_h1n1_vacc_effective1 = 0
    opinion_h1n1_vacc_effective2 = 0
    opinion_h1n1_vacc_effective3 = 0
    opinion_h1n1_vacc_effective4 = 0
    opinion_h1n1_vacc_effective5 = 0

    # 2
    opinion_h1n1_risk1 = 0
    opinion_h1n1_risk2 = 0
    opinion_h1n1_risk3 = 0
    opinion_h1n1_risk4 = 0
    opinion_h1n1_risk5 = 0

    # 3
    opinion_h1n1_sick_from_vacc1 = 0
    opinion_h1n1_sick_from_vacc2 = 0
    opinion_h1n1_sick_from_vacc3 = 0
    opinion_h1n1_sick_from_vacc4 = 0
    opinion_h1n1_sick_from_vacc5 = 0

    # 4
    opinion_seas_vacc_effective1 = 0
    opinion_seas_vacc_effective2 = 0
    opinion_seas_vacc_effective3 = 0
    opinion_seas_vacc_effective4 = 0
    opinion_seas_vacc_effective5 = 0

    # 5
    opinion_seas_risk1 = 0
    opinion_seas_risk2 = 0
    opinion_seas_risk3 = 0
    opinion_seas_risk4 = 0
    opinion_seas_risk5 = 0

    for item in json_list:
        # opinion_h1n1_vacc_effective #1
        if int(item['opinion_h1n1_vacc_effective']) == 1:
            opinion_h1n1_vacc_effective1 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_vacc_effective_1_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_vacc_effective_1_score_season_count += 1
        elif int(item['opinion_h1n1_vacc_effective']) == 2:
            opinion_h1n1_vacc_effective2 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_vacc_effective_2_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_vacc_effective_2_score_season_count += 1
        elif int(item['opinion_h1n1_vacc_effective']) == 3:
            opinion_h1n1_vacc_effective3 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_vacc_effective_3_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_vacc_effective_3_score_season_count += 1
        elif int(item['opinion_h1n1_vacc_effective']) == 4:
            opinion_h1n1_vacc_effective4 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_vacc_effective_4_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_vacc_effective_4_score_season_count += 1
        elif int(item['opinion_h1n1_vacc_effective']) == 5:
            opinion_h1n1_vacc_effective5 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_vacc_effective_5_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_vacc_effective_5_score_season_count += 1
        else:
            pass

        # opinion_h1n1_risk #2
        if int(item['opinion_h1n1_risk']) == 1:
            opinion_h1n1_risk1 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_risk_1_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_risk_1_score_season_count += 1
        elif int(item['opinion_h1n1_risk']) == 2:
            opinion_h1n1_risk2 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_risk_2_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_risk_2_score_season_count += 1
        elif int(item['opinion_h1n1_risk']) == 3:
            opinion_h1n1_risk3 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_risk_3_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_risk_3_score_season_count += 1
        elif int(item['opinion_h1n1_risk']) == 4:
            opinion_h1n1_risk4 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_risk_4_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_risk_4_score_season_count += 1
        elif int(item['opinion_h1n1_risk']) == 5:
            opinion_h1n1_risk5 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_risk_5_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_risk_5_score_season_count += 1
        else:
            pass

        # opinion_h1n1_sick_from_vacc #3
        if int(item['opinion_h1n1_sick_from_vacc']) == 1:
            opinion_h1n1_sick_from_vacc1 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_sick_from_vacc_1_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_sick_from_vacc_1_score_season_count += 1
        elif int(item['opinion_h1n1_sick_from_vacc']) == 2:
            opinion_h1n1_sick_from_vacc2 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_sick_from_vacc_2_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_sick_from_vacc_2_score_season_count += 1
        elif int(item['opinion_h1n1_sick_from_vacc']) == 3:
            opinion_h1n1_sick_from_vacc3 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_sick_from_vacc_3_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_sick_from_vacc_3_score_season_count += 1
        elif int(item['opinion_h1n1_sick_from_vacc']) == 4:
            opinion_h1n1_sick_from_vacc4 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_sick_from_vacc_4_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_sick_from_vacc_4_score_season_count += 1
        elif int(item['opinion_h1n1_sick_from_vacc']) == 5:
            opinion_h1n1_sick_from_vacc5 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_h1n1_sick_from_vacc_5_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_h1n1_sick_from_vacc_5_score_season_count += 1
        else:
            pass

        # opinion_seas_vacc_effective #4
        if int(item['opinion_seas_vacc_effective']) == 1:
            opinion_seas_vacc_effective1 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_vacc_effective_1_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_vacc_effective_1_score_season_count += 1
        elif int(item['opinion_seas_vacc_effective']) == 2:
            opinion_seas_vacc_effective2 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_vacc_effective_2_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_vacc_effective_2_score_season_count += 1
        elif int(item['opinion_seas_vacc_effective']) == 3:
            opinion_seas_vacc_effective3 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_vacc_effective_3_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_vacc_effective_3_score_season_count += 1
        elif int(item['opinion_seas_vacc_effective']) == 4:
            opinion_seas_vacc_effective4 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_vacc_effective_4_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_vacc_effective_4_score_season_count += 1
        elif int(item['opinion_seas_vacc_effective']) == 5:
            opinion_seas_vacc_effective5 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_vacc_effective_5_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_vacc_effective_5_score_season_count += 1
        else:
            pass

        # opinion_seas_risk #5
        if int(item['opinion_seas_risk']) == 1:
            opinion_seas_risk1 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_risk_1_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_risk_1_score_season_count += 1
        elif int(item['opinion_seas_risk']) == 2:
            opinion_seas_risk2 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_risk_2_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_risk_2_score_season_count += 1
        elif int(item['opinion_seas_risk']) == 3:
            opinion_seas_risk3 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_risk_3_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_risk_3_score_season_count += 1
        elif int(item['opinion_seas_risk']) == 4:
            opinion_seas_risk4 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_risk_4_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_risk_4_score_season_count += 1
        elif int(item['opinion_seas_risk']) == 5:
            opinion_seas_risk5 += 1
            if int(item['h1n1_pre']) == 1:
                opinion_seas_risk_5_score_h1n1_count += 1
            if int(item['season_pre']) == 1:
                opinion_seas_risk_5_score_season_count += 1
        else:
            pass

    json_list_len = len(json_list)

    x_label = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    y_label = [1.0, 2.0, 3.0, 4.0, 5.0]

    # 1
    opinion_h1n1_vacc_effective_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_h1n1_vacc_effective_1_score_h1n1_count / opinion_h1n1_vacc_effective1),
        "ratio2": float(opinion_h1n1_vacc_effective_2_score_h1n1_count / opinion_h1n1_vacc_effective2),
        "ratio3": float(opinion_h1n1_vacc_effective_3_score_h1n1_count / opinion_h1n1_vacc_effective3),
        "ratio4": float(opinion_h1n1_vacc_effective_4_score_h1n1_count / opinion_h1n1_vacc_effective4),
        "ratio5": float(opinion_h1n1_vacc_effective_5_score_h1n1_count / opinion_h1n1_vacc_effective5),
    }
    opinion_h1n1_vacc_effective_ylabel_season_ratio = {
        "ratio1": float(opinion_h1n1_vacc_effective_1_score_season_count / opinion_h1n1_vacc_effective1),
        "ratio2": float(opinion_h1n1_vacc_effective_2_score_season_count / opinion_h1n1_vacc_effective2),
        "ratio3": float(opinion_h1n1_vacc_effective_3_score_season_count / opinion_h1n1_vacc_effective3),
        "ratio4": float(opinion_h1n1_vacc_effective_4_score_season_count / opinion_h1n1_vacc_effective4),
        "ratio5": float(opinion_h1n1_vacc_effective_5_score_season_count / opinion_h1n1_vacc_effective5),
    }

    # 2
    opinion_h1n1_risk_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_h1n1_risk_1_score_h1n1_count / opinion_h1n1_risk1),
        "ratio2": float(opinion_h1n1_risk_2_score_h1n1_count / opinion_h1n1_risk2),
        "ratio3": float(opinion_h1n1_risk_3_score_h1n1_count / opinion_h1n1_risk3),
        "ratio4": float(opinion_h1n1_risk_4_score_h1n1_count / opinion_h1n1_risk4),
        "ratio5": float(opinion_h1n1_risk_5_score_h1n1_count / opinion_h1n1_risk5),
    }
    opinion_h1n1_risk_ylabel_season_ratio = {
        "ratio1": float(opinion_h1n1_risk_1_score_season_count / opinion_h1n1_risk1),
        "ratio2": float(opinion_h1n1_risk_2_score_season_count / opinion_h1n1_risk2),
        "ratio3": float(opinion_h1n1_risk_3_score_season_count / opinion_h1n1_risk3),
        "ratio4": float(opinion_h1n1_risk_4_score_season_count / opinion_h1n1_risk4),
        "ratio5": float(opinion_h1n1_risk_5_score_season_count / opinion_h1n1_risk5),
    }

    # 3
    opinion_h1n1_sick_from_vacc_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_h1n1_sick_from_vacc_1_score_h1n1_count / opinion_h1n1_sick_from_vacc1),
        "ratio2": float(opinion_h1n1_sick_from_vacc_2_score_h1n1_count / opinion_h1n1_sick_from_vacc2),
        "ratio3": float(opinion_h1n1_sick_from_vacc_3_score_h1n1_count / opinion_h1n1_sick_from_vacc3),
        "ratio4": float(opinion_h1n1_sick_from_vacc_4_score_h1n1_count / opinion_h1n1_sick_from_vacc4),
        "ratio5": float(opinion_h1n1_sick_from_vacc_5_score_h1n1_count / opinion_h1n1_sick_from_vacc5),
    }
    opinion_h1n1_sick_from_vacc_ylabel_season_ratio = {
        "ratio1": float(opinion_h1n1_sick_from_vacc_1_score_season_count / opinion_h1n1_sick_from_vacc1),
        "ratio2": float(opinion_h1n1_sick_from_vacc_2_score_season_count / opinion_h1n1_sick_from_vacc2),
        "ratio3": float(opinion_h1n1_sick_from_vacc_3_score_season_count / opinion_h1n1_sick_from_vacc3),
        "ratio4": float(opinion_h1n1_sick_from_vacc_4_score_season_count / opinion_h1n1_sick_from_vacc4),
        "ratio5": float(opinion_h1n1_sick_from_vacc_5_score_season_count / opinion_h1n1_sick_from_vacc5),
    }

    # 4
    opinion_seas_vacc_effective_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_seas_vacc_effective_1_score_h1n1_count / opinion_seas_vacc_effective1),
        "ratio2": float(opinion_seas_vacc_effective_2_score_h1n1_count / opinion_seas_vacc_effective2),
        "ratio3": float(opinion_seas_vacc_effective_3_score_h1n1_count / opinion_seas_vacc_effective3),
        "ratio4": float(opinion_seas_vacc_effective_4_score_h1n1_count / opinion_seas_vacc_effective4),
        "ratio5": float(opinion_seas_vacc_effective_5_score_h1n1_count / opinion_seas_vacc_effective5),
    }
    opinion_seas_vacc_effective_ylabel_season_ratio = {
        "ratio1": float(opinion_seas_vacc_effective_1_score_season_count / opinion_seas_vacc_effective1),
        "ratio2": float(opinion_seas_vacc_effective_2_score_season_count / opinion_seas_vacc_effective2),
        "ratio3": float(opinion_seas_vacc_effective_3_score_season_count / opinion_seas_vacc_effective3),
        "ratio4": float(opinion_seas_vacc_effective_4_score_season_count / opinion_seas_vacc_effective4),
        "ratio5": float(opinion_seas_vacc_effective_5_score_season_count / opinion_seas_vacc_effective5),
    }

    # 5
    opinion_seas_risk_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_seas_risk_1_score_h1n1_count / opinion_seas_risk1),
        "ratio2": float(opinion_seas_risk_2_score_h1n1_count / opinion_seas_risk2),
        "ratio3": float(opinion_seas_risk_3_score_h1n1_count / opinion_seas_risk3),
        "ratio4": float(opinion_seas_risk_4_score_h1n1_count / opinion_seas_risk4),
        "ratio5": float(opinion_seas_risk_5_score_h1n1_count / opinion_seas_risk5),
    }
    opinion_seas_risk_ylabel_season_ratio = {
        "ratio1": float(opinion_seas_risk_1_score_season_count / opinion_seas_risk1),
        "ratio2": float(opinion_seas_risk_2_score_season_count / opinion_seas_risk2),
        "ratio3": float(opinion_seas_risk_3_score_season_count / opinion_seas_risk3),
        "ratio4": float(opinion_seas_risk_4_score_season_count / opinion_seas_risk4),
        "ratio5": float(opinion_seas_risk_5_score_season_count / opinion_seas_risk5),
    }

    # 图1的json数据
    paint_opinion_h1n1_vacc_effective = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_h1n1_vacc_effective_ylabel_h1n1_ratio": opinion_h1n1_vacc_effective_ylabel_h1n1_ratio,
        "opinion_h1n1_vacc_effective_ylabel_season_ratio": opinion_h1n1_vacc_effective_ylabel_season_ratio}

    # 图2的json数据
    paint_opinion_h1n1_risk = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_h1n1_risk_ylabel_h1n1_ratio": opinion_h1n1_risk_ylabel_h1n1_ratio,
        "opinion_h1n1_risk_ylabel_season_ratio": opinion_h1n1_risk_ylabel_season_ratio}

    # 图3的json数据
    paint_opinion_h1n1_sick_from_vacc = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_h1n1_sick_from_vacc_ylabel_h1n1_ratio": opinion_h1n1_sick_from_vacc_ylabel_h1n1_ratio,
        "opinion_h1n1_sick_from_vacc_ylabel_season_ratio": opinion_h1n1_sick_from_vacc_ylabel_season_ratio}

    # 图4的json数据
    paint_opinion_seas_vacc_effective = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_seas_vacc_effective_ylabel_h1n1_ratio": opinion_seas_vacc_effective_ylabel_h1n1_ratio,
        "opinion_seas_vacc_effective_ylabel_season_ratio": opinion_seas_vacc_effective_ylabel_season_ratio}

    # 图5的json数据
    paint_opinion_seas_risk = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_seas_risk_ylabel_h1n1_ratio": opinion_seas_risk_ylabel_h1n1_ratio,
        "opinion_seas_risk_ylabel_season_ratio": opinion_seas_risk_ylabel_season_ratio}

    all_paint = {
        "paint_opinion_h1n1_vacc_effective": paint_opinion_h1n1_vacc_effective,
        "paint_opinion_h1n1_risk": paint_opinion_h1n1_risk,
        "paint_opinion_h1n1_sick_from_vacc": paint_opinion_h1n1_sick_from_vacc,
        "paint_opinion_h1n1_sick_from_vacc": paint_opinion_h1n1_sick_from_vacc,
        "paint_opinion_seas_vacc_effective": paint_opinion_seas_vacc_effective,
        "paint_opinion_seas_risk": paint_opinion_seas_risk}


    return JsonResponse(all_paint)

# 运行模型
def run_test(request):
    # 不要改methodName
    methodName = {}
    methodName['inputName'] = 'kmeansTest'
    methodName['outputName'] = 'kmeansTest'
    methodName['algroithmName'] = 'kmeansTest'
    dict_data = {}
    # 应这样与前端相连,使用时应修改
    # dict_data['h1n1_concern'] = request.POST.get('h1n1_concern')
    dict_data['h1n1_concern'] = 0
    dict_data['h1n1_knowledge'] = 0
    dict_data['behavioral_antiviral_meds'] = 0
    dict_data['behavioral_avoidance'] = 0
    dict_data['behavioral_face_mask'] = 0
    dict_data['behavioral_wash_hands'] = 0
    dict_data['behavioral_large_gatherings'] = 0
    dict_data['behavioral_outside_home'] = 0
    dict_data['behavioral_touch_face'] = 0
    dict_data['doctor_recc_h1n1'] = 0
    dict_data['doctor_recc_seasonal'] = 0
    dict_data['chronic_med_condition'] = 0
    dict_data['child_under_6_months'] = 0
    dict_data['health_worker'] = 0
    dict_data['health_insurance'] = 0

    dict_data['opinion_h1n1_vacc_effective'] = 0#request.POST.get('opinion_h1n1_vacc_effective')
    dict_data['opinion_h1n1_risk'] = 0#request.POST.get('opinion_h1n1_risk')
    dict_data['opinion_h1n1_sick_from_vacc'] = 0#request.POST.get('opinion_h1n1_sick_from_vacc')
    dict_data['opinion_seas_vacc_effective'] = 0#request.POST.get('opinion_seas_vacc_effective')
    dict_data['opinion_seas_risk'] = 0#request.POST.get('opinion_seas_risk')

    dict_data['opinion_seas_sick_from_vacc'] = 0
    dict_data['age_group'] = '0'
    dict_data['education'] = '0'
    dict_data['race'] = '0'
    dict_data['sex'] = '0'
    dict_data['income_poverty'] = '0'
    dict_data['marital_status'] = '0'
    dict_data['rent_or_own'] = '0'
    dict_data['employment_status'] = '0'
    dict_data['hhs_geo_region'] = '0'
    dict_data['census_msa'] = '0'
    dict_data['household_adults'] = 0
    dict_data['household_children'] = 0
    dict_data['employment_industry'] = '0'
    dict_data['employment_occupation'] = '0'
    # 运行预测
    result = runDemo.run_main(dict_data, methodName=methodName)
    # result为二维数组，只有一行2列
    # 返回字典，两个键,h1n1和season,值为两个数0或1,incidence为发病率
    dict_data['h1n1']=float(result[0][0])
    dict_data['h1n1_incidence'] = float(result[0][2])
    dict_data['season']=float(result[0][1])
    dict_data['season_incidence'] = float(result[0][3])

    return JsonResponse(dict_data)

#返回全部数据
def get_all(request):
    result = databaseMapper.databaseMapper().selectAll()
    print("查询成功")
    json_list = []
    for i in range(len(result)):
        dict_data={}
        dict_data['h1n1_concern'] = result[i][2]
        dict_data['h1n1_knowledge'] = result[i][3]
        dict_data['behavioral_antiviral_meds'] = result[i][4]
        dict_data['behavioral_avoidance'] = result[i][5]
        dict_data['behavioral_face_mask'] =result[i][6]
        dict_data['behavioral_wash_hands'] = result[i][7]
        dict_data['behavioral_large_gatherings'] = result[i][8]
        dict_data['behavioral_outside_home'] = result[i][9]
        dict_data['behavioral_touch_face'] = result[i][10]
        dict_data['doctor_recc_h1n1'] = result[i][11]
        dict_data['doctor_recc_seasonal'] = result[i][12]
        dict_data['chronic_med_condition'] = result[i][13]
        dict_data['child_under_6_months'] = result[i][14]
        dict_data['health_worker'] = result[i][15]
        dict_data['health_insurance'] = result[i][16]
        dict_data['opinion_h1n1_vacc_effective'] = result[i][17]
        dict_data['opinion_h1n1_risk'] = result[i][18]
        dict_data['opinion_h1n1_sick_from_vacc'] = result[i][19]
        dict_data['opinion_seas_vacc_effective'] = result[i][20]
        dict_data['opinion_seas_risk'] = result[i][21]
        dict_data['opinion_seas_sick_from_vacc'] = result[i][22]
        dict_data['age_group'] = result[i][23]
        dict_data['education'] = result[i][24]
        dict_data['race'] = result[i][25]
        dict_data['sex'] = result[i][26]
        dict_data['income_poverty'] = result[i][27]
        dict_data['marital_status'] = result[i][28]
        dict_data['rent_or_own'] = result[i][29]
        dict_data['employment_status'] = result[i][30]
        dict_data['hhs_geo_region'] = result[i][31]
        dict_data['census_msa'] = result[i][32]
        dict_data['household_adults'] = result[i][33]
        dict_data['household_children'] = result[i][34]
        dict_data['employment_industry'] = result[i][35]
        dict_data['employment_occupation'] = result[i][36]
        dict_data['h1n1_true'] = result[i][37]
        dict_data['season_true'] = result[i][38]
        json_list.append(dict_data)
    print("变化成功")
    #统计
    # 定义需要的统计量######################################################
    # opinion_h1n1_vacc_effective的h1n1疫苗统计量  #1
    opinion_h1n1_vacc_effective_1_score_h1n1_count = 0
    opinion_h1n1_vacc_effective_2_score_h1n1_count = 0
    opinion_h1n1_vacc_effective_3_score_h1n1_count = 0
    opinion_h1n1_vacc_effective_4_score_h1n1_count = 0
    opinion_h1n1_vacc_effective_5_score_h1n1_count = 0
    # opinion_h1n1_vacc_effective的season疫苗统计量
    opinion_h1n1_vacc_effective_1_score_season_count = 0
    opinion_h1n1_vacc_effective_2_score_season_count = 0
    opinion_h1n1_vacc_effective_3_score_season_count = 0
    opinion_h1n1_vacc_effective_4_score_season_count = 0
    opinion_h1n1_vacc_effective_5_score_season_count = 0

    # opinion_h1n1_risk的h1n1疫苗统计量 #2
    opinion_h1n1_risk_1_score_h1n1_count = 0
    opinion_h1n1_risk_2_score_h1n1_count = 0
    opinion_h1n1_risk_3_score_h1n1_count = 0
    opinion_h1n1_risk_4_score_h1n1_count = 0
    opinion_h1n1_risk_5_score_h1n1_count = 0
    # opinion_h1n1_risk的season疫苗统计量
    opinion_h1n1_risk_1_score_season_count = 0
    opinion_h1n1_risk_2_score_season_count = 0
    opinion_h1n1_risk_3_score_season_count = 0
    opinion_h1n1_risk_4_score_season_count = 0
    opinion_h1n1_risk_5_score_season_count = 0

    # opinion_h1n1_sick_from_vacc的h1n1疫苗统计量 #3
    opinion_h1n1_sick_from_vacc_1_score_h1n1_count = 0
    opinion_h1n1_sick_from_vacc_2_score_h1n1_count = 0
    opinion_h1n1_sick_from_vacc_3_score_h1n1_count = 0
    opinion_h1n1_sick_from_vacc_4_score_h1n1_count = 0
    opinion_h1n1_sick_from_vacc_5_score_h1n1_count = 0
    # opinion_h1n1_sick_from_vacc的season疫苗统计量
    opinion_h1n1_sick_from_vacc_1_score_season_count = 0
    opinion_h1n1_sick_from_vacc_2_score_season_count = 0
    opinion_h1n1_sick_from_vacc_3_score_season_count = 0
    opinion_h1n1_sick_from_vacc_4_score_season_count = 0
    opinion_h1n1_sick_from_vacc_5_score_season_count = 0

    # opinion_seas_vacc_effective的h1n1疫苗统计量 #4
    opinion_seas_vacc_effective_1_score_h1n1_count = 0
    opinion_seas_vacc_effective_2_score_h1n1_count = 0
    opinion_seas_vacc_effective_3_score_h1n1_count = 0
    opinion_seas_vacc_effective_4_score_h1n1_count = 0
    opinion_seas_vacc_effective_5_score_h1n1_count = 0
    # opinion_seas_vacc_effective的season疫苗统计量
    opinion_seas_vacc_effective_1_score_season_count = 0
    opinion_seas_vacc_effective_2_score_season_count = 0
    opinion_seas_vacc_effective_3_score_season_count = 0
    opinion_seas_vacc_effective_4_score_season_count = 0
    opinion_seas_vacc_effective_5_score_season_count = 0

    # opinion_seas_risk的h1n1疫苗统计量 #5
    opinion_seas_risk_1_score_h1n1_count = 0
    opinion_seas_risk_2_score_h1n1_count = 0
    opinion_seas_risk_3_score_h1n1_count = 0
    opinion_seas_risk_4_score_h1n1_count = 0
    opinion_seas_risk_5_score_h1n1_count = 0
    # opinion_seas_risk的season疫苗统计量
    opinion_seas_risk_1_score_season_count = 0
    opinion_seas_risk_2_score_season_count = 0
    opinion_seas_risk_3_score_season_count = 0
    opinion_seas_risk_4_score_season_count = 0
    opinion_seas_risk_5_score_season_count = 0
    # END########################################################################

    # 1
    opinion_h1n1_vacc_effective1 = 0
    opinion_h1n1_vacc_effective2 = 0
    opinion_h1n1_vacc_effective3 = 0
    opinion_h1n1_vacc_effective4 = 0
    opinion_h1n1_vacc_effective5 = 0

    # 2
    opinion_h1n1_risk1 = 0
    opinion_h1n1_risk2 = 0
    opinion_h1n1_risk3 = 0
    opinion_h1n1_risk4 = 0
    opinion_h1n1_risk5 = 0

    # 3
    opinion_h1n1_sick_from_vacc1 = 0
    opinion_h1n1_sick_from_vacc2 = 0
    opinion_h1n1_sick_from_vacc3 = 0
    opinion_h1n1_sick_from_vacc4 = 0
    opinion_h1n1_sick_from_vacc5 = 0

    # 4
    opinion_seas_vacc_effective1 = 0
    opinion_seas_vacc_effective2 = 0
    opinion_seas_vacc_effective3 = 0
    opinion_seas_vacc_effective4 = 0
    opinion_seas_vacc_effective5 = 0

    # 5
    opinion_seas_risk1 = 0
    opinion_seas_risk2 = 0
    opinion_seas_risk3 = 0
    opinion_seas_risk4 = 0
    opinion_seas_risk5 = 0

    for item in json_list:
        # opinion_h1n1_vacc_effective #1
        if int(item['opinion_h1n1_vacc_effective']) == 1:
            opinion_h1n1_vacc_effective1 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_vacc_effective_1_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_vacc_effective_1_score_season_count += 1
        elif int(item['opinion_h1n1_vacc_effective']) == 2:
            opinion_h1n1_vacc_effective2 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_vacc_effective_2_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_vacc_effective_2_score_season_count += 1
        elif int(item['opinion_h1n1_vacc_effective']) == 3:
            opinion_h1n1_vacc_effective3 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_vacc_effective_3_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_vacc_effective_3_score_season_count += 1
        elif int(item['opinion_h1n1_vacc_effective']) == 4:
            opinion_h1n1_vacc_effective4 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_vacc_effective_4_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_vacc_effective_4_score_season_count += 1
        elif int(item['opinion_h1n1_vacc_effective']) == 5:
            opinion_h1n1_vacc_effective5 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_vacc_effective_5_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_vacc_effective_5_score_season_count += 1
        else:
            pass

        # opinion_h1n1_risk #2
        if int(item['opinion_h1n1_risk']) == 1:
            opinion_h1n1_risk1 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_risk_1_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_risk_1_score_season_count += 1
        elif int(item['opinion_h1n1_risk']) == 2:
            opinion_h1n1_risk2 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_risk_2_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_risk_2_score_season_count += 1
        elif int(item['opinion_h1n1_risk']) == 3:
            opinion_h1n1_risk3 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_risk_3_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_risk_3_score_season_count += 1
        elif int(item['opinion_h1n1_risk']) == 4:
            opinion_h1n1_risk4 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_risk_4_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_risk_4_score_season_count += 1
        elif int(item['opinion_h1n1_risk']) == 5:
            opinion_h1n1_risk5 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_risk_5_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_risk_5_score_season_count += 1
        else:
            pass

        # opinion_h1n1_sick_from_vacc #3
        if int(item['opinion_h1n1_sick_from_vacc']) == 1:
            opinion_h1n1_sick_from_vacc1 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_sick_from_vacc_1_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_sick_from_vacc_1_score_season_count += 1
        elif int(item['opinion_h1n1_sick_from_vacc']) == 2:
            opinion_h1n1_sick_from_vacc2 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_sick_from_vacc_2_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_sick_from_vacc_2_score_season_count += 1
        elif int(item['opinion_h1n1_sick_from_vacc']) == 3:
            opinion_h1n1_sick_from_vacc3 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_sick_from_vacc_3_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_sick_from_vacc_3_score_season_count += 1
        elif int(item['opinion_h1n1_sick_from_vacc']) == 4:
            opinion_h1n1_sick_from_vacc4 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_sick_from_vacc_4_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_sick_from_vacc_4_score_season_count += 1
        elif int(item['opinion_h1n1_sick_from_vacc']) == 5:
            opinion_h1n1_sick_from_vacc5 += 1
            if int(item['h1n1_true']) == 1:
                opinion_h1n1_sick_from_vacc_5_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_h1n1_sick_from_vacc_5_score_season_count += 1
        else:
            pass

        # opinion_seas_vacc_effective #4
        if int(item['opinion_seas_vacc_effective']) == 1:
            opinion_seas_vacc_effective1 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_vacc_effective_1_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_vacc_effective_1_score_season_count += 1
        elif int(item['opinion_seas_vacc_effective']) == 2:
            opinion_seas_vacc_effective2 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_vacc_effective_2_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_vacc_effective_2_score_season_count += 1
        elif int(item['opinion_seas_vacc_effective']) == 3:
            opinion_seas_vacc_effective3 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_vacc_effective_3_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_vacc_effective_3_score_season_count += 1
        elif int(item['opinion_seas_vacc_effective']) == 4:
            opinion_seas_vacc_effective4 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_vacc_effective_4_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_vacc_effective_4_score_season_count += 1
        elif int(item['opinion_seas_vacc_effective']) == 5:
            opinion_seas_vacc_effective5 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_vacc_effective_5_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_vacc_effective_5_score_season_count += 1
        else:
            pass

        # opinion_seas_risk #5
        if int(item['opinion_seas_risk']) == 1:
            opinion_seas_risk1 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_risk_1_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_risk_1_score_season_count += 1
        elif int(item['opinion_seas_risk']) == 2:
            opinion_seas_risk2 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_risk_2_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_risk_2_score_season_count += 1
        elif int(item['opinion_seas_risk']) == 3:
            opinion_seas_risk3 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_risk_3_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_risk_3_score_season_count += 1
        elif int(item['opinion_seas_risk']) == 4:
            opinion_seas_risk4 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_risk_4_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_risk_4_score_season_count += 1
        elif int(item['opinion_seas_risk']) == 5:
            opinion_seas_risk5 += 1
            if int(item['h1n1_true']) == 1:
                opinion_seas_risk_5_score_h1n1_count += 1
            if int(item['season_true']) == 1:
                opinion_seas_risk_5_score_season_count += 1
        else:
            pass

    json_list_len = len(json_list)

    x_label = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    y_label = [1.0, 2.0, 3.0, 4.0, 5.0]
    # 1
    opinion_h1n1_vacc_effective_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_h1n1_vacc_effective_1_score_h1n1_count / opinion_h1n1_vacc_effective1),
        "ratio2": float(opinion_h1n1_vacc_effective_2_score_h1n1_count / opinion_h1n1_vacc_effective2),
        "ratio3": float(opinion_h1n1_vacc_effective_3_score_h1n1_count / opinion_h1n1_vacc_effective3),
        "ratio4": float(opinion_h1n1_vacc_effective_4_score_h1n1_count / opinion_h1n1_vacc_effective4),
        "ratio5": float(opinion_h1n1_vacc_effective_5_score_h1n1_count / opinion_h1n1_vacc_effective5),
    }
    opinion_h1n1_vacc_effective_ylabel_season_ratio = {
        "ratio1": float(opinion_h1n1_vacc_effective_1_score_season_count / opinion_h1n1_vacc_effective1),
        "ratio2": float(opinion_h1n1_vacc_effective_2_score_season_count / opinion_h1n1_vacc_effective2),
        "ratio3": float(opinion_h1n1_vacc_effective_3_score_season_count / opinion_h1n1_vacc_effective3),
        "ratio4": float(opinion_h1n1_vacc_effective_4_score_season_count / opinion_h1n1_vacc_effective4),
        "ratio5": float(opinion_h1n1_vacc_effective_5_score_season_count / opinion_h1n1_vacc_effective5),
    }

    # 2
    opinion_h1n1_risk_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_h1n1_risk_1_score_h1n1_count / opinion_h1n1_risk1),
        "ratio2": float(opinion_h1n1_risk_2_score_h1n1_count / opinion_h1n1_risk2),
        "ratio3": float(opinion_h1n1_risk_3_score_h1n1_count / opinion_h1n1_risk3),
        "ratio4": float(opinion_h1n1_risk_4_score_h1n1_count / opinion_h1n1_risk4),
        "ratio5": float(opinion_h1n1_risk_5_score_h1n1_count / opinion_h1n1_risk5),
    }
    opinion_h1n1_risk_ylabel_season_ratio = {
        "ratio1": float(opinion_h1n1_risk_1_score_season_count / opinion_h1n1_risk1),
        "ratio2": float(opinion_h1n1_risk_2_score_season_count / opinion_h1n1_risk2),
        "ratio3": float(opinion_h1n1_risk_3_score_season_count / opinion_h1n1_risk3),
        "ratio4": float(opinion_h1n1_risk_4_score_season_count / opinion_h1n1_risk4),
        "ratio5": float(opinion_h1n1_risk_5_score_season_count / opinion_h1n1_risk5),
    }

    # 3
    opinion_h1n1_sick_from_vacc_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_h1n1_sick_from_vacc_1_score_h1n1_count / opinion_h1n1_sick_from_vacc1),
        "ratio2": float(opinion_h1n1_sick_from_vacc_2_score_h1n1_count / opinion_h1n1_sick_from_vacc2),
        "ratio3": float(opinion_h1n1_sick_from_vacc_3_score_h1n1_count / opinion_h1n1_sick_from_vacc3),
        "ratio4": float(opinion_h1n1_sick_from_vacc_4_score_h1n1_count / opinion_h1n1_sick_from_vacc4),
        "ratio5": float(opinion_h1n1_sick_from_vacc_5_score_h1n1_count / opinion_h1n1_sick_from_vacc5),
    }
    opinion_h1n1_sick_from_vacc_ylabel_season_ratio = {
        "ratio1": float(opinion_h1n1_sick_from_vacc_1_score_season_count / opinion_h1n1_sick_from_vacc1),
        "ratio2": float(opinion_h1n1_sick_from_vacc_2_score_season_count / opinion_h1n1_sick_from_vacc2),
        "ratio3": float(opinion_h1n1_sick_from_vacc_3_score_season_count / opinion_h1n1_sick_from_vacc3),
        "ratio4": float(opinion_h1n1_sick_from_vacc_4_score_season_count / opinion_h1n1_sick_from_vacc4),
        "ratio5": float(opinion_h1n1_sick_from_vacc_5_score_season_count / opinion_h1n1_sick_from_vacc5),
    }

    # 4
    opinion_seas_vacc_effective_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_seas_vacc_effective_1_score_h1n1_count / opinion_seas_vacc_effective1),
        "ratio2": float(opinion_seas_vacc_effective_2_score_h1n1_count / opinion_seas_vacc_effective2),
        "ratio3": float(opinion_seas_vacc_effective_3_score_h1n1_count / opinion_seas_vacc_effective3),
        "ratio4": float(opinion_seas_vacc_effective_4_score_h1n1_count / opinion_seas_vacc_effective4),
        "ratio5": float(opinion_seas_vacc_effective_5_score_h1n1_count / opinion_seas_vacc_effective5),
    }
    opinion_seas_vacc_effective_ylabel_season_ratio = {
        "ratio1": float(opinion_seas_vacc_effective_1_score_season_count / opinion_seas_vacc_effective1),
        "ratio2": float(opinion_seas_vacc_effective_2_score_season_count / opinion_seas_vacc_effective2),
        "ratio3": float(opinion_seas_vacc_effective_3_score_season_count / opinion_seas_vacc_effective3),
        "ratio4": float(opinion_seas_vacc_effective_4_score_season_count / opinion_seas_vacc_effective4),
        "ratio5": float(opinion_seas_vacc_effective_5_score_season_count / opinion_seas_vacc_effective5),
    }

    # 5
    opinion_seas_risk_ylabel_h1n1_ratio = {
        "ratio1": float(opinion_seas_risk_1_score_h1n1_count / opinion_seas_risk1),
        "ratio2": float(opinion_seas_risk_2_score_h1n1_count / opinion_seas_risk2),
        "ratio3": float(opinion_seas_risk_3_score_h1n1_count / opinion_seas_risk3),
        "ratio4": float(opinion_seas_risk_4_score_h1n1_count / opinion_seas_risk4),
        "ratio5": float(opinion_seas_risk_5_score_h1n1_count / opinion_seas_risk5),
    }
    opinion_seas_risk_ylabel_season_ratio = {
        "ratio1": float(opinion_seas_risk_1_score_season_count / opinion_seas_risk1),
        "ratio2": float(opinion_seas_risk_2_score_season_count / opinion_seas_risk2),
        "ratio3": float(opinion_seas_risk_3_score_season_count / opinion_seas_risk3),
        "ratio4": float(opinion_seas_risk_4_score_season_count / opinion_seas_risk4),
        "ratio5": float(opinion_seas_risk_5_score_season_count / opinion_seas_risk5),
    }

    # 图1的json数据
    paint_opinion_h1n1_vacc_effective = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_h1n1_vacc_effective_ylabel_h1n1_ratio": opinion_h1n1_vacc_effective_ylabel_h1n1_ratio,
        "opinion_h1n1_vacc_effective_ylabel_season_ratio": opinion_h1n1_vacc_effective_ylabel_season_ratio}

    # 图2的json数据
    paint_opinion_h1n1_risk = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_h1n1_risk_ylabel_h1n1_ratio": opinion_h1n1_risk_ylabel_h1n1_ratio,
        "opinion_h1n1_risk_ylabel_season_ratio": opinion_h1n1_risk_ylabel_season_ratio}

    # 图3的json数据
    paint_opinion_h1n1_sick_from_vacc = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_h1n1_sick_from_vacc_ylabel_h1n1_ratio": opinion_h1n1_sick_from_vacc_ylabel_h1n1_ratio,
        "opinion_h1n1_sick_from_vacc_ylabel_season_ratio": opinion_h1n1_sick_from_vacc_ylabel_season_ratio}

    # 图4的json数据
    paint_opinion_seas_vacc_effective = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_seas_vacc_effective_ylabel_h1n1_ratio": opinion_seas_vacc_effective_ylabel_h1n1_ratio,
        "opinion_seas_vacc_effective_ylabel_season_ratio": opinion_seas_vacc_effective_ylabel_season_ratio}
    # 图5的json数据
    paint_opinion_seas_risk = {
        "x_label": x_label,
        "y_label": y_label,
        "opinion_seas_risk_ylabel_h1n1_ratio": opinion_seas_risk_ylabel_h1n1_ratio,
        "opinion_seas_risk_ylabel_season_ratio": opinion_seas_risk_ylabel_season_ratio}
    all_paint = {
        "paint_opinion_h1n1_vacc_effective": paint_opinion_h1n1_vacc_effective,
        "paint_opinion_h1n1_risk": paint_opinion_h1n1_risk,
        "paint_opinion_h1n1_sick_from_vacc": paint_opinion_h1n1_sick_from_vacc,
        "paint_opinion_h1n1_sick_from_vacc": paint_opinion_h1n1_sick_from_vacc,
        "paint_opinion_seas_vacc_effective": paint_opinion_seas_vacc_effective,
        "paint_opinion_seas_risk": paint_opinion_seas_risk}

    return JsonResponse(all_paint)



# 执行自定SQL
def runSQL(request):
    #sql = request.POST.get('SQL')
    sql = "SELECT * FROM set_labels"
    # 执行自定SQL语句
    result = databaseMapper.databaseMapper().runSQL(sql)
    # result为二维列表类型
    result_json = [{'result':row} for row in result]
    #返回result_json,列表每行表示查询表的一行信息组成的字典，每行的格式为{'result':查询结果列表}
    print(result_json)
    return JsonResponse(result_json,safe=False)


