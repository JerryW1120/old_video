import os


path = "D:\\"
dirs = []
count = 1000000
while count <= 7946377:
    dirs.append(path + str(count))
    print(count)
    count += 1

for dir in dirs:
    if os.path.isdir(dir):
        os.removedirs(dir)
        print("%s目录 已删除" % dir)

print("finish")
