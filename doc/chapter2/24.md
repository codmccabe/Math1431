# Section 2.4

:::{prf:definition} Linear Function
:label: linearFunction
Let $m$ and $b$ be any real number. Then a linear function is defined as

$$f(x)=mx+b$$
:::

When $m\ne0$ the domain and range of the $f$ is the set of all real numbers. However, if $m=0$ then the linear function graph would be a horizontal line, the domain of a function that is a horizontal line is the set of all real numbers, and the function's range would be $\{b\}$.

:::{prf:definition} Standard Form Line Equation
:label: standardFormLine
Let $A$, $B$, and $C$ be integers such that $A\ge0$ and $\text{gcf}(A,B,C)=1$. Then the standard form of the linear equation is:

$$Ax+By=C$$

:::

::::{prf:example}
:label: exmapleStandFormLine
Write $-\frac{4}{3}x+\frac{2}{3}y=\frac{8}{3}$ in standard form.
:::{dropdown} Solution:
First, we notice that $A$, $B$, and $C$ are not integers. This can be fixed by multiplying both sides of the equation by $3$. We would then get:

$$-4x+2y=8$$

However, $A\not\ge0$. This can be fixed by multiplying by $-1$ on both sides. We would then get:

$$4x-2y=-8$$

However, $\text{gcf}(A,B,C)=2\ne1$. This can be fixed by dividing by $2$ on both sides. We would then get:

$$2x-y=-4$$

This would be the linear equation in standard form.
:::
::::

:::{prf:definition} Slope
:label: defSlope
The slope of a line is the change in $y$ values over the change in $x$ values. Or,

$$m=\frac{\Delta y}{\Delta x}$$

:::

Remember, $\Delta x = x_2 - x_1$ and $\Delta y = y_2 - y_1$. In function notation, we say $y_1=f(x_1)$.

:::{prf:property} 
:label: slopeIncDecCons
Consider $m=\frac{\Delta y}{\Delta x}$.

* If $m>0$, then we say the line is increasing.
* If $m<0$, then we say the line is decreasing.
* If $m=0$, then $\Delta y = 0$, $\Delta x\ne0$, and the line is constant. We also say the line is horizontal.
* If (for some reason) $m$ is undefined, then $\Delta x=0$ and the line would be vertical. We also say the slope is undefined.
:::

:::{prf:definition} Secant Line
:label: secantLine
Let $f$ be a function defined on an interval $I$ and $x_1,x_2\in I$. The average rate of change of a function $f$ from $x_1$ to $x_2$ is defined as:

$$m_{\text{ave}} = \dfrac{f(x_2)-f(x_1)}{x_2-x_1}$$

The line through these two points, $(x_1,f(x_1)$ and $(x_2,f(x_2))$, is called the **secant line**.
:::

:::{prf:Definition} Business Models
:label: bizModels
In general, we say 
* $R(x)=xp$ is the revenue function where $x$ is the number of units sold and $p$ is the price per unit. Sometimes, $p$ is a function of $x$.
* $C(x)=V(x)+F(x)$ where $V(x)$ is the variable cost function and $F(x)$ is the fixed cost function.
* $P(x)=R(x)-C(x)$
:::

::::{prf:example}
:label: bizExample
Assume that the product cost of a pager is a linear function. The fixed cost is 1500 dollars and the cost to make one pager is 100 dollars. If you plan to sell each pager for 125 dollars answer the following questions.

What is the cost function?
:::{dropdown} Solution:
$$C(x)=100x+1500$$
:::
What is the revenue function?
:::{dropdown} Solution:
$$R(x)=125x$$
:::
What is the profit function?
:::{dropdown} Solution:
\begin{align*}
    P(x) & = R(x)-C(x)\\
    & = (125x) - (100x+1500)\\
    & = 25x-1500
\end{align*}
:::
How many units must be sold before you make a profit?
:::{dropdown} Solution:
That is, solve the equation $P(x)=0$.
\begin{align*}
    P(x) & = 0\\
    25x-1500 & = 0\\
    25x & = 1500\\
    x & = \frac{1500}{25}\text{ or } 60
\end{align*}
That is, you will need to sell 60 pagers before we can make a profit.
:::
How much profit will you make when you sell zero pagers?
:::{dropdown} Solution:
That is, evaluate $P(0)$.
$$P(0)=25(0)-1500 = -1500$$
That is, you will lose 1500 dollars.
:::
::::