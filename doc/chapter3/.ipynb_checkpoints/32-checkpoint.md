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

$$\frac{a}{b} = q+\frac{r}{b}$$

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
x-4 & )\overline{3x^{3}-2x^{2}\phantom{xx}+0x-150}\\
- & \underline{\phantom{x}3x^{3}-12x^{2}} & \leftarrow3x^{2}(x-4)\phantom{x)-(3x^{3}-2x^{2}-12xxxx)}\\
 & \phantom{)3^{3}xxxx}10x^{2}+0x & \leftarrow(3x^{3}-2x^{2}+0x)-(3x^{3}-2x^{2}-12x)\\
- & \underline{\phantom{xxxxxx}10x^{2}-40x} & \leftarrow-2(x^{2}+0x-4)\phantom{150)-(-2x^{2}+0x+))}\\
 & \phantom{xxxxxxxxxxx}40x-150 & \leftarrow(-2x^{2}+12x-150)-(-2x^{2}+0x+8)\\
- & \underline{\phantom{xxxxxxxxxxx}40x-160} & \leftarrow40(x-4)\phantom{0)-(4x-160xxxxxxxxxxx)}\\
 & \phantom{xxxxxxxxxxxxxxxx}10 & \leftarrow(40x-150)-(4x-160)\phantom{xxxxxxxxxx)}
\end{alignat*}

Next, we want to do this again but remove all the $x^n$ factors.

\begin{alignat*}{10}
& \phantom{)3x^{3}-}3\phantom{xx}10\phantom{xxxx}40\\
-4 & )\overline{3\phantom{xx}-2\phantom{xx}0\phantom{x}-150}\\
- & \underline{\phantom{)}3\phantom{xx}-4}\\
 & \phantom{)3^{3}}10\phantom{xxxx}0\\
- & \underline{\phantom{xxx}10\phantom{xxx}40}\\
 & \phantom{xxxxxxxx}40\text{\ensuremath{\phantom{x}}}-150\\
- & \underline{\phantom{xxxxxxxx}40\phantom{x}-160}\\
 & \phantom{xxxxxxxxxxxxx}10
\end{alignat*}

where $q(x)=3x^2+10x+40$ and $r(x)=10$ still. We can still remove some items from the work:

\begin{alignat*}{10}
 & \phantom{)3x^{3}-}3\phantom{xx}10\phantom{xxxx}40\\
-4 & )\overline{3\phantom{xx}-2\phantom{xx}0\phantom{x}-150}\\
- & \underline{\phantom{)}\phantom{xxx}-4}\\
 & \phantom{)3^{3}xx}10\phantom{xxxx}\\
- & \underline{\phantom{xxxxi}10\phantom{xx}40}\\
 & \phantom{xxxxxxxx}40\text{\ensuremath{\phantom{x}}}\\
- & \underline{\phantom{xxxxxxxx}40\phantom{x}-160}\\
 & \phantom{xxxxxxxxxxxxx}10
\end{alignat*}

Next, we can smash everything together to get

\begin{align*}
 & \phantom{)3x^{3}-}3\phantom{xx}10\phantom{xxxx}40\\
-4 & )\overline{3\phantom{xx}-2\phantom{xxxxx}0\phantom{x}-150}\\
- & \underline{\phantom{xxx}-12\phantom{xx}-40\phantom{x}-160}\\
 & \phantom{xxxxx}10\phantom{xxxx}40\phantom{xxx}10
\end{align*}

Finally, if we use $4$ instead of $-4$ and add down instead of subtract down we have synthetic division:

\begin{align*}
 & \phantom{)3x^{3}-}3\phantom{xxxxx}10\phantom{xxxx}40\\
4 & )\overline{3\phantom{xx}-2\phantom{xxxxx}0\phantom{x}-150}\\
+ & \underline{\phantom{xxxxx}12\phantom{xxxx}40\phantom{xxx}160}\\
 & \phantom{xxxxx}10\phantom{xxxx}40\phantom{xxxx}10
\end{align*}

Again, doing this shows that $q(x)=3x^2+10x+40$ and $r(x)=10$. We also have

$$\frac{3x^3-2x^2+0x-150}{x-4}=3x^2+10x+40+\frac{10}{x-4}$$

### Synthetic Division Examples

::::{prf:example}
:label: synDivExam1
Rewrite $\frac{5x^3-6x^2-28x-2}{x+2}$ as $q(x)+\frac{r(x)}{x+2}$.
:::{dropdown}
In this case $x-k$ we have $x+2=x-(-2)$. This means $k=-2$.

\begin{align*}
 & \phantom{xxxxxx}5\phantom{xx}-16\phantom{xxxx}4\\
-2 & )\overline{5\phantom{xx}-6\phantom{xx}-28\phantom{xx}-2}\\
+ & \underline{\phantom{xxx}-10\phantom{xxxx}32\phantom{xx}-8}\\
 & \phantom{xxx}-16\phantom{xxxxx}4\phantom{xx}-10
\end{align*}

Therefore,

$$\frac{5x^3-6x^2-28x-2}{x+2} = 5x^2 -16x +4 + \frac{-10}{x+2}$$
:::
::::

::::{prf:example}
:label: synDivExam2
Evaluate $\frac{5x^3-6x^2+3x}{x-1}$
:::{dropdown} Solution:
Here $k=1$.

\begin{align*}
 & \phantom{xxxxxx}5\phantom{xx}-1\phantom{xxxx}2\\
1 & )\overline{5\phantom{xx}-6\phantom{xxx}3\phantom{xxxxx}0}\\
+ & \underline{\phantom{xxxxxx}5\phantom{x}-1\phantom{xxxxx}2}\\
 & \phantom{xxx}-1\phantom{xxxxx}2\phantom{xxxx}2
\end{align*}

Therefore, we have $\frac{5x^3-6x^2+3x}{x-1}=5x^2-x+2+\frac{2}{x-1}$.
:::
::::

Quick reminder: $i=\sqrt{-1}$, $i^2=-1$, $i^3=-i$, and $i^4=1$.

Also,

\begin{align*}
    (2-i)(-8+4i) & = -16 + 8i + 8i - 4(-1)\\
    & = -16+16i+4\\
    & = -12+16i
\end{align*}