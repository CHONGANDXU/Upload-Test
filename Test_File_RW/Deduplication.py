# 导入os模块
import os

# 获取当前工作目录
cwd = os.getcwd()
# 拼接文件路径
file_path = os.path.join(cwd, 'Test_File_RW')

# 导入re模块
import re
import itertools

# 打开文件
row = open(file_path + "/tracker_best.txt", "r")
# 获取所有行的列表
lines = row.readlines()
# 关闭文件
row.close()

# 创建一个空的set集合
all_urls = set()
# 遍历每一行
for line in lines:
    # 去除换行符
    line = line.strip()
    all_urls.add(line)

http_urls = set()
https_urls = set()
other_urls = set()

# 遍历set集合中的每个URL
for url in all_urls:
    # 如果URL以https开头，且有端口号443，则去除端口号，并添加到https_urls中
    if url.startswith('https') and ':443' in url:
        new_url = re.sub(':443', '', url)
        https_urls.add(new_url)
    # 如果URL以http开头，且有端口号80，则去除端口号，并添加到http_urls中
    elif url.startswith('http') and ':80' in url and ':8080' not in url:
        new_url = re.sub(':80', '', url)
        http_urls.add(new_url)
    # 如果URL有其他端口号，则根据协议添加到相应的set集合中
    else:
        if url.startswith('https'):
            https_urls.add(url)
        elif url.startswith('http'):
            http_urls.add(url)
        else:
            other_urls.add(url)

# 打印三个set集合中的元素
print("The set of http URLs is:", http_urls)
print("The set of https URLs is:", https_urls)
print("The set of other URLs is:", other_urls)

combine = itertools.product(http_urls, https_urls)

# for subset in combine:  # 遍历每个子集
#     print(subset[0])
#     print(subset[1])

# # 重新打开文件，指定写入模式
# file = open(file_path+"/non-duplicate.txt", "w")
# # 遍历字典中的键
# for url in urls:
#     # 将键加上换行符写入文件
#     file.write(url + "\n")
# # 关闭文件
# file.close()
