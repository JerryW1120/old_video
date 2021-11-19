import os
import matplotlib.pyplot as plt
import numpy as np


'''
返回值是三级列表
[ [[og_1,fixed_1], [og_2,fixed_2]...[og_7,fixed_7]]   [[], [], ...[]]   ...]

如果去掉大循环，每次返回一个二级列表，大循环需要自己设置
[[og_1,fixed_1], [og_2,fixed_2]...[og_7,fixed_7]]
'''
def input_pictures_with_pairs(dir_origin, dir_fixed):
    # 去掉大循环时，路径具体到场景的文件夹(D:\修复2分场景\\000109449 - 000109497)
    # 有大循环时，路径具体到总文件夹(D:\修复2分场景)

    files = os.listdir(dir_origin)
    files.sort()

    count = 0
    middle_list = []
    count_inside = count

    while count_inside - count < 7:
        pair_list = []
        pic_og = plt.imread(os.path.join(dir_origin, files[count_inside]))
        pic_fixed = plt.imread(os.path.join(dir_fixed, files[count_inside]))
        pic_og = np.array(pic_og)
        pic_fixed = np.array(pic_fixed)
        
        pair_list.append(pic_og)
        pair_list.append(pic_fixed)
        middle_list.append(pair_list)
        count_inside += 1

    
    return middle_list


'''
返回值是两个二级列表
[ [og_1, og_2, og_3, ... og_7], ...[] ]
[ [fixed_1, fixed_2, fixed_3, ... fixed_7], ...[] ]

如果去掉大循环，每次返回两个普通列表，大循环需要自己设置
[og_1, og_2, og_3, ... og_7]
[fixed_1, fixed_2, fixed_3, ... fixed_7]
'''
def input_pictures_with_two_lists(dir_origin, dir_fixed):
    # 去掉大循环时，路径具体到场景的文件夹(D:\修复2分场景\\000109449 - 000109497)
    # 有大循环时，路径具体到总文件夹(D:\修复2分场景)

    files = os.listdir(dir_origin)
    files.sort()

    count = 0


    og_list = []
    fixed_list = []
    count_inside = count

    while count_inside - count < 7:
        pic_og = plt.imread(os.path.join(dir_origin, files[count_inside]))
        pic_fixed = plt.imread(os.path.join(dir_fixed, files[count_inside]))
        pic_og = np.array(pic_og)
        pic_fixed = np.array(pic_fixed)
    
        og_list.append(pic_og)
        fixed_list.append(pic_fixed)
        count_inside += 1

 
    return og_list, fixed_list



           
        