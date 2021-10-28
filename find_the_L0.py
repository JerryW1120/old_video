import os
dir1 = "G:\修复2png"
dir2 = "G:\修复2"

def compare(dir):
    list_fold = []
    files = os.listdir(dir)
    files.sort()

    for file in files:
        if dir == "G:\修复2png":
            number = str(file).split(".")[0]
        else:
            number = str(file).split(".")[1]
        list_fold.append(number)
    list_fold.sort()
    return list_fold

fold1 = compare(dir1)
fold2 = compare(dir2)


print(fold1 == fold2)
# count = 0
# for file in files:
#     number1 = str(files[count]).split(".")[0]
#     number2 = str(files[count + 1]).split(".")[0]
#     if number2 == 'L0':
#         count += 2
#         continue
#     else:
#         if int(number2) - int(number1) != 1:
#             print("the number is", number1)
#             break
#         else:
#             count += 1
#     print(count)       
