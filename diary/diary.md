
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

# 12th

* 积分表示法

# 13th

* 定积分——第一类换元法
* 定积分——分部积分法
* 李林880(1,2,3)

### 总结: 问心无愧

# 14th

* 浮点数
* IEEE
* 移码深入
* 泰勒展开(公式)
* 分部积分法初步

### 总结: 问心无愧

# 15th

* 分部积分法深入(列表法)
* 数列初步
* 李林(4, 5)
* 浮点数的运算
* 海捏定理