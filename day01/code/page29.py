# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="D:\\迅雷下载\\2-1Q22FT622\\罗西钢笔行楷.ttf")

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(11,31)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font)
#绘制网格
plt.yticks(range(0,9))

#绘制网格 alpha=0.1透明度
plt.grid(alpha=0.5)

#展示
plt.show()
