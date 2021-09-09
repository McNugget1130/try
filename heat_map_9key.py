import pdfplumber
import pinyin
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# 提取pdf文件中文章的拼音

file_path = r'D:\……\共产党宣言.pdf'

article_pinyin = ''        # 全文拼音

with pdfplumber.open(file_path) as pdf:
    for page in pdf.pages:        # 对pdf文件中的每一页
        text = page.extract_text()        # 提取当前页的文字
        page_pinyin = pinyin.get(text, format='strip')        # 将汉字文本转化为拼音
        article_pinyin = article_pinyin + page_pinyin        # 把每一页的拼音连在一起


# count()函数统计各字符的出现次数

n = {}
for i in article_pinyin:
    n[i] = article_pinyin.count(i)


# 构建类似键盘分布的3行3列二维数组，手动将数组的每个元素与26个字母的出现次数一一对应

data = [[0 for i in range(1,4)] for j in range(1,4)]

# 键盘第一行
data[0][1] = n['a'] + n['b'] + n['c']
data[0][2] = n['d'] + n['e'] + n['f']

# 键盘第二行
data[1][0] = n['g'] + n['h'] + n['i']
data[1][1] = n['j'] + n['k'] + n['l']
data[1][2] = n['m'] + n['n'] + n['o']

# 键盘第三行
data[2][0] = n['p'] + n['q'] + n['r'] + n['s']
data[2][1] = n['t'] + n['u'] + n['v']
data[2][2] = n['w'] + n['x'] + n['y'] + n['z']


# 计算均衡性(标准差)

arr = [data[0][1],data[0][2],
       data[1][0],data[1][1],data[1][2],
       data[2][0],data[2][1],data[2][2]]
print("Homogeneity of key use:", np.std(arr))


# 绘制热力图

sns.heatmap(data, cmap = 'PuBuGn', annot = True, fmt = '.0f')

#sns.heatmap(data,        # 矩阵数据集
#            vmin = None,        # 颜色取值最小范围
#            vmax = None,        # 颜色取值最大范围
#            cmap = None,        # 填充色
#            center = None,        # 设置色彩中心对齐值，可以调整生成的图像颜色的整体深浅
#            robust = False,        # 如果是False，且没设定vmin和vmax的值，
#            # 热力图的颜色映射范围根据具有鲁棒性的分位数设定，而不是用极值设定。
#            annot = False,        # 默认取值False；如果为True，就在热力图的每个单元上显示数值
#            fmt = '.2g',        # 矩阵上标识数字的数据格式，比如保留小数点后几位数字
#            annot_kws = False,        # 默认取值False；如果为True，设置热力图矩阵上数字的大小颜色字体
#            linewidths = 0,        # 定义热力图里“表示两两特征关系的矩阵小块”之间的间隔大小
#            linecolor = 'white',        # 切分热力图上每个矩阵小块的线的颜色，默认值是’white’
#            cbar = True,        # 是否在热力图侧边绘制颜色刻度条，默认值是True
#            cbar_kws = None,        # 热力图侧边绘制颜色刻度条时，相关字体设置，默认值是None
#            cbar_ax = None,        # 热力图侧边绘制颜色刻度条时，刻度条位置设置，默认值是None
#            square = False,        # 设置热力图矩阵小块形状，默认值是False
#            xticklabels = 'auto',        # 控制每列标签名的输出，默认值是auto
#            yticklabels = 'auto',        # 控制每行标签名的输出，默认值是auto
#            # 如果是True，则以DataFrame的列名作为标签名
#            # 如果是False，则不添加行标签名
#            # 如果是列表，则标签名改为列表中给的内容
#            # 如果是整数K，则在图上每隔K个标签进行一次标注
#            # 如果是auto，则自动选择标签的标注间距，将标签名不重叠的部分(或全部)输出
#            mask = None,        # 控制某个矩阵块是否显示出来，默认值是None
#            ax = None,        # 设置作图的坐标轴
#            **kwargs)        # 所有其他关键字参数都传递给ax.pcolormesh

# 添加标题
plt.title('Heat map of the use of the 9-key recording the Communist Manifesto')

# 显示图形
plt.show()
