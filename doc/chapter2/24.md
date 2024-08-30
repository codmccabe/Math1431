# Section 2.4

:::{prf:definition} Linear Function
:label: linearFunction
Let $m$ and $b$ be any real number. Then a linear function is defined as

$$f(x)=mx+b$$
:::

When $m\ne0$ the domain and range of the $f$ is the set of all real number. However, if $m=0$ then the graph of the linear function would be a horizontal line. The domain of a function that is a horizontal line is the set of all real number and the range of the function would be $\{b\}$.

:::{prf:definition} Standard Form Line Equation
:label: standardFormLine
Let $A$, $B$, and $C$ be integers such that $A\ge0$ and $\text{gcf}(A,B,C)=1$. Then the stanard form linear equation is:
$$Ax+By=C$$
:::

::::{prf:example}
:label: exmapleStandFormLine
Write $-\frac{4}{3}x+\frac{2}{3}y=\frac{8}{3}$ in standard form.
:::{dropdown} Solution:
First, we notice that $A$, $B$, and $C$ are not integers. This can be fixed by multiplying both sides of the equation by $3$. We would then get:

$$-4x+2y=8$$

However, $A\not\ge0$. This can be fixed by multiplying by $-1$ to both sides. We would then get:

$$4x-2y=-8$$

However, $\text{gcf}(A,B,C)=2\ne1$. This can be fixed by dividing by $2$ to both sides. We would then get:

$$2x-y=-4$$

This would be the linear equation in standard form.
:::
::::

:::{prf:definition} Slope
:label: defSlope
The slope of a line is the change in $y$ values over the change in $x$ values. Or,

$$m=\frac{\Delta y}{\Delta x}$$
:::

Remember, $\Delta x = x_2 - x_1$ and $\Delta y = y_2 - y_1$. In function notation we say $y_1=f(x_1)$.

:::{prf:property} 
:label: slopeIncDecCons
Consider $m=\frac{\Delta y}{\Delta x}$.

* If $m>0$, then we say the line is increasing.
* If $m<0$, then we say the line is decreasing.
* If $m=0$, then $\Delta y = 0$, $\Delta x\ne0$, and the line is constant. We also say the line is horizontal.
* If (for some reason) $m$ is undefined, then $\Delta x=0$ and the line would be vertical. We also say the slope is undefined.
:::