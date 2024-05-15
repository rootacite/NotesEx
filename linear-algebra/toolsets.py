import numpy as np
import matplotlib.pyplot as plt
import math

def draw_pic():
    # 生成数据

    # 创建图像和子图
    fig, ax = plt.subplots()

    # 绘制曲线
    ax.quiver(0, 0, 2, 5, angles='xy', scale_units='xy', scale=1,color='blue')
    ax.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1,color='red')
   
    ax.quiver(1, 1, 2, 5, angles='xy', scale_units='xy', scale=1,color='blue')
    ax.quiver(2, 5, 1, 1, angles='xy', scale_units='xy', scale=1,color='red')
   
    # 移动坐标轴到图像中心
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    #ax.set_aspect('equal')

    # 隐藏原始的坐标轴刻度
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.set_xlim([-6.5,6.5])
    ax.set_ylim([-6.5,6.5])

    plt.show()

A = np.array([
    [0,-1,0],
    [0,2,-1],
    [-1,0,2]
])

print(np.linalg.det(A))