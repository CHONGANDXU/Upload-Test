import math
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置中文字体
plt.rcParams["font.family"] = ""

# 读取Excel文件并指定第一行为列索引
data = pd.read_excel("your dataset path here!!!", header=0)

# 将空值替换为 NaN
data = data.fillna(np.nan)

# 将表格转换为字典形式
data = data.to_dict("list")

# 将所有数据转换为数值型，并删除大于80的值
for key in data.keys():
    data[key] = pd.to_numeric(data[key], errors="coerce")
    # data[key] = [x for x in data[key] if not math.isnan(x) and x <= 6.1]

# 删除字典中的NaN值
for key in data.keys():
    data[key] = [x for x in data[key] if not math.isnan(x)]

# 标签
labels = list(data.keys())

# 生成颜色列表
colors = [
    "#FFC107",
    "#FF9800",
    "#FF5722",
    "#F44336",
    "#E91E63",
    "#9C27B0",
    "#673AB7",
    "#3F51B5",
    "#2196F3",
    "#03A9F4",
    "#00BCD4",
    "#009688",
    "#4CAF50",
    "#8BC34A",
    "#CDDC39",
    "#FFEB3B",
    "#FFC107",
    "#FF9800",
    "#FF5722",
    "#795548",
    "#9E9E9E",
    "#607D8B",
    "#E65100",
    "#FFD600",
    "#1E88E5",
    "#6D4C41",
    "#C2185B",
    "#7CB342",
    "#039BE5",
    "#F9A825",
    "#5D4037",
    "#AFB42B",
    "#E53935",
    "#43A047",
    "#FDD835",
    "#00897B",
    "#D81B60",
    "#00ACC1",
    "#F4511E",
    "#546E7A",
    "#3949AB",
    "#FFA726",
    "#7E57C2",
    "#C0CA33",
    "#FF7043",
    "#FFEE58",
    "#26A69A",
    "#5E35B1",
]

# 设置绘图参数
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制箱线图
positions = list(range(1, len(labels) + 1))
for i in range(len(labels)):
    ax.boxplot(
        data[labels[i]],
        positions=[positions[i]],
        widths=0.6,
        showfliers=False,
        patch_artist=True,
        boxprops={"color": "black", "facecolor": colors[i], "alpha": 0.7},
        capprops={"color": "black"},
        whiskerprops={"color": "black"},
        medianprops={"color": "white"},
    )

# 绘制数据点
for i, label in enumerate(labels):
    ax.scatter(
        np.ones(len(data[label])) * positions[i],
        data[label],
        alpha=0.5,
        s=30,
        color=colors[i],
    )

# 设置横纵坐标标签
ax.set_xticks(positions)
ax.set_xticklabels(labels, fontsize=9.8, rotation=45, ha="right")
ax.set_ylabel("Cd (mg/kg)", fontsize=16)

# 添加水平线
ax.axhline(y=1, color="r", linestyle="--", linewidth=1)

# 设置y轴刻度为整数
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# 调整子图间距和边距
fig.tight_layout(pad=2, w_pad=1.5, h_pad=1)

# 显示图形
plt.show()
