import os
import read_pictures_like_vimeo_demo as ld
'''
a = ld.input_pictures_with_pairs('D:\原始2分场景\\000109449 - 000109497', 'D:\修复2分场景\\000109449 - 000109497')

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])

    print('\n')'''


two_lists = ld.input_pictures_with_two_lists('D:\修复2分场景', 'D:\修复2分场景')

print("\n", two_lists)

#print(two_lists[0] == two_lists[1])
#print(len(two_lists[0]))
f = open("index.txt", "w")


path_fixed = '修复2分场景/'

folders = os.listdir('D:\修复2分场景')
count = 0

for second_lists in two_lists:
    path_og = '修复2分场景/'
    path_og = os.path.join(path_og, folders[count]) + '/'
    for lists in second_lists:       
        for item in lists:
            item = path_og + item + ' '
            f.write(item)
        f.write('\n')

    count += 1



f.close()
