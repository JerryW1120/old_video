import os
import shutil

def copyfile(sourcefile, destanationfile):
    if not os.path.isfile(sourcefile):
        print ("%s not exist!"%(sourcefile))
    else:
        shutil.move(sourcefile, destanationfile)          # 复制文件
        print ("copy %s -> %s" % (sourcefile, destanationfile))


output_directory = "G:\原始1png\\"
address = []
i = 1
while i <= 95:
    address.append("G:\原始1png\场景" + str(i))
    i += 1


for dir in address:
    for file in os.listdir(dir):
        copyfile(dir + '\\' + str(file), output_directory + str(file))

print("finish")