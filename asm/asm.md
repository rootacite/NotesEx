# x86汇编与处理器体系结构

## 基础知识

### 重要的寄存器

#### 通用寄存器

| 累加器 | 基地址寄存器 | 计数寄存器 | 数据寄存器 |
|-------|-------|-------|-------|
|RAX|RBX|RCX|RDX|

| 源索引寄存器 | 目标索引寄存器 | 基指针寄存器 | 堆栈指针寄存器
|-------|-------|-------|-------|
|RSI|RDI|RBP|RSP|

此外，**%rax被用作保存函数返回值。**
**%rdi, %rsi, %rdx, %rcx, %r8, %r9 分别保存第 1-6个参数**

#### 状态寄存器

* CF: 进位标志
* ZF: 零标志
* SF: 符号标志
* OF: 溢出标志

#### 控制寄存器

* RIP: 指令计数器
* TSC: 时间戳计数器

*************

### 数据访问方式

对于(提供给CPU的)指令来说，能直接访问的数据主要分为三种：

* 立即数
* 寄存器
* 主存

并衍生出以下若干种寻址格式

| Type | Format | Operation value | Name |
|-------|-------|-------|-------|
| 立即数 | $\$Imm$ | $Imm$ | 立即数寻址 |
| 寄存器 | $r_a$  | $R(r_a)$ | 寄存器寻址 |
| 存储器 | $Imm$ | $M(Imm)$ | 绝对寻址 |
| 存储器 | $(r_a)$  | $M[R(r_a))]$ | 间接寻址 |
| 存储器 | $Imm(r_b)$  | $M[Imm+R(r_b)]$ | 基址+偏移 |
| 存储器 | $(r_b,r_i)$  | $M[R(r_b)+R(r_i)]$ | 变址寻址 |
| 存储器 | $Imm(r_b,r_i)$  | $M[Imm+R(r_b)+R(r_i)]$ | 变址寻址 |
| 存储器 | $(,r_i,s)$  | $M[R(r_i) \cdot s]$ | 比例变址寻址 |
| 存储器 | $Imm(,r_i,s)$  | $M[Imm+R(r_i) \cdot s]$ | 比例变址寻址 |
| 存储器 | $(r_b,r_i,s)$  | $M[R(r_b)+R(r_i) \cdot s]$ | 比例变址寻址 |
| 存储器 | $Imm(r_b,r_i,s)$  | $M[Imm+R(r_b)+R(r_i) \cdot s]$ | 比例变址寻址 |

## 程序的机器级表示

### 总览

我们有以下C程序：

```c
extern long mul2(long, long);

void mulstore(long x, long y, long *dst)
{
    long t = mul2(x, y);
    *dst = t;
}
```

其可以被编译为下面的汇编代码：

```asm
;   void mulstore(long x, long y, long *dst)
;   x: %edi, y: %esi, dst: %edx
;   return: %eax

mulstore:
    push %ebp           ; Save stack base address
    mov  %esp, %ebp     ; Set local stack frame
    call mul2
    mov  %eax, (%edx)
    mov  %ebp, %esp     ; Destory function stack
    pop  %ebp           ; Restore stack base of last function
```

值得注意的是，我们在代码中调用了过程"mul2"但却没有给出他的定义。在此处，mul2被称为外部导入符号，被定义在目标文件的符号表内。在被链接为可执行文件时，链接器需要去其他目标文件中寻找"mul2"的定义。
如果找到了那是最好，没找到的话，我们就会见到喜闻乐见的"Undefined External Symbol"错误。
关于链接器如何找到一个目标文件需要的外部符号，又如何在可执行文件中组织他们，这是一个有趣的问题，但它不在这篇笔记的讨论范围内，所以我们点到为止。

### 数据传输指令

#### mov系列

| Command | Effect | Discription |
|-------|-------|-------|
| MOV   S,D| $S \to D$| 传送|
|movb||传送字节|
|movw||传送字|
|movl||传送双字|
|movq||传送四字|

若我们需要在不同长度的存储单位之间传送数据，x86为我们提供了另外两组指令，前者用于传送无符号数，后者用于传送有符号数：

* **movz + "sf" + "df"**
* **movs + "sf" + "df"**

例如：

```asm
movl %eax, (%rsp)
movw (%rax), %dx
movb %0xFFh, %bl
movb (%rsp,%rdx,4), %dl
movq (%rdx), %rax
movw %dx, (%rax)
```

在一个具体的例子里，对于数据交换函数:

```c
void swap(int32_t *x, int32_t *y)
{
    int32_t temp = *x;
    *x = *y;
    *y = temp;
}
```

其可以被编译为:

```asm
swap:
    push  %ebp
    movl  %esp,   %ebp

    movl  (%edi), %eax
    movl  (%esi), %ebx  ;不能直接进行内存->内存数据传输
    movl  %ebx,   (%edi)
    movl  %eax,   (%esi)

    movl %ebp,    %esp
    pop  %ebp
```

#### 压入和弹出栈数据

| Command | Effect | Discription |
|-------|-------|-------|
|push  S| sub $4, %esp <br> mov S, (%esp)| 将数据入栈|
|pop  D| mov (%esp), D <br> add $4, %esp | 将数据出栈|

#### 加载有效地址

* lea (Load Effective Address) 指令将一个形式地址转化为有效地址。需要注意的是，在现代的编译器中，lea指令几乎已经偏离了它原本的用法。

对于下面的程序:

```c
long scale(long x, long y, long z)
{
    long t = x + (4 * y) + (12 * z);
    return t;
}
```

其可以被编译为

```asm
scale:
    lea (%rdi, %rsi, 4), %rax
    lea (,%rdx,12), %rbx
    add %rbx, %rax
    ret
```

### 算术&逻辑操作

| Command | Effect | Discription |
|-------|-------|-------|
|inc &emsp; D| D++ |自增|
|dec &emsp; D| D-- |自减|
|neg &emsp; D| D=-D|取负|
|not &emsp; D| D=~D|取反|

| Command | Effect | Discription |
|-------|-------|-------|
|add &emsp; S,D| D+=S |加|
|sub &emsp; S,D| D-=S |减|
|imul &emsp; S,D| D*=S|乘|
|xor &emsp; S,D| D^=S|异或|
|or &emsp; S,D| D\|=S |或|
|and &emsp; S,D| D&=S |与|

| Command | Effect | Discription |
|-------|-------|-------|
|sal &emsp; k,D| D = D << k |算术左移|
|shl &emsp; k,D| D = D << k |逻辑左移|
|sar &emsp; k,D| D = D >> k |算术右移|
|shr &emsp; k,D| D = (uint32_t)D >> k|逻辑右移|

#### 条件码

状态寄存器中的一些位可以被单独访问，并具有一下意义：

* CF: 进位标志 最近的操作使最高位产生了进位，用于检测无符号运算的溢出
* ZF: 零标志   最近的操作结果为0
* SF: 符号标志 最近的操作得出了负数的结果
* OF: 溢出标志 最近的操作导致一个补码溢出

这些标志位是进行条件分歧和分支跳转的基础。

#### 测试指令

| Command | Effect | Discription |
|-------|-------|-------|
|cmp &emsp; s1,s2| $S_2-S_1$|比较|
|test &emsp; s1,s2| $S_1\&S_2$ |测试|

### 分支控制

#### 无条件跳转

| Command | Condition | Discription |
|-------|-------|-------|
|jmp &emsp; Label| Always | 直接跳转 |
|jmp &emsp; *Operand| Always | 间接跳转 |

#### 跳转指令的编码



******
