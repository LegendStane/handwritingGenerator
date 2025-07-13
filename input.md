<h3>期中前</h3>

- 一些基础概念

  - Sample Space 样本空间：一个随机试验(Random Experiment)的所有可能结果的集合
  - Event 事件：一个样本空间的一个子集
  - 若干集合$A_1,A_2\cdots A_k$之间的关系
    - Mutually Exclusive 互斥的$\Leftrightarrow \forall i \neq j,A_i\cap A_j=\emptyset$
    - Exhaustive 穷尽的，并集为全集

- 两种抽样方式

  - Ordered Sample：选择r个样本，并记录选择的顺序
  - Unordered Sample：选择r个样本，不关心选择的顺序
    抽样中涉及的一个记号：$_nP_r=\frac{n!}{(n-r)!}$

- 条件概率公式：$P(R|E)=\frac{P(R\cap E)}{P(E)}$

- Independent Events 独立事件：若$P(A\cap B)=P(A)P(B)$，则$A,B$独立
  	若$A,B,C$两两独立，且$P(A\cap B\cap C)=P(A)P(B)P(C)$，则$A,B,C$相互独立(Mutually Independent)；可以扩展到三个以上的事件

- Random Variable 随机变量：令$S$为一个样本空间，$T$为一个实数集，映射$X: S\to T$是一个随机变量。随机变量(也就是这个函数本身)一般用大写字母表示，它取的值一般用小写字母表示

- 图形化表示PMF的两种方式：线图(Line Graph)和直方图(Probability Histogram)

  <img src="/Users/legendstane/Library/Application Support/typora-user-images/image-20250614234500238.png" alt="image-20250614234500238" style="zoom: 33%;" />

- $Var(X)=E(X^2)-(E(X))^2$

- $r$阶矩(Moment):
  计算 $X$ 的 $r$ 次方的均值，即 $E[X^r] = \sum_{x \in S} x^r f(x)$

  $r$阶中心矩($r$ th moment of $X$ about $b$):
  计算 $(X - b)$ 的 $r$ 次方的均值，即 $E[(X - b)^r] = \sum_{x \in S} (x - b)^r f(x)$

  $r$阶阶乘矩($r$ th factorial moment):
  计算 $X$ 乘以 $(X-1)$ 乘以 $(X-2)$ ... 直到 $(X-r+1)$ 的均值，即 $E[(X)_r] = E[X(X-1)\cdots(X-r+1)]$

- Moment Generating Function 矩生成函数

  若$E(e^{tX})=\sum_{x\in\overline S} e^{tx}f(x)$在一个包含0的开区间内存在(也就是收敛)，则$M(t)=E(e^{tX})$是随机变量$X$的一个矩生成函数

  矩生成函数的性质：

  - $M(0)=1,M'(0)=E(X),M''(0)=E(X^2)$
  - 若两个随机变量的矩生成函数相同，它们的PMF就相同

  典型的矩生成函数形式：

  - $M(t)=(pe^t+(1-p))^n$：二项分布
  - $M(t)=\frac{pe^t}{1-(1-p)e^t}$：几何分布(随机变量定义为"到第一次成功为止的总试验次数") 

- 常见离散随机分布

  - Bernoulli Distribution 伯努利分布：一次试验

  - Binomial Distribution 二项分布：做一定次数的试验，看成功的次数

    $E(X)=np,\ Var(X)=np(1-p),E(X(X-1))=n(n-1)p^2,M(t)=[(1-p)+pe^t]^n$

  - Negative Binomial Distribution 负二项分布：刚好观察到$r$次成功的期望试验次数

    负二项分布的PMF为：$f(x) = \binom{x-1}{r-1} p^r (1-p)^{x-r}$，其中 $x = r, r+1, \ldots$。

    $E(X)=\frac rp,Var(X)=\frac{r(1-p)}{p^2},M(t)=\frac{(pe^t)^r}{[1-(1-p)e^t]^r}$

  - Geometric Distribution 几何分布：$r=1$的负二项分布，是负二项分布的一个特例

    $E(X)=\frac 1p,\ Var(X)=\frac{1-p}{p^2},M(t)=\frac{pe^t}{1-(1-p)e^t}$

  - Uniform Distribution (Discrete, 即在$[a,b]$内的整数中随机取)：$\forall x,y\in\overline S,f(x)=f(y)$

    $E(X)=\frac{a+b}2,Var(X)=\frac{(b-a+1)^2-1}{12}$

  - Poisson Distribution 泊松分布

    - Approximate Poisson Process 近似泊松过程：满足以下条件的情况
      1. 事件在不重叠的时间段内发生互不影响
      2. 极短时间内，事件发生一次的概率与时间长度成正比
      3. 极短时间内，不可能发生两次或以上事件

    令$\lambda$为单位时间内发生一件事的平均次数，令单位时间内实际发生次数为$X$，则泊松分布PMF为

    $f(k)=P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}$

    若一个随机变量的分布符合以上形式，可以直接判断其就是泊松分布。

    $E(X)=Var(x)=\lambda,M(t)=e^{\lambda(e^t-1)}$

- 常见连续随机分布

  - Uniform Distribution (Continuous)

    $E(x)=\frac{a+b}2,Var(X)=\frac{(b-a)^2}{12}$

  - Exponential Distribution 指数分布：一个近似泊松过程中，第一次事件发生前等待的时间

    推导过程：

    在时间$[0,w]$内没有事件发生的概率是$e^{-\lambda w}$，因此CDF $F(w)=1-e^{-\lambda w}$，求导得到：

    PDF $f(w)=\lambda e^{-\lambda w}$，标准形式为$f(x)=\frac1\theta e^{-\frac x\theta}(\theta=\frac1\lambda)$

    $E(X)=\theta=\frac1\lambda,Var(X)=\theta^2=\frac1{\lambda^2},M(t)=\frac1{1-t\theta}$

  - Gamma Distribution 伽马分布：一个近似泊松过程中，第$\alpha$次事件发生前等待的时间

    $F(w)=1-\sum_{k=0}^{\alpha-1}\frac{(\lambda w)^ke^{-\lambda w}}{k!}$

    $f(w)=F'(w)=\frac{\lambda^\alpha w^{\alpha-1}}{(\alpha-1)!}e^{-\lambda w}$

    $E(X)=\alpha\theta=\frac\alpha\lambda,Var(X)=\alpha\theta^2=\frac\alpha{\lambda^2},M(t)=\frac1{(1-t\theta)^\alpha}$

    通过定义一般化的阶乘函数Gamma函数$\Gamma(t)=\int_0^\infty y^{t-1}e^{-y}dy$，可以把Gamma分布扩展到$\alpha$不是正整数的情况

  - Chi square Distribution 卡方分布：自由度为整数$r$的卡方分布是$\alpha=\frac r2,\lambda=\frac12$的Gamma分布

    $f(x)=\frac{(\frac12)^{\frac r2}x^{\frac r2-1}}{\Gamma(\frac r2)}e^{-\frac x2}$

    $E(X)=r,Var(X)=2r,M(t)=(1-2t)^{-\frac r2}$

  - Normal Distribution 正态分布

    $f(x)=\frac1{\sqrt{2\pi\sigma^2}}exp(-\frac12\cdot \frac{(x-\mu)^2}{\sigma^2})$，其中$\mu$是均值，$\sigma^2$是方差，$X\sim N(\mu,\sigma^2)$

    $M(t)=exp(\mu t+\frac12\sigma^2t^2)$

    在标准正态分布($\mu=0,\sigma=1$)中，$z_\alpha$是一个满足$P(Z\geq z_\alpha)=\alpha$的值

    正态分布和卡方分布的关系：$X\sim N(\mu,\sigma^2)$，则$\frac{(X-\mu)^2}{\sigma^2}\sim \chi^2(1)$

- 百分位数的表示：可以用$\pi_p$的形式来表示百分位数，如$\pi_{0.25}$表示第25百分位数

- 