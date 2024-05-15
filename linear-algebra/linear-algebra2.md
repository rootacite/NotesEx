
# 线性代数

## 置换矩阵

置换矩阵是行互换后的单位矩阵。

* 对于一个nxn阶的方阵，其共有$n!$个置换矩阵。
* 置换矩阵都是可逆的。

## 转置矩阵

![alt text](image-1.png)

* 若有矩阵$R$，则$R^{T}R$永远是对称的，这不难理解。

$$(R^{T}R)^T = RR^T$$

换句话说，如果你要验证一个矩阵的对称性，一个很好的方式是取他的转置，看看是否相同。

## 向量空间

想象你的面前有若干个向量，比如$\begin{bmatrix}1\\ 0\end{bmatrix}$, $\begin{bmatrix}0\\ 0\end{bmatrix}$，$\begin{bmatrix}3\\ 2\end{bmatrix}$，$\begin{bmatrix}\pi \\ e\end{bmatrix}$，他们之间可以相互线性组合，或者数乘。如果将前面的四个变量设为一个集合，显然$\begin{bmatrix}3\\ 2\end{bmatrix}$和$\begin{bmatrix}\pi \\ e\end{bmatrix}$相加的结果不在那个集合之中。但是，想象一个集合，这个集合足够大，以至于他其中的任何向量之间进行数乘和加法，结果都在这个集合之内，我们就称这个集合为一个**向量空间**。比如$R、R^2、R^n$。

### 向量空间的八条运算定律

* $a+b=b+a \qquad \forall a,b \in V$
* $(a+b)+c=a+(b+c) \qquad \forall a, b, c \in V$
* $\exists 0 \in V \quad \forall a \in V, 0+a=a$
* $\forall a \in V, \exists b \in V \qquad a+b=0$
<br>
* $\exists 1 \in k, \forall a \in V \qquad 1 \cdot a = a$
* $(n \cdot m) \cdot a = n \cdot (m \cdot a) \qquad \forall n, m \in k, a \in V$
* $(n+m) \cdot a = a \cdot n + a \cdot m  \qquad \forall n, m \in k, a \in V$
* $n \cdot (a+b) = n \cdot a + n \cdot b  \qquad \forall n, m \in k, a \in V$

### 子空间

顾名思义——向量空间中的另一个向量空间。比如对于$R^2$来说，他的子空间可以分为三种: 

* $R^2$ 本身
* 任何过原点的，限延伸的直线
* 零向量

而对于$R^3$来说，除了它自身和零向量，还有两种情况: 

* 任何过原点的，无限延伸的直线
* 任何过原点的，无限展开的平面

#### 从矩阵中构造子空间

假设我们有矩阵$A = \begin{bmatrix} 1 & 3\\ 2 & 3 \\ 4 & 1 \end{bmatrix}$，它的每一列都是一个属于$R^3$的向量。

$$\begin{bmatrix} 1\\ 2 \\ 4 \end{bmatrix}, \begin{bmatrix} 3\\ 3 \\ 1 \end{bmatrix} \in R^3$$

如果我们想用这两个向量构建一个子空间，那个子空间需要包含什么呢？这两个向量本身、零向量、这两个向量相加以及数乘的结果...... 总得来说，我们构建的子空间，**包含这两个向量的所有可能的线性组合**。而一个矩阵的全部列的所有可能的线性组合的结果组成的子空间，就称为这个矩阵的**列空间**。

##### 子空间的交集与并集

* 子空间的交集是子空间
* 子空间的并集不一定是子空间

### 列空间

若有矩阵$A=\begin{bmatrix}1 & 1 & 2\\ 2 & 1 & 3\\ 3 & 1 & 4\\ 4 & 1 & 5 \end{bmatrix}$，它的所有列均为$R^4$中的四维向量。$A$的列空间为$R^4$子空间，记为$C(A)$。现在我们要关注的是，这是一个怎么样的子空间？是一整个$R^4$空间吗，或者是一个$R^3$空间。首先，我们的直觉就告诉我们，他不会是一个完整的$R^4$空间，三个向量的线性组合怎么说也不会是四维。那么我们不妨列一个方程:

$$\begin{bmatrix}1 & 1 & 2\\ 2 & 1 & 3\\ 3 & 1 & 4\\ 4 & 1 & 5 \end{bmatrix} \begin{bmatrix}x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix}b_1 \\ b_2 \\ b_3 \\b_4 \end{bmatrix}$$

这个方程有解，当且仅当$\begin{bmatrix}b_1 \\ b_2 \\ b_3 \\b_4 \end{bmatrix} \in C(A)$。

随后，我们关注一个更重要的问题，矩阵$A$的所有列是线性无关的吗？它的三列是否都对线性组合有所贡献，还是说其中一列没有。这个问题的答案是否定的，至少有一行对这个线性组合没有贡献。因此，实际上$C(A)$是一个二维平面。

### 零空间

对于上述的方程，若右侧的$b$为零向量，方程的所有的解的集合被成为零空间。

$$\begin{bmatrix}1 & 1 & 2\\ 2 & 1 & 3\\ 3 & 1 & 4\\ 4 & 1 & 5 \end{bmatrix} \begin{bmatrix}x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix}0 \\ 0 \\ 0 \\0 \end{bmatrix}$$

显然，它的解位于$R^3$，对于这个方程它的解集为$\begin{bmatrix} c \\ c \\ -c \end{bmatrix}$，一个一维直线。

#### $Ax=0$求解零空间与矩阵的秩

$$A=\begin{bmatrix}1 & 2 & 2 & 2 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 8 & 10 \end{bmatrix}$$

以往我们消元的对象都是方阵，而这次换成了长方矩阵。这导致什么呢？即使遇到主元为0的情况，我们也得继续下去。

$$\widetilde{r_2-2r_1, r_3-3r_1}\begin{bmatrix}1 & 2 & 2 & 2 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 2 & 4 \end{bmatrix}$$

我们会发现，第二列的主元变为了0，并且也没有可以用来置换的行。这说明第二列是前面几列的线性组合，以及我们对第二列没辙，于是我们转向第三列，把$a_{23}$作为主元

$$\widetilde{r_3-r_2}\begin{bmatrix}(1) & 2 & 2 & 2 \\ 0 & 0 & (2) & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix} = U$$

我们得到了矩阵$U$，一个阶梯矩阵。这个矩阵中主元的数目为2，这被称为矩阵的**秩**。记作$R(A)=2$。

此时我们还可以将行一中的主元$(2)$消去，形成行最简矩阵。

$$\widetilde{r_1-r_2}\begin{bmatrix}(1) & 2 & 0 & -2 \\ 0 & 0 & (2) & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix} = R$$

而此时，原本的$Ax=0$被我们转化为了$Rx=0$。

## Determinant (行列式)

总得来说，Determinant是一个**线性函数**，其输入变量是一个矩阵，输出为这个矩阵的某个属性值。
其有以下四个特点:

1. $det(I) = 1$
2. 交换矩阵的任意两行，会使他的Determinant取负值。你理解的没错，假设对于矩阵$A$，行交换的次数为$n$，那么$det(A')=(-1)^ndet(A)$
3. $\begin{vmatrix} t \cdot a & t \cdot b\\ c & d \end{vmatrix} = t \cdot \begin{vmatrix} a & b \\ c & d \end{vmatrix}$
4. $\begin{vmatrix} a + a' & b + b'\\ c & d \end{vmatrix} = \begin{vmatrix} a & b \\ c & d \end{vmatrix} + \begin{vmatrix} a' & b' \\ c & d \end{vmatrix}$

根据上面的几个特点，按理来说我可以推出Determinant函数的所有性质。比如下面几条: 

5. 如果有两行完全相同，这个矩阵的Determinant为零。
6. 将一行加上其他行的实数倍，Determinant不变。

性质6的推导如下：

$$l \in R, \begin{vmatrix} a & b \\ c-la & d-lb\end{vmatrix} = \begin{vmatrix} a & b \\ c & d\end{vmatrix}-l\begin{vmatrix} a & b \\ a & b\end{vmatrix}$$

而为什么$\begin{vmatrix} a & b \\ a & b\end{vmatrix}=0$呢？根据性质2,交换行Determinant取负，而对于前面的矩阵来说，交换行等于没交换。那么什么数取负等于没取呢——0？

### Determinant与奇异矩阵

总得来说，若一个矩阵的Determinant不为0，则它为非奇异矩阵，否则为奇异矩阵。我们可以回忆一下奇异矩阵的特点——有一行或多行呈线性相关。

#### Determinant的几何定义

这里我们引入Determinant函数的几何定义，它表示以这个矩阵的行组/列组作为向量组，n个n维向量，所围成的集合图形的空间积。
比如二维矩阵$A=\begin{vmatrix} 2 & 1\\ 5 & 1 \end{vmatrix}$，它在空间中围成了这样的图形。

![alt text](image-2.png)

而$detA$的值，就是这个图形的面积。若两个向量具有线性相关性，很显然，这个图形的面积为0。

### 逆序数

对于一个n阶方阵，将其按照行列式的规则展开为多项式，该多项式的每一项都是形如$$s \cdot a_{0j_0}a_{1j_1}a_{2j_2}a_{3j_3}...a_{nj_n}$$的形式。其中：$$s=-1^{\tau(j_0j_1j_2...j_n)}$$

### 代数余子式

#### 余子式

把方阵中的$(i, j)$元素所在的行与列全部删去后，剩下的部分被称为$a_{ij}$的余子式，记作$M_{ij}$。若取$r=(-1)^{i+j}$，则$r \cdot M_{ij} = A_{ij}$被成为代数余子式。

#### 矩阵的按行(列)展开

对于三阶以上的矩阵，计算其行列式若使用逆序数法会较为麻烦，但行列式有一个重要的性质。
例如我们有 $$D_4 = \begin{vmatrix} 2&-1&0&0 \\ 0 & 2 & -1 &0\\ 0&0&2&-1\\ -1&0&0&2 \end{vmatrix}$$
要计算他的行列式，我们可以选择一个基准行，比如行一。然后我们可以利用一个规律，矩阵的行列式值，等于其某行的元素乘以其代数余子式的值再累加。
具体来说，我们这样计算。
$$det(D_4)=2 \cdot det \begin{vmatrix} 2&-1&0\\ 0&2&-1 \\0&0&2\end{vmatrix}+(-1) \cdot -det\begin{vmatrix} 0&-1&0\\ 0&2&-1\\ -1&0&2 \end{vmatrix}\\ =2 \cdot 8 - 1 = 15 $$

#### Laplace 展开

若$A、B$为$m、n$阶矩阵，则
$$\begin{vmatrix} A&0\\ 0&B \end{vmatrix} = \begin{vmatrix} A&C\\ 0&B \end{vmatrix}= \begin{vmatrix} A&0\\ C&B \end{vmatrix}  = det(A) + det(B)$$

若交换$A、B$矩阵的位置，则上式等于$(-1)^{nm}det(A)det(B)$。

#### Vandermond矩阵

形如 $$A = \begin{vmatrix}1&1&1&1\\ x_1&x_2&x_3&x_4\\ x_1^2&x_2^2&x_3^2&x_4^2\\ \vdots &\vdots&\vdots&\vdots \\ x_1^n&x_2^n&x_3^n&x_4^n\end{vmatrix}$$ 的行列式被称为Vandermond矩阵。
这种矩阵的Det值有特殊求法，我们可以取第二行的元素的，所有逆序组合，然后将它们累乘。