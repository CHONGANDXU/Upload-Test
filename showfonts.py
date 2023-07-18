# 查询当前系统所有字体
from matplotlib.font_manager import FontManager
 
mac_fonts = set(f.name for f in FontManager().ttflist)
 
print('all font list get from matplotlib.font_manager:')
for f in sorted(mac_fonts):
    print('\t' + f)