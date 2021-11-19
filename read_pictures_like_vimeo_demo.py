import os
import matplotlib.pyplot as plt
import numpy as np


dir_origin = "D:\原始2分场景\\000109449 - 000109497"
dir_fixed = "D:\修复2分场景\\000109449 - 000109497"
files = os.listdir(dir_origin)
files.sort()

'''
读取各个场景下的文件夹
'''
# for folder in folders:
#         files = os.listdir(dir_origin + '\\' + folder)
#         files.sort()

'''
返回值是三级列表
[ [[og_1,fixed_1], [og_2,fixed_2]...[og_7,fixed_7]]   [[], [], ...[]]   ...]
'''
def input_pictures_with_pairs():
    
        count = 0

        whole_list = []
        while count <= len(files) - 7:
            middle_list = []
            count_inside = count

            while count_inside - count < 7:
                pair_list = []
                # pic_og = plt.imread(os.path.join(dir_origin, folder, files[count]))
                # pic_fixed = plt.imread(os.path.join(dir_fixed, folder, files[count]))
                # pic_og = np.array(pic_og)
                # pic_fixed = np.array(pic_fixed)
                
                pair_list.append(files[count_inside])
                pair_list.append(files[count_inside])
                middle_list.append(pair_list)
                count_inside += 1

            whole_list.append(middle_list)
            count += 1
        
        return whole_list
'''
返回值是两个二级列表
[[og_1, og_2, og_3, ... og_7], ...[] ]
[[fixed_1, fixed_2, fixed_3, ... fixed_7], ...[]]
'''
def input_pictures_with_two_lists():

        count = 0

        whole_og_list = []
        whole_fixed_list = []
        while count <= len(files) - 7:
            og_list = []
            fixed_list = []
            count_inside = count

            while count_inside - count < 7:
                # pic_og = plt.imread(os.path.join(dir_origin, folder, files[count]))
                # pic_fixed = plt.imread(os.path.join(dir_fixed, folder, files[count]))
                # pic_og = np.array(pic_og)
                # pic_fixed = np.array(pic_fixed)
            
                og_list.append(files[count_inside])
                fixed_list.append(files[count_inside])
                count_inside += 1

            whole_og_list.append(og_list)
            whole_fixed_list.append(fixed_list)

            count += 1
        
        return whole_og_list, whole_fixed_list

#如果要每7个7个输入网络的话，去掉大循环即可

#print("成对儿返回得到的列表就是：",input_pictures_with_pairs())
a = input_pictures_with_pairs()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
    
    print('\n')


#two_lists = input_pictures_with_two_lists()
#print("\n直接返回两个列表是：", two_lists[0])
#print("\n", two_lists[1])
           
        