# Section 3.2

## Real Number Division Algorithm

:::{prf:definition} Division Algorithm (Real Numbers)
:label: divAlgRealNumbers
Let $a$ and $b$ be any real number where $b\ne0$. Then there exists a unique real number $q$ and $r$ such that 

$$a=b\cdot q+r$$

where $0<r<b$ or $r=0$.
:::

:::{prf:example}
:label: divExample1
If we look at $12$ and $3$ we know that

$$12=3\cdot 4 + 0$$

This can be shown by doing long division:

\begin{alignat*}{10}
& \phantom{11}4\\
3 & )\overline{12}\\
- & \underline{\phantom{)}12} & \leftarrow4(3)\phantom{--}\\
 & \phantom{)1}0 & \leftarrow12-12
\end{alignat*}

If we look at $13$ and $3$ we know that

$$13 = 3\cdot 4 + 1$$

This can be shown by doing long division:

\begin{alignat*}{10}
& \phantom{11}4\\
3 & )\overline{13}\\
- & \underline{\phantom{)}12} & \leftarrow4(3)\phantom{--}\\
 & \phantom{)1}1 & \leftarrow13-12
\end{alignat*}
:::

Since the division algorithm for real numbers is $a=bq+r$ we know that if we divide both sides by $b$ we have

$$\frac{a}{b} = q+\frac{r}{b}$

We will use this fact to rewrite polynomial over polynomial expressions later on. For example, we know that $13=3(4)+1$. If we divide both sides by $3$ we have: $\frac{13}{3} = 4+\frac{1}{3}$.

## Division Algorithm for Polynomials

:::{prf:definition} Division Algorithm for Polynomials
:label: divAlgPolynomial
Let $f(x)$ and $g(x)$ be polynomials with $g(x)$ of lesser degree than $f(x)$ and $g(x)$ is of degree one or higher. Then there exists a unique $q(x)$ and $r(x)$ such that 

$$f(x)=g(x)\cdot q(x)+r(x)$$

where $0<\text{deg}(r(x))<\text{deg}(g(x))$ or $\text{deg}(r(x))=0$.
:::

:::{prf:example}
:label: polyLongExam1
If we look at $x^2+3x+2$ and $x+1$ we know that 

$$x^2+3x+2=(x+1)(x+2)+0$$ 

by factoring $x2+3x+2$. This can also be done by polynomial long division.

\begin{alignat*}{10}
 & \phantom{)x^{2}+)}x+2\\
x+1 & )\overline{x^{2}+3x+2}\\
- & \underline{\phantom{)}x^{2}+x} & \leftarrow x(x+1)\phantom{)-(x^{2}+x)}\\
 & \phantom{)x^{2}+)}2x+2 & \leftarrow(x^{2}+3x)-(x^{2}+x)\\
 & \underline{-\phantom{x^{2}))}2x+2} & \leftarrow2(x+1)\phantom{))))(2x+2}\\
 & \phantom{-x^{2}))2x+)}0 & \leftarrow(2x+2)-(2x+2)
\end{alignat*}
:::

From the previous example, we also know that

$$\frac{x^2+3x+2}{x+1}=(x+2)$$

Let's do another polynomial long-division problem.

::::{prf:example}
:label: polyLongExam2
Use polynomial long division to evaluate $\frac{3x^3-2x^2-150}{x^2-4}$.
:::{dropdown} Solution:
We should first notice that the numerator and denominator are missing an $x$ term. This would be like saying $12$ is the same as $102$. Therefore, we must first rewrite the quotient.

$$\frac{3x^3-2x^2+0x-150}{x^2+0x-4}$$

Next, we have the following setup

\begin{align*}
x^{2}+0x-4 & )\overline{3x^{3}-2x^{2}+0x-150}
\end{align*}

Then we start the polynomial long division

\begin{alignat*}{10}
 & \phantom{)3x^{3}-2x^{2}+)}3x-2\\
x^{2}+0x-4 & )\overline{3x^{3}-2x^{2}+0x-150}\\
- & \underline{\phantom{)}3x^{3}-0x^{2}-12x} & \leftarrow3x(x^{2}+0x-4)\phantom{x)-(3x^{3}-2x^{2}-12)}\\
 & \phantom{)3^{3}}-2x^{2}+12x-150 & \leftarrow(3x^{3}-2x^{2}+0x)-(3x^{3}-2x^{2}-12x)\\
- & \underline{\phantom{xx}-2x^{2}+0x\phantom{x}+8} & \leftarrow-2(x^{2}+0x-4)\phantom{150)-(-2x^{2}+0x+))}\\
 & \phantom{xxxxxxxx}12x-158 & \leftarrow(-2x^{2}+12x-150)-(-2x^{2}+0x+8)\\
\end{alignat*}

Therefore, we have

$$\frac{3x^3-2x^2-150}{x^2-4}=3x-2+\frac{12x-158}{x^2-4}$$
:::
::::

## Synthetic Division

In **special cases**, we can use a method called synthetic division instead of polynomial long division. We can use synthetic division when a polynomial is divided by a binomial $x-k$. This means the previous example could not be done by synthetic division.

Consider the following polynomial long division of $\frac{3x^3-2x^2+0x-150}{x-4}$. Notice that the denominator satisfied the $x-k$ requirement. We then have

\begin{alignat*}{10}
 & \phantom{)3x^{3}-}3x^{2}+10x+40\\
x-4 & )\overline{3x^{3}-2x^{2}+0x-150}\\
- & \underline{\phantom{)}3x^{3}-4x^{2}} & \leftarrow3x^{2}(x-4)\phantom{x)-(3x^{3}-2x^{2}-12xxxx)}\\
 & \phantom{)3^{3}}10x^{2}+0x & \leftarrow(3x^{3}-2x^{2}+0x)-(3x^{3}-2x^{2}-12x)\\
- & \underline{\phantom{xx}10x^{2}-40x} & \leftarrow-2(x^{2}+0x-4)\phantom{150)-(-2x^{2}+0x+))}\\
 & \phantom{xxxxxxxx}40x-150 & \leftarrow(-2x^{2}+12x-150)-(-2x^{2}+0x+8)\\
- & \underline{\phantom{xxxxxxxx}40x-160} & \leftarrow40(x-4)\phantom{0)-(4x-160xxxxxxxxxxx)}\\
 & \phantom{xxxxxxxxxxxxxx}10 & \leftarrow(40x-150)-(4x-160)\phantom{xxxxxxxxxx)}
\end{alignat*}