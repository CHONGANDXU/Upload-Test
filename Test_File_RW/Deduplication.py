# 导入os模块
import os

# 获取当前工作目录
cwd = os.getcwd()
# 拼接文件路径
file_path = os.path.join(cwd, 'Test_File_RW')

# 导入re模块
import re

# 打开文件
row = open(file_path+"/tracker_https.txt", "r")
# 获取所有行的列表
lines = row.readlines()
# 关闭文件
row.close()

# 创建一个正则表达式对象，用于匹配url地址中的端口号443
pattern = re.compile(r":443")

# 创建一个空的set集合
urls = set()
# 遍历每一行
for line in lines:
    # 去除换行符
    line = line.strip()
    # 进行正则表达式匹配
    new_line=pattern.sub("",line)
    urls.add(new_line)

urls = sorted(urls)

for i in urls:
    print(i)

# 重新打开文件，指定写入模式
file = open(file_path+"/non-duplicate.txt", "w")
# 遍历字典中的键
for url in urls:
    # 将键加上换行符写入文件
    file.write(url + "\n")
# 关闭文件
file.close()

