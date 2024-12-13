

#pip install matplotlib

### 2. 编写Python代码绘制图像

import numpy as np
import matplotlib.pyplot as plt

# 生成x轴的数据范围，这里我们设置从-10到10，间隔为0.1
x = np.arange(-10, 10, 0.1)

# 计算一次函数对应的y值，这里以y = y_linear = -2 * x + 8为例
y_linear = -2 * x + 8
# 计算二次函数对应的y值，这里以y = x ** 2 + 2 * x + 3为例
y_quadratic = x ** 2 + 2 * x + 3

# 绘制一次函数图像，设置标签、颜色等属性
plt.plot(x, y_linear, label='y = -2 * x + 8', color='r')

# 绘制二次函数图像，设置标签、颜色等属性
plt.plot(x, y_quadratic, label='y = x ** 2 + 2 * x + 3', color='b')

# 添加标题
plt.title("Graph of Linear and Quadratic Functions")

# 添加x轴标签
plt.xlabel('x')

# 添加y轴标签
plt.ylabel('y')

# 添加图例，用于区分不同函数的图像
plt.legend()

# 显示网格，使图像更清晰直观
plt.grid(True)

# 显示图像
plt.show()


