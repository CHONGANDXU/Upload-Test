"""
Clear the default ports for http and https protocols, 
and remove duplicates for URLs with different protocols.
"""

# 导入os模块
import os

# 获取当前工作目录
cwd = os.getcwd()
# 拼接文件路径
file_path = os.path.join(cwd, "Test_File_RW")

# 导入re模块
import re
import itertools
import urllib.parse

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
    parsed_url = urllib.parse.urlparse(url)
    # 如果URL协议为https，且有端口号443，则去除端口号，并添加到https_urls中
    if parsed_url.scheme == "https" and parsed_url.port == 443:
        new_url = re.sub(":443", "", url)
        https_urls.add(new_url)
    # 如果URL协议为http，且有端口号80，则去除端口号，并添加到http_urls中
    elif parsed_url.scheme == "http" and parsed_url.port == 80:
        new_url = re.sub(":80", "", url)
        http_urls.add(new_url)
    # 如果URL有其他端口号，则根据协议添加到相应的set集合中
    else:
        if url.startswith("https"):
            https_urls.add(url)
        elif url.startswith("http"):
            http_urls.add(url)
        else:
            other_urls.add(url)

# 打印三个set集合中的元素
print("The set of http URLs is:", http_urls)
print()
print("The set of https URLs is:", https_urls)
print()
print("The set of other URLs is:", other_urls)
print()

combine = itertools.product(http_urls, https_urls)

import itertools

# 生成http和https集合的所有可能组合
combine = itertools.product(http_urls, https_urls)

# 创建一个空集合用于存储只有协议不同的网址
different_protocol_urls = set()

# 检查每个组合中的网址是否只是协议不同
for subset in combine:
    http_url = subset[0]
    https_url = subset[1]

    # 检查网址是否只是协议不同
    if http_url[4:] == https_url[5:]:
        different_protocol_urls.add(http_url)

# 从http集合中删除只有协议不同的网址
http_urls.difference_update(different_protocol_urls)

# 重新打开文件，指定写入模式
file = open(file_path + "/non-duplicate.txt", "w")
# 遍历字典中的键
for url in http_urls:
    # 将键加上换行符写入文件
    file.write(url + "\n")

for url in https_urls:
    # 将键加上换行符写入文件
    file.write(url + "\n")

for url in other_urls:
    # 将键加上换行符写入文件
    file.write(url + "\n")
# 关闭文件
file.close()
