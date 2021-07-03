import numpy as np
import random
"""
#算法预处理
def yuchuli(data):
    new_data=[]
    for i in range(len(data)):
        line = []
        for j in range(len(data[i])):
            if((not(23<=j<=32))and(j!=35)and(j!=36)):
                line.append(data[i][j])
        new_data.append(line)
    return new_data


def yuchuli_test(data):
    new_data=[]
    for i in range(len(data)):
        line = []
        for j in range(len(data[i])):
            if((not(22<=j<=31))and(j!=34)and(j!=35)):
                line.append(data[i][j])
        new_data.append(line)
    return new_data


import numpy as np
"""

# 算法预处理
def yuchuli(data):
    new_data = []
    for i in range(len(data)):
        line = []
        for j in range(len(data[i])):
            if ((not (23 <= j and j <= 32)) and (j != 35) and (j != 36)):
                line.append(data[i][j])
            elif j == 23:
                line.append(int(data[i][j][0]))
            elif j == 24:
                line.append(handleEducation(data[i][j]))
            elif j == 25:
                line.append(handleRace(data[i][j]))
            elif j == 26:
                line.append(handleSex(data[i][j]))
            elif j == 27:
                line.append(handleIncome(data[i][j]))
            elif j == 28:
                line.append(handleMaritalStatus(data[i][j]))
            elif j == 29:
                line.append(handleRentOrOwn(data[i][j]))
            elif j == 30:
                line.append(handleEmployment(data[i][j]))
            elif j == 31:
                line.append(handleHGR(data[i][j]))
            elif j == 32:
                line.append(handleCensus(data[i][j]))
            elif j == 35:
                line.append(handleIndustry(data[i][j]))
            elif j == 36:
                line.append(handleOccupation(data[i][j]))
        new_data.append(line)
    return new_data


def yuchuli_test(data):
    new_data = []
    for i in range(len(data)):
        line = []
        for j in range(len(data[i])):
            if ((not (22 <= j and j <= 31)) and (j != 34) and (j != 35)):
                line.append(data[i][j])
            elif j == 22:
                line.append(int(data[i][j][0]))
            elif j == 23:
                line.append(handleEducation(data[i][j]))
            elif j == 24:
                line.append(handleRace(data[i][j]))
            elif j == 25:
                line.append(handleSex(data[i][j]))
            elif j == 26:
                line.append(handleIncome(data[i][j]))
            elif j == 27:
                line.append(handleMaritalStatus(data[i][j]))
            elif j == 28:
                line.append(handleRentOrOwn(data[i][j]))
            elif j == 29:
                line.append(handleEmployment(data[i][j]))
            elif j == 30:
                line.append(handleHGR(data[i][j]))
            elif j == 31:
                line.append(handleCensus(data[i][j]))
            elif j == 34:
                line.append(handleIndustry(data[i][j]))
            elif j == 35:
                line.append(handleOccupation(data[i][j]))
        new_data.append(line)
    return new_data


def handleRace(race):
    if race == 'White':
        return 0
    elif race == 'Black':
        return 1
    elif race == 'Other or Multiple':
        return 2
    elif race == 'Hispanic':
        return 3
    else:
        return 4


def handleSex(sex):
    if sex == 'Female':
        return 0
    elif sex == 'Male':
        return 1
    else:
        return 2


def handleIncome(income):
    if income == '<= $75,000, Above Poverty':
        return 0
    elif income == '> $75,000':
        return 1
    elif income == 'Below Poverty':
        return 2
    else:
        return 3


def handleMaritalStatus(status):
    if status == 'Not Married':
        return 0
    elif status == 'Married':
        return 1
    else:
        return 2


def handleRentOrOwn(roo):
    if roo == 'Rent':
        return 0
    elif roo == 'Own':
        return 1
    else:
        return 2


def handleEducation(education):
    if education == '< 12 Years':
        return 0
    elif education == '12 Years':
        return 1
    elif education == 'College Graduate':
        return 2
    elif education == 'Some College':
        return 3
    else:
        return 4


def handleEmployment(employment):
    if employment == 'Not in Labor Force':
        return 0
    elif employment == 'Employed':
        return 1
    elif employment == 'Unemployed':
        return 2
    else:
        return 3


def handleHGR(hgr):
    if hgr == 'oxchjgsf':
        return 0
    elif hgr == 'bhuqouqj':
        return 1
    elif hgr == 'qufhixun':
        return 2
    elif hgr == 'lrircsnp':
        return 3
    elif hgr == 'atmpeygn':
        return 4
    elif hgr == 'lzgpxyit':
        return 5
    elif hgr == 'fpwskwrf':
        return 6
    elif hgr == 'mlyzmhmf':
        return 7
    elif hgr == 'dqpwygqj':
        return 8
    elif hgr == 'kbazzjca':
        return 9
    else:
        return 0

def make_up(dict):
    dict[0].append(int(dict[0][0])/2 + 0.5 * random.random())
    dict[0].append(int(dict[0][1])/2 + 0.5 * random.random())
    return dict

def handleCensus(census):
    if census == 'Non-MSA':
        return 0
    elif census == 'MSA, Not Principle  City':
        return 1
    elif census == 'MSA, Principle City':
        return 2
    else:
        return 0


def handleIndustry(industry):
    if industry == 'pxcmvdjn':
        return 0
    elif industry == 'rucpziij':
        return 1
    elif industry == 'wxleyezf':
        return 2
    elif industry == 'saaquncn':
        return 3
    elif industry == 'xicduogh':
        return 4
    elif industry == 'ldnlellj':
        return 5
    elif industry == 'wlfvacwt':
        return 6
    elif industry == 'nduyfdeo':
        return 7
    elif industry == 'fcxhlnwr':
        return 8
    elif industry == 'vjjrobsf':
        return 9
    elif industry == 'arjwrbjb':
        return 10
    elif industry == 'atmlpfrs':
        return 11
    elif industry == 'msuufmds':
        return 12
    elif industry == 'xqicxuve':
        return 13
    elif industry == 'phxvnwax':
        return 14
    elif industry == 'dotnnunm':
        return 15
    elif industry == 'mfikgejo':
        return 16
    elif industry == 'cfqqtusy':
        return 17
    elif industry == 'mcubkhph':
        return 18
    elif industry == 'haxffmxo':
        return 19
    elif industry == 'qnlwzans':
        return 20
    else:
        return 20


def handleOccupation(occupation):
    if occupation == 'xgwztkwe':
        return 0
    elif occupation == 'xtkaffoo':
        return 1
    elif occupation == 'emcorrxb':
        return 2
    elif occupation == 'vlluhbov':
        return 3
    elif occupation == 'xqwwgdyp':
        return 4
    elif occupation == 'ccgxvspp':
        return 5
    elif occupation == 'qxajmpny':
        return 6
    elif occupation == 'kldqjyjy':
        return 7
    elif occupation == 'mxkfnird':
        return 8
    elif occupation == 'hfxkjkmi':
        return 9
    elif occupation == 'bxpfxfdn':
        return 10
    elif occupation == 'ukymxvdu':
        return 11
    elif occupation == 'cmhcxjea':
        return 12
    elif occupation == 'haliazsg':
        return 13
    elif occupation == 'dlvbwzss':
        return 14
    elif occupation == 'xzmlyyjv':
        return 15
    elif occupation == 'oijqvulv':
        return 16
    elif occupation == 'rcertsgn':
        return 17
    elif occupation == 'tfqavkke':
        return 18
    elif occupation == 'hodpvpew':
        return 19
    elif occupation == 'uqqtjvyb':
        return 20
    elif occupation == 'pvmttkik':
        return 21
    elif occupation == 'dcjcmpih':
        return 22
    else:
        return 22

