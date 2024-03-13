# 查询当前系统所有字体
import matplotlib.font_manager as font_manager

print("all font list get from matplotlib.font_manager:")

for f in sorted(font_manager.get_font_names()):
    print(f)
