import os
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.utils import who
from skimage.metrics import peak_signal_noise_ratio

dir_origin = "D:\原始2分场景"
dir_fixed = "D:\修复2分场景"
folders = os.listdir(dir_origin)
folders.sort()

'''
读取各个场景下的文件夹
'''
for folder in folders:
        files = os.listdir(dir_origin + '\\' + folder)
        files.sort()

'''
返回值是三级列表
[[  [og_1,fixed_1], [og_2,fixed_2]...[og_7,fixed_7]  ...]   []   ...]
'''
def input_pictures_with_pairs():
    
        count = 0

        whole_list = []
        while count <= len(files) - 7:
            temp_list = []
            count_inside = 0

            while count_inside < 7:
                pair_list = []
                pic_og = plt.imread(os.path.join(dir_origin, folder, files[count]))
                pic_fixed = plt.imread(os.path.join(dir_fixed, folder, files[count]))
                pic_og = np.array(pic_og)
                pic_fixed = np.array(pic_fixed)
                
                pair_list.append(pic_og)
                pair_list.append(pic_fixed)
                temp_list.append(pair_list)
                count_inside += 1

            whole_list.append(temp_list)
            count += 1
        
        return whole_list
'''
返回值是两个二级列表
[]
'''
def input_pictures_with_two_lists():

        count = 0

        whole_og_list = []
        whole_fixed_list = []
        while count <= len(files) - 7:
            og_list = []
            fixed_list = []
            count_inside = 0

            while count_inside < 7:
                pic_og = plt.imread(os.path.join(dir_origin, folder, files[count]))
                pic_fixed = plt.imread(os.path.join(dir_fixed, folder, files[count]))
                pic_og = np.array(pic_og)
                pic_fixed = np.array(pic_fixed)
            
                og_list.append(pic_og)
                fixed_list.append(pic_fixed)
                count_inside += 1

            whole_og_list.append(og_list)
            whole_fixed_list.append(fixed_list)

            count += 1
        
        return whole_og_list, whole_fixed_list

#如果要每7个7个输入网络的话，去掉大循环即可


           
        