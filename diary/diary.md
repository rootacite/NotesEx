
# May

## 4th

* 高斯消元法求逆矩阵
* 矩阵的三角化、对角化、归一化
* 矩阵的转置运算法则
* 矩阵的$A=LU$分解
* (回顾)微分的定义
* 置换矩阵

### 总结: 问心无愧


## 5th

* 矩阵消元行置换算法
* 线性空间初步 运算律
* 矩阵的行列操作算法
* 模板+lamba表达式配合使用

### 总结: 问心无愧

## 6th

* 三角恒等
* $x \to \infty$时求极限的思路
* 介值定理、极值
* 递归思路求导
* 求导的乘积公式与链式法则的证明
* 隐函数与相关变化率
* 向量空间(列空间)
* 三角化算法、对角化算法、归一化算法

### 总结: 问心无愧

## 7th

* 向量空间(零空间)
* $Ax=0$的解法
* 长方矩阵的消元与矩阵的秩
* 行列式的性质
* 行列式的几何定义
* 行列式的解法
* 行列式的基本类型

### 总结: 问心无愧

## 8th

* 复利问题与第一个重要极限
* 码制——补码的运算
* 码制——移码与定点小数

## 9th

* 微分中值定理、导数的应用
* 函数的零点判断
* 补码溢出判断

### 总结: 问心无愧

## 10th

* 最优化问题
* 函数的线性化估值
* 牛顿法解方程

```cpp
typedef double(*UnaryFunction)(double);

template<typename T>
double derivative(T fun, double x, double dx = 0.000001)
{
    double y1 = fun(x), y2 = fun(x + dx);
    return (y2 - y1) / dx;
}

template<typename T>
double solve(T fun, double value, double begin, double diff = 0.000001)
{
    double result = begin;
    while(true)
    {
        double ly = fun(result);
        if(abs(ly - value) <= diff) return result;
        double dy = value - ly;
        double dx = dy / derivative(fun, result);
        result += dx;
    }
}
```

* 原码的乘法运算
* 补码的乘法运算 (Booth算法)

### 总结: 问心无愧

## 11th

* 原码与补码的除法运算
* 浮点数的表示与IEEE格式
* 定积分
* 微积分第一基本定理

### 总结: 问心无愧

## 12th

* 积分表示法

## 13th

* 定积分——第一类换元法
* 定积分——分部积分法
* 李林880(1,2,3)

### 总结: 问心无愧

## 14th

* 浮点数
* IEEE
* 移码深入
* 泰勒展开(公式)
* 分部积分法初步

### 总结: 问心无愧

## 15th

* 分部积分法深入(列表法)
* 数列初步
* 李林(4, 5)
* 浮点数的运算
* 海涅定理

### 总结: 问心无愧

## 16th

* 数列深入(夹逼准则)
* 放缩法与重要不等式
* 单调有界定理
* 压缩映射原理

### “因为徐畅开了三个小时会，今天差点问心有愧”

## 17th

* 李林 (8,9)
* 中值定理深入
* 零点、临界点、极值点、反曲点
* SRAM、DRAM、ROM

### 总结: 问心无愧

## 18th

* 多体存储器
* 数据结构(树、图)复习
* 李林(9)

### 总结: 问心无愧

## 19th

* 数据结构可视化初步

## 20th

* 数据可视化: Dragable
* 数据可视化: Connection
* 数据可视化: TreeNode
* 李林 (10)
* OCL电路修复

### 总结: 问心无愧

## 21th

* HHD、SSD
* Cache
* 修复电路 (失败)

## 22th

* Cache 深入
* 李林 (11)
* 修复电路 (成功) 明天消振

## 23th

* 电路消振
* 单声道修复成功

## 24th

* 电路修复完全成功
* Cache深入(三种映射方式)
* Cache替换策略
* Cache写策略
* 互斥&同步&前驱(复习)

### 总结: 问心无愧

## 25th

* 页式存储
* 虚拟内存
* 指令系统
* 指令编码概述
* 指令格式
* 扩展操作码
* 指令寻址
* 数据访问概述

### 总结: 问心无愧

## 26th

* 汇编语言(复习)
* CPU

## 27th

### PLC实习 问心有愧

## 28th

### PLC实习 问心有愧

## 29th

### PLC实习 问心有愧

## 30th

### PLC实习 问心有愧

## 31th

* 李林(12)
* 控制器(CU)
* 指令周期流程

# June

## 1th

* 数据通路
* 硬布线控制器
* 微命令与微操作

## 2th

* 机器周期 II
* 操作码译码器
* 硬布线三原则

## 3th

* PLC基础

## 4th

* PLC基础

## 5th

* 计网3.4

## 6th

* 计算机网络深入(数据链路)

## 7th & 8th

* 可靠数据传输协议的构建(完成)
* 速率与时延与吞吐量
* 流水线传输初步

## 9th

* TCP链接
* 回退N步(GBN)协议
* 选择重发(SR)
* TCP报文段结构

## 10th

* TCP 抓包实验

## 11th

* LWIP Socket DGRAM
* LWIP 多路复用
* UDP广播

## 12th

* stm32h7 ETH外设
* stm32h7 DCache
* MPU
* stm32h7 Cache与DMA冲突的解决

## 13th->17th

* Unity

## 18th->30th

* 模电课设

# July

# 15th

* 中值定理回顾
* 计算机系统：内存布局深入
* Bluetooth技术HID

# 16th

* 中值定理回顾2
* 第一类换元回顾
* GTK 4 学习开始
* Cairo 学习开始
* 深入理解Git分支管理
* 难题 6.5

# 17th


* 魔改MicroPython源码
* esp-joy

# 18th