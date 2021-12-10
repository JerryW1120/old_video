import os
import read_pictures_like_vimeo_demo as ld



two_lists = ld.input_pictures_with_two_lists('D:修复2分场景', 'D:\修复2分场景')

print("\n", two_lists)

#print(two_lists[0] == two_lists[1])
#print(len(two_lists[0]))
f = open("index.txt", "w")


path_fixed = 'fixed2/'

folders = os.listdir('D:\原始2分场景')
count = 0

for second_lists in two_lists:
    path_og = 'fixed2/'
    path_og = os.path.join(path_og, folders[count]) + '/'
    for lists in second_lists:       
        for item in lists:
            item = path_og + item + ' '
            f.write(item)
        f.write('\n')

    count += 1