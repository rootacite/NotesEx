
# 线性代数

## 线性代数与线性方程组

对于线性方程组:&emsp; $\begin{cases}
\begin{aligned}
2x - y  &= 0\\
-x + 2y &= 3
\end{aligned}
\end{cases}$ &emsp;我们可以根据各个行的系数，将它转换为一个矩阵算式:
$$\begin{bmatrix}
2  & -1\\
-1 & 2
\end{bmatrix} \begin{bmatrix}
x \\
y
\end{bmatrix} = \begin{bmatrix}
0 \\
3
\end{bmatrix}
$$

### Row Picture

顾名思义，我们逐行的关注这个方程组。针对它的每一行，我们可以在一个n维坐标系上画出一条直线，这也就是为什么它被称为 **"线性方程组"**。

![alt text](image.png)

### Column Picture

现在，让我们逐列地关注这个方程组。我们是否可以这样理解，2和-1乘以同一个变量x的结果，加上-1和2乘以同一个变量y的结果，等于0和3，随后我们可以列出一个矩阵。

$$x\begin{bmatrix}
2 \\
-1
\end{bmatrix} + y\begin{bmatrix}
-1 \\
2
\end{bmatrix} = \begin{bmatrix}
0 \\
3
\end{bmatrix}$$

从这个角度看，解线性方程组的问题被我们转化为了如何线性地组合两个向量，才能得到另一个向量的问题。

## 矩阵运算

### 矩阵与向量的乘法

$$\begin{bmatrix}
2 & 5 & 4 \\
1 & 1 & 8 \\
4 & 4 & 9
\end{bmatrix} \begin{bmatrix}
2\\
1\\
5
\end{bmatrix} = X$$

在上述的矩阵运算中，我们可以把列向量的三个分量分别乘以矩阵的每个列，从而得出：

$$2 \times \begin{bmatrix}
2\\
1\\
4
\end{bmatrix} + 1 \times \begin{bmatrix}
5\\
1\\
4
\end{bmatrix} + 5 \times \begin{bmatrix}
4\\
8\\
9
\end{bmatrix}  = X $$

如果换一种说法，算式$Ax$，可以看作矩阵$A$中各列的**线性组合**。

### 消元法

对于矩阵 $\begin{bmatrix}
1 & 2 & 1 \\
3 & 8 & 1 \\
0 & 4 & 1
\end{bmatrix}$ 它描述了一个三元一次方程组的左值: $\begin{cases}
\begin{aligned}
 x + 2y + z &= 2\\
3x + 8y + z &= 12\\
     4y + z &= 2
\end{aligned}
\end{cases}$ &emsp; 为了消去第二行的$x$变量，与第三行的$x$、$y$变量，我们进行如下运算:

首先，我们需要选择三个**主元**，他们不可以为0，这里我们选择行一的$x$、行二的$y$、以及行三的$z$作为主元。

对于第二行 $\begin{bmatrix}
3 & 8 & 1
\end{bmatrix}$ 我们需要将行一$\begin{bmatrix}
1 & 2 & 1
\end{bmatrix}$乘以-3后，与之相加：
$$\begin{bmatrix}
3 & 8 & 1
\end{bmatrix} - 3\times\begin{bmatrix}
1 & 2 & 1
\end{bmatrix} = \begin{bmatrix}
0 & 2 & -2
\end{bmatrix}$$ 然后我们得到了第二个矩阵
$$\begin{bmatrix}
1 & 2 & 1\\
0 & 2 & -2\\
0 & 4 & 1
\end{bmatrix}$$

正常来说，我们本来需要消去行三列一，但在这里，它原本就是0，我们就不需要另加处理了。而对于行三列二，我们可以用主元二将其消去。

$$\begin{bmatrix}
0 & 4 & 1
\end{bmatrix} - 2\times\begin{bmatrix}
0 & 2 & -2
\end{bmatrix} = \begin{bmatrix}
0 & 0 & 5
\end{bmatrix} $$

随后我们得到了第三个矩阵:

$$\begin{bmatrix}
1 & 2 & 1\\
0 & 2 & -2\\
0 & 0 & 5
\end{bmatrix} = U$$

它是一个上三角矩阵，其中(0, 0), (1, 1), (2, 2)为主元。

现在来考虑把右侧的$\begin{bmatrix}
2\\
12\\
2
\end{bmatrix}$ 也考虑在内的情况。我们可以把$\begin{bmatrix}
1 & 2 & 1 \\
3 & 8 & 1 \\
0 & 4 & 1
\end{bmatrix}$ 与 $\begin{bmatrix}
2\\
12\\
2
\end{bmatrix}$ 合并，得到一个新的矩阵 $$\begin{bmatrix}
1 & 2 & 1 & 2\\
3 & 8 & 1 & 12\\
0 & 4 & 1 & 2
\end{bmatrix} = Y$$ 这里$Y$被称为 **增广矩阵**，因为我们为它新增了一列。对这个将右值带入到一起的矩阵，对其消元的结果应当是 $$\begin{bmatrix}
1 & 2 & 1 & 2\\
0 & 2 & -2 & 6\\
0 & 0 & 5 & -10
\end{bmatrix} = C$$ 随后我们可以由此得出一个新的线性方程组: 

$$\begin{cases}
\begin{aligned}
 x + 2y +  z &= 2\\
     2y - 2z &= 6\\
          5z &= -10
\end{aligned}
\end{cases}$$

### Matrix Picture

现在让我们用矩阵的视角来看待前面的操作。首先，一个行向量乘以一个矩阵可以用以下的方法计算:

$$\begin{bmatrix}
x & y & z
\end{bmatrix}\begin{bmatrix}
x_1 & y_1 & z_1 \\
x_2 & y_2 & z_2 \\
x_3 & y_3 & z_3
\end{bmatrix} = x\begin{bmatrix}
x1 & y1 & z1
\end{bmatrix} + y\begin{bmatrix}
x2 & y2 & z2
\end{bmatrix} + z\begin{bmatrix}
x3 & y3 & z3
\end{bmatrix}$$

随后，我们思考，一个什么样的矩阵$M$作用在$\begin{bmatrix}
1 & 2 & 1 \\
3 & 8 & 1 \\
0 & 4 & 1
\end{bmatrix}$上可以实现让行二与-3倍的行一相加，让我们逐行来分析。对于我们想要的结果来说，我们不希望改变原矩阵的第一行与第三行。
换一种思路，我们想要的结果的第一行应当是1份操作数的第一行，以及0份第二行和第三行的线性组合。故而我们这样构造矩阵$M$的第一行: $\begin{bmatrix}
1 & 0 & 0
\end{bmatrix}$，同理，我们这样构造矩阵$M$的第三行: $\begin{bmatrix}
0 & 0 & 1
\end{bmatrix}$。

这里插入一句，假如我们这样构造矩阵$M$的第二行: $\begin{bmatrix}
0 & 1 & 0
\end{bmatrix}$ , 得到的矩阵$M$将会是 
$$\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}$$ 然而这个矩阵与任何三阶矩阵相乘的结果都是原矩阵，我们将这样的矩阵称为**单位矩阵**。
回到正题，我们这样构造我们的矩阵$M$

$$M = \begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}$$

这表示我们的结果矩阵的第二行，应当取-3份的原矩阵第一行，以及1份第二行进行线性组合。我们将$M$与原矩阵相乘：

$$\begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} \cdot \begin{bmatrix}
1 & 2 & 1 \\
3 & 8 & 1 \\
0 & 4 & 1
\end{bmatrix} = \begin{bmatrix}
1 & 2 & 1 \\
0 & 2 & -2 \\
0 & 4 & 1
\end{bmatrix}$$

这正是我们第一步消元后应该得到的结果。同理，我们将两次消元一并进行: 

$$\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -2 & 1
\end{bmatrix} \cdot \begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} \cdot \begin{bmatrix}
1 & 2 & 1 \\
3 & 8 & 1 \\
0 & 4 & 1
\end{bmatrix} = \begin{bmatrix}
1 & 2 & 1 \\
0 & 2 & -2 \\
0 & 0 & 5
\end{bmatrix}$$ 或者，我们将前两个矩阵优先计算，得到变换矩阵$M_T$: 

$$M_T = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -2 & 1
\end{bmatrix} \cdot \begin{bmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 0 \\
-1 & 1 & 0 \\
6 & -2 & 1
\end{bmatrix}$$ 显然，$M_T$就是能对原矩阵进行消元操作的变换矩阵。

### 置换矩阵

假设我们有矩阵$\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}$ 置换矩阵可以交换他们的行，从而得到$\begin{bmatrix}
c & d\\
a & b
\end{bmatrix}$，对于上述的矩阵，它的置换矩阵为$\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix}$，这不难理解。我们的输出矩阵的第一行取原矩阵的第二行，而第二行取原矩阵的第一行。
$$\begin{bmatrix}
0 & 1\\
1 & 0 \end{bmatrix} \begin{bmatrix}
a & b\\
c & d \end{bmatrix} = \begin{bmatrix}
c & d\\
a & b \end{bmatrix}$$

而如果将置换矩阵乘在原矩阵的后面， 它会将原矩阵的两列交换。

$$\begin{bmatrix}
a & b\\
c & d \end{bmatrix} \begin{bmatrix}
0 & 1\\
1 & 0 \end{bmatrix} = \begin{bmatrix}
b & a\\
d & c \end{bmatrix}$$

* 一个重要的意识 : 进行行操作时，变换矩阵左乘。进行列操作时，变换矩阵右乘。

### 逆矩阵

一个矩阵乘以它的逆矩阵等于单位矩阵。

$$E\cdot E^{-1} = I$$

### 矩阵乘法

简单来说，如果矩阵$A$，$B$相乘等于$C$，$C$中的某个元素可以用以下的算法得出

```cpp

int get_element_inresult(Matrix a, Matrix b, Point point)
{
     int r = 0;
     for(auto i : a.row(point.x))
          for(auto j : b.col(point.y))
          {
               r += i * j;
          }

     return r;
}
```

或者说，我们可以按照以下两种方式去理解矩阵乘法: 
* 取A的一行，以该行的每个元素作为权值，线性地组合B的每一行，得到的结果是C中的一行，位置与在A中相同

* 取B的一列，以该列的每个元素作为权值，线性地组合A的每一列，得到的结果是C中的一列，位置与在B中相同

这两种解释方法指向相同的结果。而从它们身上，我们可以得到两个信息:

1. A的列数必须等于B的行数。(因为我们根据A中某行的元素作为权值去组合B中的行)

2. A的行数决定了C的行数，B的列数决定了C的列数。(A有多少行就组合多少次，B有多少列就组合多少次)

### 奇异矩阵

为什么某些矩阵没有逆矩阵，换句话说，他们与任何一个矩阵相乘都不可能得到单位矩阵，我们先来看一个简单的例子: 

$$A = \begin{bmatrix}
1 & 2 & 4\\
4 & 8 & 16\\
3 & 6 & 12
\end{bmatrix}$$

这个矩阵就是一个奇异矩阵，它与任何矩阵相乘都得不到单位矩阵 $\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1 \end{bmatrix}$，但这是为什么？我们先来回忆一下矩阵的乘法，我们说A乘以任何矩阵都无法得到单位矩阵，实际上我们是在说什么呢？
答案是：无论我们如何线性地组合矩阵中的每一列，都无法得到$\begin{bmatrix}
1 \\
0 \\
0 \end{bmatrix}$、$\begin{bmatrix}
0 \\
1 \\
0 \end{bmatrix}$以及$\begin{bmatrix}
0 \\
0 \\
1 \end{bmatrix}$ 三个列向量。正常来说，取N个向量进行线性组合的结果，应该能铺满整个N维空间，但有些情况例外。比如这N的向量中的2个或多个共线。
于是我们再回过头来看一看矩阵$A$，果然是这样。
于是我们这样理解奇异矩阵: **如果我能找到一个非0向量$x$，使得$Ax=0$，则$A$为奇异矩阵**。这句话实际是在说如果我能通过线性地组合$A$中的向量而得到0向量，那就说明$A$中的某些列对线性组合毫无贡献，这会使它的线性组合的结果降维——这是灾难性的，至少会让我无法得到这个线性空间中的所有正交基矢。

### 高斯消元法求逆矩阵

首先我们需要弄清楚，当我们说要求一个矩阵的逆矩阵时，我们是在求什么。假设我们有矩阵$A$

$$A = \begin{bmatrix}
1 & 5 & 2\\
2 & 7 & 1\\
0 & 1 & 2
\end{bmatrix}$$

我们求它的逆矩阵，需要列出下面的方程

$$\begin{bmatrix}
1 & 5 & 2\\
2 & 7 & 1\\
0 & 1 & 2
\end{bmatrix} \begin{bmatrix}
a & d & g\\
b & e & h\\
c & f & i
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}$$

如果我们以列视角去看待这个方程，我们是否可以把它分成三份呢？答案是肯定的。

$$\begin{bmatrix}
1 & 5 & 2\\
2 & 7 & 1\\
0 & 1 & 2
\end{bmatrix} \begin{bmatrix}
a\\
b\\
c
\end{bmatrix} = \begin{bmatrix}
1\\
0\\
0
\end{bmatrix}$$

$$\begin{bmatrix}
1 & 5 & 2\\
2 & 7 & 1\\
0 & 1 & 2
\end{bmatrix} \begin{bmatrix}
d\\
e\\
f
\end{bmatrix} = \begin{bmatrix}
0\\
1\\
0
\end{bmatrix}$$

$$\begin{bmatrix}
1 & 5 & 2\\
2 & 7 & 1\\
0 & 1 & 2
\end{bmatrix} \begin{bmatrix}
g\\
h\\
i
\end{bmatrix} = \begin{bmatrix}
0\\
0\\
1
\end{bmatrix}$$

我们会发现，这其实就是三个线性方程组的矩阵形式。

$$\begin{cases}
\begin{aligned}
x + 5y + 2z &= 1 \\
2x + 7y + z &= 0 \\
      y + 2z &= 0
\end{aligned}
\end{cases}$$

这里只写出一个。那么我们会想到用哪种工具呢？**消元法**。但值得一提的是，这三个方程组我们可以一并处理，把他们的右值全都粘到左值右面，形成增广矩阵就可以了。

$$\begin{bmatrix}
1 & 5 & 2 | 1 & 0 & 0\\
2 & 7 & 1 | 0 & 1 & 0\\
0 & 1 & 2 | 0 & 0 & 1
\end{bmatrix}$$

现在我们来试着算出矩阵$A$的消元矩阵，与以往不同，我们要试着一次求出将对A进行下三角消元的矩阵。
首先，我们写出一个单位矩阵 $\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1 \end{bmatrix}$ 然后思考，如何线性地组合行一与行二，可以消去行二中的主元$X$，显然，我们这样做: $\begin{bmatrix}
1 & 0 & 0\\
-2 & 1 & 0\\
0 & 0 & 1 \end{bmatrix}$。对于行三的主元$X$，他本来就是$0$所以无需另加处理。而对于行三的主元$Y$，情况则有些复杂。如果我们直接思考的话，需要组合行一和行二，使行三的$X、Y$主元都为0。然而，我们在前一步中，不是已经消去了行二的$X$吗？得到的结果是$\begin{bmatrix}
1 & 5 & 2\\
0 & -3 & -3\\
0 & 1 & 2 \end{bmatrix}$ 那不妨将他们放在一起思考。
消元后的行二由-2份的行一，和1份行二组成，而将这个结果整体乘以 $\frac{1}{3}$ 就可以消去行三的$Y$！所以我们这样做: $\begin{bmatrix}
1 & 0 & 0\\
-2 & 1 & 0\\
-\frac{2}{3} & \frac{1}{3} & 1 \end{bmatrix}$。到此，三角消元结束。试着将消元矩阵乘回原矩阵，我们得到了
$$\begin{bmatrix}
1 & 5 & 2\\
0 & -3 & -3\\
0 & 0 & 1 \end{bmatrix}$$
如果是高斯在做这道题的话，到这里就结束了，但我们还要继续做。也就是消去上三角的元，将矩阵**对角化**。
幸运的是，这一步并没有变得很复杂。我们只需要一点反向思维，也就是从下向上思考。
同样的，我们写出一个单位矩阵$\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1 \end{bmatrix}$，很容易就能看出，我们可以用$3 \times Row(3)$消去行二列三: $\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 3\\
0 & 0 & 1 \end{bmatrix}$，然后用$-2 \times Row(3)$消去行一列三: $\begin{bmatrix}
1 & 0 & -2\\
0 & 1 & 3\\
0 & 0 & 1 \end{bmatrix}$。最后，我们用$\frac{5}{3}$倍的行二，消去行一的$Y$: $\begin{bmatrix}
1 & \frac{5}{3} & 3\\
0 & 1 & 3\\
0 & 0 & 1 \end{bmatrix}$。将这个矩阵乘回去，我们得到了$\begin{bmatrix}
1 & 0 & 0\\
0 & -3 & 0\\
0 & 0 & 1 \end{bmatrix}$，一个对角矩阵。到这一步为止，我们的工作结束了吗？很遗憾并没有，还有最后的最简单的一步。那个$-3$看着很碍眼不是吗？很好，再乘上这个矩阵$\begin{bmatrix}
1 & 0 & 0\\
0 & -\frac{1}{3} & 0\\
0 & 0 & 1 \end{bmatrix}$，我们就从矩阵$A = \begin{bmatrix}
1 & 5 & 2\\
2 & 7 & 1\\
0 & 1 & 2
\end{bmatrix}$，一步一步地得到了单位矩阵。没错，**不知不觉中，我们已经求出了A的逆矩阵**。
回想一下，我们都对矩阵$A$做了什么。我们首先用一个三角化矩阵$\begin{bmatrix}
1 & 0 & 0\\
-2 & 1 & 0\\
-\frac{2}{3} & \frac{1}{3} & 1 \end{bmatrix}$对其进行下三角消元，又用一个对角化矩阵对其进行对角化$\begin{bmatrix}
1 & \frac{5}{3} & 3\\
0 & 1 & 3\\
0 & 0 & 1 \end{bmatrix}$，最后用一个归一化矩阵$\begin{bmatrix}
1 & 0 & 0\\
0 & -\frac{1}{3} & 0\\
0 & 0 & 1 \end{bmatrix}$将其化为单位矩阵。现在，让我们把三次操作和为一次。
$$\begin{bmatrix}
1 & 0 & 0\\
0 & -\frac{1}{3} & 0\\
0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix}
1 & \frac{5}{3} & 3\\
0 & 1 & 3\\
0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix}
1 & 0 & 0\\
-2 & 1 & 0\\
-\frac{2}{3} & \frac{1}{3} & 1 \end{bmatrix} = \begin{bmatrix}
-4\frac{1}{3} & 2\frac{2}{3} & 3\\
\frac{4}{3} & -\frac{2}{3} & -1\\
-\frac{2}{3} & \frac{1}{3} & 1 \end{bmatrix}$$

就这样，我们求出了A的逆矩阵。

### 转置

$$A A^{-1}=I \\
(A^{-1})^{T}A^{T}=I$$

### $A=LU$

这被称为$A$的$LU$分解。其中，U意为Upper，L意为Lower.让我们来看一个简单的例子。
对于矩阵$A = \begin{bmatrix}
2 & 1\\
8 & 7\end{bmatrix}$，我们通过消元法得出它的三角化矩阵$U = \begin{bmatrix}
2 & 1\\
0 & 3\end{bmatrix}$，消元转换矩阵为$M_T=\begin{bmatrix}
1 & 0\\
-4 & 1\end{bmatrix}$。随后我们求出$M_T$的逆矩阵: $M_T^{-1}=\begin{bmatrix}
1 & 0\\
4 & 1\end{bmatrix}$。
随后我们观察到一个有趣的事情，$M_T^{-1}U=A$。$M_T^{-1}$正是我们寻找的$L$矩阵，正如其名，它是一个下三角矩阵。

而对于3x3矩阵，情况会略显复杂。假设我们有三阶矩阵$A$，对他的消元过程可分为三步，也就是用到三个行操作矩阵，我们将其记为$E_{21}、E_{31}、E_{32}$

$$E_{32}E_{31}E_{21}A=U\\
A=E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}U\\
E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}=L$$

我们注意到，E在一式子和二式中的位置是相反的。这很好理解，就好像我们先穿袜子再穿鞋，但是要先脱鞋再脱袜子。

