# Section 1.6 - Other Types of Equations and Applications

## BRIEF REVIEW

Let $\{1,2,3\}$ be a set of numbers. If $\{1,2,3,...\}$ is a set of numbers then the set could also be presented as $\{1,2,3,4,5,6,...\}$. The "$...$" represents the pattern of the previous number, which will continue to repeat.

-   The set of Real number, $\mathbb{R}$, is the set of all possible real numbers.
    -   $0,1,\frac{1}{2},\frac{3}{2},\sqrt{2},\pi,e,...$
-   The set of Natural Numbers, $\mathbb{N}$,
    -   is $\{1,2,3,...\}$.
-   Notice that $\mathbb{N}$ is absent of the number $0$. The whole numbers is the set
    -   $\{0,1,2,...\}=\mathbb{N}\cup\{0\}$.
-   Notice that $\mathbb{N}$ is absent of the negative values and $0$. The integers is the set
    -   $\{...,-2,-1,0,1,2,...\}=\mathbb{Z}$
-   Notice that $\mathbb{Z}$ is absent of the values between each element. The rational numbers is
    -   $\{\frac{q}{p}\,|\,q\in\mathbb{Z}$ and $p\in\mathbb{Z}\backslash\{0\}\}=\mathbb{Q}$
-   Notice that $\mathbb{Q}$ is absent of the values between each element. The irrational number is what is left after real numbers and rational numbers
    -   , i.e., $\mathbb{R}\backslash\mathbb{Q}$.
-   Notice that $\mathbb{R}$ is absent of values involving $\sqrt{-1}$ as a factor. The complex numbers is $$\mathbb{C}=\{a,b\in\mathbb{R}\,|\,a+ib\land i=\sqrt{-1}\}$$

:::::{grid}
::::{grid-item-card}
:::{prf:property} No Real Solution
:label: noRealSolution
:nonumber:
The solution to the equation $x^{2}+1=0$ is $x=\pm i$ where $i=\sqrt{-1}$.
:::
::::
::::{grid-item-card}
:::{prf:property} Powers of Imaginary Number
:label: powersImaginaryNumber
:nonumber:
Let $i=\sqrt{-1}$. Then $$\begin{aligned}
\sqrt{-1} & =i\\
i^{2} & =-1\\
i^{3} & =-i\\
i^{4} & =1\end{aligned}$$
:::
::::
:::::

:::{prf:property} Arithmetic Properties
:label: arithmeticProperties
Let $a,b,c,d\in\mathbb{R}$ 
$$
    \begin{aligned}
        a+0 & =a\\
        a\cdot1 & =a\\
        a & =b\iff a+c=b+c\\
        a & =b\iff a\cdot c=b\cdot c
    \end{aligned}
$$
:::

:::{prf:property} Laws of Exponents
:label: loe
:nonumber:
Further let $m,n\in\mathbb{Z}$ 
$$
    \begin{aligned}
        \text{If $n>0$, then }a^{n} & =\underset{\text{$n$ times}}{\underbrace{a\cdot a\cdot\ldots\cdot a}}. & (ab)^{n} & =a^{n}b^{n}\\
        a^{n}\cdot a^{m} & =a^{n+m} & \left(\frac{a}{b}\right)^{n} & =\frac{a^{n}}{b^{n}}\\
        \frac{a^{n}}{a^{m}} & =a^{n-m} & \sqrt{a} & =a^{\frac{1}{2}}\\
        (a^{n})^{m} & =a^{n\cdot m} & \sqrt[n]{a} & =a^{\frac{1}{n}}\\
        a^{-n} & =\frac{1}{a^{n}} & \sqrt[n]{a^{m}} & =a^{\frac{m}{n}}
    \end{aligned}
$$
:::

:::{prf:property} Methods for solving equations
:label: methodSolvingEquations
:nonumber:
The solution for (provided the equation is solvable) $$\begin{aligned}
x+c & =d\iff x=c-d\\
x\cdot c & =d\iff x=\frac{d}{c}\\
x^{2} & =c\iff x=\pm\sqrt{c}\text{ or }\pm c^{\frac{1}{2}}\\
x^{3} & =d\iff x=\sqrt[3]{d}\text{ or }d^{\frac{1}{3}}\\
x^{\frac{1}{2}} & =d\iff x=d^{2}\\
x^{\frac{1}{3}} & =d\iff x=d^{\frac{2}{3}}\\
x^{\frac{m}{n}} & =d\iff x=d^{\frac{n}{m}}\end{aligned}$$
:::

## Solving Equations and Constructing Models

One of the most important properties in this course that we will use is the follow.
:::{prf:theorem} Zero Product Property
:label: zpp
Let $a$ and $b$ be any real number $a\cdot b=0$ if and only if $a=0$ or $b=0$.
:::

Let $P$ and $Q$ be algebraic expressions. If the set $X$ is the solution set for $P=Q$, then the set $X$ is the solution set for $(P)^{n}=(Q)^{n}$ where $n$ is some positive integer. Similarly, if $X$ is the solution set for $(P)^{n}=(Q)^{n}$, then $X$ is the solution set for $P=Q$ where $n$ is some positive integer.

### Basic Models

Here is an example of the basic models we will use moving forward. There will be more models discovered as the semester moves along.
:::{prf:example} Simple algebraic models
Moving objects: $$d=rt$$ where

-   $d$ equals distance traveled,
-   $r$ is the rate as which something is moving, and
-   $t$ is the time traveled.

Similarly, work: $$W=rt$$ where

-   $W$ is the amount of work completed,
-   $r$ is the number of tasks completed over a period of time, and
-   $t$ is the time worked.
:::
A rational equation is an equation that has a rational expression for one or more terms. Moving forward when solving equations we will present the solution as a set of numbers, the solution set.

### Rational Equations
::::{prf:example}
Solve the equation $$\dfrac{3x-1}{3}-\dfrac{2x}{x-1}=x$$
:::{dropdown} Solution:
$$\begin{aligned}
\dfrac{3x-1}{3}-\dfrac{2x}{x-1} & =x\\
(3)\cdot(x-1)\cdot\left(\dfrac{3x-1}{3}-\dfrac{2x}{x-1}\right) & =x\cdot(3)\cdot(x-1)\\
(3x-1)(x-1)-2x(3) & =3x(x-1)\\
3x^{2}-3x-x+1-6x & =3x^{2}-3x\\
-10x+1 & =-3x\\
-7x & =-1\\
x & =\dfrac{1}{7}\end{aligned}$$
Therefore the solution set for the equation is $\{\frac17\}$.
:::
::::
::::{prf:example}
Solve $$\dfrac{3x+2}{x-2}+\dfrac{1}{x}=\dfrac{-2}{x^{2}-2x}$$
:::{dropdown} Solution:
The left hand side is: $$\begin{aligned}
\left(\dfrac{x}{x}\right)\cdot\dfrac{3x+2}{x-2}+\dfrac{1}{x}\cdot\left(\dfrac{x-2}{x-2}\right) & =\dfrac{3x^{2}+2x}{x(x-2)}+\dfrac{x-2}{x(x-2)}\\
 & =\dfrac{3x^{2}+3x-2}{x(x-2)}\end{aligned}$$

The right hand side is $$\dfrac{-2}{x^{2}-2x}=\dfrac{-2}{x(x-2)}$$

Putting back together we have $$\begin{aligned}
(x)\cdot(x-2)\left(\dfrac{3x^{2}+3x-2}{x(x-2)}\right) & =\left(\dfrac{-2}{x(x-2)}\right)\cdot(x)(x-2)\\
3x^{2}+3x-2 & =-2\\
3x^{2}+3x & =0\\
3x(x+1) & =0\\
x & =\{0,-1\}\end{aligned}$$ Since the equation is undefined when $x=0$ we will exclude $x=0$ from the solution set. After checking we have $\{-1\}$ as the solution set.
:::
::::
### Radical Equations
::::{prf:example}
Find the solution set for $$\sqrt{x}=2$$
:::{dropdown} Solution:
In this case $P=\sqrt{x}$ and $Q=2$, we know that $$\sqrt{x}=2\iff x=\{4\}.$$ Similarly, $$\begin{aligned}
P^{2} & =Q^{2}\\
\left(\sqrt{x}\right)^{2} & =(2)^{2}\\
\left(x^{\frac{1}{2}}\right)^{2} & =4\\
x & =4\end{aligned}$$ which matches the solution set before.
:::
::::
::::{prf:example}
Solve $$\sqrt{x}-5=2$$
:::{dropdown} Solution:
To solve the equation we want to find the solution set for the equation $\sqrt{x}-5=2$. $$\begin{aligned}
\sqrt{x}-5 & =2\\
\sqrt{x} & =5+2\\
\sqrt{x} & =7\\
x & =7^{2}=49\end{aligned}$$ therefore the solution set is $x=\{49\}$. We can check this set to see if it is a solution set $$\begin{aligned}
\sqrt{49}-5 & =2\\
7-5 & =2\\
2 & =2\checkmark\end{aligned}$$ Therefore, the solution set is verified.
:::
::::
::::{prf:example}
Solve $$x-\sqrt{4x+12}=0$$
:::{dropdown} Solution:
We will isolate the radical expression and then square both sides of the equation: $$\begin{aligned}
x-\sqrt{4x+12} & =0\\
x & =\sqrt{4x+12}\\
\left(x\right)^{2} & =\left(\sqrt{4x+12}\right)^{2}\\
x^{2} & =\left(\left(4x+12\right)^{\frac{1}{2}}\right)^{2}\because\sqrt{x}=x^{\frac{1}{2}}\\
x^{2} & =4x+12\\
x^{2}-4x-12 & =0\\
(x-6)(x+2) & =0\end{aligned}$$ Since $a\cdot b=0$ if and only if $a=0$ or $b=0$; we have, $$\begin{aligned}
x-6 & =0\text{ or }x+2=0\\
x & =6\text{ or }x=-2\end{aligned}$$ Therefore, we claim the solution set is $\{6,-2\}$.

Next, we will check:

When $x=6$: $$\begin{aligned}
6-\sqrt{4\cdot6+12} & =0\\
6-\sqrt{36} & =0\\
6-6 & =0\\
0 & =0\checkmark\end{aligned}$$

When $x=-2$: $$\begin{aligned}
-2-\sqrt{4\cdot(-2)+12} & =0\\
-2-\sqrt{4} & =0\\
-2-2 & =0\\
-4 & \ne0\end{aligned}$$

This means $\{6\}$ is the solution set.
:::
::::
::::{prf:example}
Solve $$\sqrt{3x+1}-\sqrt{x+4}=1$$
:::{dropdown} Solution:
In this case, we cannot isolate the radical expression. We will have to settle for isolating one of the radical expressions and squaring both sides. This will eliminate all of the radical expressions, but it will eliminate one of the radical expressions.

$$\begin{aligned}
\sqrt{3x+1}-\sqrt{x+4} & =1\\
\sqrt{3x+1} & =1+\sqrt{x+4}\\
\left((3x+1)^{\frac{1}{2}}\right)^{2} & =\left(1+(x+4)^{\frac{1}{2}}\right)^{2}\\
3x+1 & =1^{2}+2(x+4)^{\frac{1}{2}}+\left((x+4)^{\frac{1}{2}}\right)^{2}\because(a+b)^{2}=a^{2}+2ab+b^{2}\\
3x+1 & =1+2\sqrt{x+4}+(x+4)\\
3x+1 & =2\sqrt{x+4}+x+5\end{aligned}$$ Next, we will isolate the radical expression to eliminate the last radical expression. $$\begin{aligned}
3x+1-x-5 & =2\sqrt{x+4}\\
2x-4 & =2\sqrt{x+4}\\
2(x-2) & =2\sqrt{x+4}\\
\frac{1}{2}\left(2(x-2)\right) & =\frac{1}{2}\left(2\sqrt{x+4}\right)\\
x-2 & =\sqrt{x+4}\\
\left(x-2\right)^{2} & =\left((x+4)^{\frac{1}{2}}\right)^{2}\\
x^{2}-4x+4 & =x+4\\
x^{2}-4x+4-x-4 & =0\\
x^{2}-5x & =0\\
x(x-5) & =0\\
x & =\{0,5\}\end{aligned}$$ Therefore, we claim $x=\{0,5\}$ is the solution set.

When $x=0$: $$\begin{aligned}
\sqrt{3(0)+1}-\sqrt{0+4} & =1\\
\sqrt{1}-\sqrt{4} & =1\\
1-2 & =1\\
-1 & \ne1\end{aligned}$$

When $x=5$: $$\begin{aligned}
\sqrt{3(5)+1}-\sqrt{5+4} & =1\\
\sqrt{16}-\sqrt{9} & =1\\
4-3 & =1\\
1 & =1\checkmark\end{aligned}$$

This means the solution set is $x=\{5\}$.
:::
::::
::::{prf:example}
Solve $$\sqrt[3]{5x^{2}-12x+6}-\sqrt[3]{x}=0$$
:::{dropdown} Solution:
First, recall $$\begin{aligned}
\sqrt[3]{x} & =x^{\frac{1}{3}}\\
\left(x^{\frac{1}{3}}\right)^{3} & =x\end{aligned}$$

Since there are two expressions with cube-root-radicals we want to separate them and then cube both sides. 
$$\begin{aligned}
\sqrt[3]{5x^{2}-12x+6}-\sqrt[3]{x} & =0\\
\sqrt[3]{5x^{2}-12x+6} & =\sqrt[3]{x}\\
\left(5x^{2}-12x+6\right)^{\frac{1}{3}} & =x^{\frac{1}{3}}\\
\left(\left(5x^{2}-12x+6\right)^{\frac{1}{3}}\right)^{3} & =\left(x^{\frac{1}{3}}\right)^{3}\\
5x^{2}-12x+6 & =x\\
5x^{2}-13x+6 & =0\\
5x^{2}-10x-3x+6 & =0\\
5x(x-2)-3(x-2) & =0\\
(x-2)(5x-3) & =0\end{aligned}$$ By the zero product property we have 
$$\begin{aligned}
x-2 & =0\iff x=2\\
5x-3 & =0\iff x=\frac{3}{5}\end{aligned}$$

We claim $\{1,\frac{6}{5}\}$ is the solution set for the original equation. Now, we will check: 
$$\begin{aligned}
5x^{2}-12x+6|_{x=2} & =5*(2)^{2}-12*(2)+6\\
 & =2\\
\sqrt[3]{5*(2)^{2}-12*(2)+6}-\sqrt[3]{2} & =0\\
\sqrt[3]{2}-\sqrt[3]{2} & =0\checkmark\\
5x^{2}-12x+6|_{x=\frac{3}{5}} & =5*(\frac{3}{5})^{2}-12*(\frac{3}{5})+6\\
 & =\frac{3}{5}\\
\sqrt[3]{5*(\frac{3}{5})^{2}-12*(\frac{3}{5})+6}-\sqrt[3]{\frac{3}{5}} & =0\\
\sqrt[3]{\frac{3}{5}}-\sqrt[3]{\frac{3}{5}} & =0\checkmark\end{aligned}$$

Therefore, the solution set for the equation $$\sqrt[3]{5x^{2}-12x+6}-\sqrt[3]{x}=0$$ is $\{2,\frac{3}{5}\}$.
:::
::::
### Exponential Equations
::::{prf:example}
Solve $$x^{\frac{3}{2}}=216$$
:::{dropdown} Solution:
Before we start $$x^{\frac{3}{2}}=d\iff\left(x^{\frac{3}{2}}\right)^{\frac{2}{3}}=(d)^{\frac{2}{3}}\iff x=d^{\frac{2}{3}}$$ provided $d^{\frac{2}{3}}$ is a real number. In this case $d=216$ and $216^{\frac{2}{3}}=(2^{3}3^{3})^{\frac{2}{3}}=2^{2}\cdot3^{2}=36$. To clarify, $36^{\frac{3}{2}}=\left(36^{\frac{1}{2}}\right)^{3}=(6)^{3}=216$.

Algebraically, we will solve "slowly" $$\begin{aligned}
x^{\frac{3}{2}} & =216 & x^{\frac{3}{2}} & =216\\
\left(x^{\frac{1}{2}}\right)^{3} & =216 & \left(x^{3}\right)^{\frac{1}{2}} & =216\\
\left(\left(x^{\frac{1}{2}}\right)^{3}\right)^{\frac{1}{3}} & =(216)^{\frac{1}{3}} & \left(\left(x^{3}\right)^{\frac{1}{2}}\right)^{2} & =(216)^{2}\\
x^{\frac{1}{2}} & =6 & x^{3} & =46656\\
\left(x^{\frac{1}{2}}\right)^{2} & =6^{2} & \left(x^{3}\right)^{\frac{1}{3}} & =(46656)^{\frac{1}{3}}\\
x & =36 & x & =36\end{aligned}$$

We claim that $x=\{36\}$ is a solution set for the original equation. Now, we can check:- $$\begin{aligned}
(36)^{\frac{3}{2}} & =216 & (36)^{\frac{3}{2}} & =216\\
\left(36^{\frac{1}{2}}\right)^{3} & =216 & \left(36^{3}\right)^{\frac{1}{2}} & =216\\
\left(6^{3}\right) & =216 & \left(46656\right)^{\frac{1}{2}} & =216\\
216 & =216\checkmark & 216 & =216\checkmark\end{aligned}$$
:::
::::
::::{prf:example}
Solve $$(x^{2}-x-1)^{\frac{3}{2}}=\sqrt{1331}$$
:::{dropdown} Solution:
Since $$\left(x^{\frac{3}{2}}\right)^{\frac{2}{3}}=x$$ provided $x\ge0$.o $$\begin{aligned}
(x^{2}-x-1)^{\frac{3}{2}} & =\sqrt{1331}\\
(x^{2}-x-1)^{\frac{3}{2}} & =(1331)^{\frac{1}{2}}\\
\left((x^{2}-x-1)^{\frac{3}{2}}\right)^{2} & =\left((1331)^{\frac{1}{2}}\right)^{2}\\
(x^{2}-x-1)^{3} & =1331\\
\left((x^{2}-x-1)^{3}\right)^{\frac{1}{3}} & =1331^{\frac{1}{3}}\\
x^{2}-x-1 & =11\\
x^{2}-x-12 & =0\\
(x-4)(x+3) & =0\\
x & =\{4,-3\}\end{aligned}$$ Claim $x=\{4,-3\}$ is a solution set:

If $x=4$ $$\begin{aligned}
(x^{2}-x-1)^{\frac{3}{2}} & =\sqrt{1331}\\
((4)^{2}-(4)-1)^{\frac{3}{2}} & =\sqrt{1331}\\
(11)^{\frac{3}{2}} & =\sqrt{1331}\\
11^{\frac{3}{2}} & =11^{\frac{3}{2}}\checkmark\end{aligned}$$

If $x=-3$ $$\begin{aligned}
(x^{2}-x-1)^{\frac{3}{2}} & =\sqrt{1331}\\
((-3)^{2}-(-3)-1)^{\frac{3}{2}} & =\sqrt{1331}\\
(11)^{\frac{3}{2}} & =11^{\frac{3}{2}}\checkmark\end{aligned}$$ Therefore, $x=\{4,-3\}$ is the solution set to the equation $(x^{2}-x-1)^{\frac{3}{2}}=\sqrt{1331}$.
:::
::::

### The equation in Quadratic Form

:::{prf:definition}
An equation in quadratic form is written as $$au^{2}+bu+c=0,$$ where $a\ne0$ and $u$ is some algebraic expression.
:::
::::{prf:example}
Solve $$x^{2}+3x-10=0$$
:::{dropdown}
$$\begin{aligned}
x^{2}+3x-10 & =0\\
(x+5)(x-2) & =0\end{aligned}$$

this mean $x=-5$ or $x=2$.
:::
::::
::::{prf:example}
Solve $$x^{4}+3x^{2}-10=0$$
:::{dropdown}
$$\begin{aligned}
x^{4}+3x^{2}-10 & =0\\
(x^{2}+5)(x^{2}-2) & =0\end{aligned}$$ By the zero product property we have $x^{2}+5=0$ or $x^{2}-2=0$. $$x^{2}+5=0\iff x^{2}=-5$$ which has no real solution since $\sqrt{-5}$ is not a real number. Notice $\sqrt{-5}=\sqrt{(-1)(5)}=\sqrt{-1}\sqrt{5}=i\sqrt{5}\in\mathbb{C}$.

$$x^{2}+5=0\iff x^{2}=-5\iff x=\pm i\sqrt{5}$$ The second equation $$x^{2}-2=0\iff x^{2}=2\iff x=\pm\sqrt{2}$$ Therefore, the entire solution set for the equation $x^{4}+3x^{2}-10=0$ where $x\in\mathbb{C}$ is $$x=\{-\sqrt{2},\sqrt{2},-i\sqrt{5},i\sqrt{5}\}$$ If $x\in\mathbb{R}$ then the solution set would be $$x=\{-\sqrt{2},\sqrt{2}\}$$
:::
::::
::::{prf:example}
Solve $$6x^{-2}-3x^{-1}=0$$
:::{dropdown}
Let $u=x^{-1}$. Then $\left(u\right)^{2}=\left(x^{-1}\right)^{2}$ and $u^{2}=x^{-2}$. This changes the original equation to $$\begin{aligned}
6u^{2}-3u & =0\\
3u(2u-1) & =0\end{aligned}$$ by the zero product property we have $$\begin{aligned}
3u & =0\iff u=0\\
2u-1 & =0\iff u=\frac{1}{2}\end{aligned}$$ Since $u=x^{-1}$ we have $$u=0\iff x^{-1}=0\to\frac{1}{x}=0$$ which has no solution. $$u=\frac{1}{2}\iff x^{-1}=\frac{1}{2}\to\frac{1}{x}=\frac{1}{2}\to x=2.$$ Therefore, we can claim that $x=2$ is the only solution to the equation.

Check $$\begin{aligned}
6(2)^{-2}-3(2)^{-1} & =0\\
\frac{6}{2^{2}}-\frac{3}{2} & =0\\
\frac{6}{4}-\frac{3}{2} & =0\\
\frac{3}{2}-\frac{3}{2} & =0\checkmark\end{aligned}$$
:::
::::