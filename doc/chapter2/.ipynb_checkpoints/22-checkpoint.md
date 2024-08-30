# Section 2.2

:::{prf:definition} Equation of Circle
:label: circleEquation
The equation of a circle with radius $r$ and centered at $(0,0)$ is:

$$x^2+y^2=r^2$$

The equation of a circle with radius $r$ and centered at $(h,k)$ is:

$$(x-h)^2+(y-k)^2=r^2$$
:::

## Completing the Square
Remember $(x+a)^2=x^2+2ax+a^2$ and $(x-a)^2=x^2-2ax+a^2$.

::::{prf:example}
:label: completeSquare1
Given the expression $x^2+x+C$. Find the value $C$ to complete the square.

:::{dropdown} Solution:
If $C=-2$, then $x^2+x-2=(x+2)(x-1)$ which does not complete the square. For this problem, we want to find the $C$ values to make a perfect square polynomial.

If $C=\left(\frac{1}{2}\right)^2=\frac{1}{4}$ then

$$x^2+x+\frac{1}{4} = \left(x+\frac{1}{2}\right)^2
:::
::::

Remember when completing the square we want the leading coefficient to be one.

::::{prf:example}
:label: completeSquare2
Using completing the square, solve the following equation:

$$ 6x^2+13x+5=0 $$
:::{dropdown} Solution:
First, we will divide by $6$ to both sides of the equation to get the leading coefficient to be one. We then get

$$x^2+\frac{13}{6} x +\frac{5}{6} = 0$$

Next, we will set up the equation for completing the square:

$$x^2 +\frac{13}{6} x + C = -\frac{5}{6} + C$$

Here, we want to find $C$ that will complete the square.

$$C=\left(\frac{\frac{13}{6}}{2}\right)^2 = \left(\frac{13}{12}\right)^2=\frac{169}{144}$$

Substituting the $C=\frac{169}{144}$ back into the equation and solving for $x$ we have:
\begin{align*}
    x^2 +\frac{13}{6} x + C & = -\frac{5}{6} + C\\
    x^2 +\frac{13}{6} x + \frac{169}{144} & = -\frac{5}{6} + \frac{169}{144}\\
    \left(x+\frac{13}{12}\right)^2 & = \frac{49}{144}
    x+\frac{13}{12} & = \pm \sqrt{\frac{49}{144}}\\
    x & = \frac{13}{12} \pm \frac{7}{12}
\end{align*}
That is, the solution set is $\{-\frac{1}{2},-\frac{5}{3}\}$.
:::
::::

## General to Standard Form Circle Equation

Next, we will use the knowledge of completing the square to write $x^2+y^2+Dx+Ey+F=0$ to $(x-h)^2+(y-k)^2=r^2$. This way we will be able to identify the circle's center and radius.

::::{prf:example}
:label: genSndCircle
Given $2x^2+2y^2+2x-6y=45$. Rewrite the equation in the form $(x-h)^2+(y-k)^2=r^2$ then find the center and radius of the resulting circle.
:::{dropdown} Solution:
First, we will divide both sides of the equation by $2$.

$$ x^2 + y^2 + x - 3y = \frac{45}{2} $$

Next, we will set up the completing the square for the $x$ expression and the $y$ expression.

$$ x^2 + x + C_x + y^2 - 3y + C_y = \frac{45}{2} + C_x + C_y$$

Next, we will find $C_x$ and $C_y$ to complete the square.

$$ C_x = \left(\frac{1}{2}\right)^2 = \frac{1}{4} $$

$$ C_y = \left(\frac{-3}{2}\right)^2 = \frac{9}{4} $$

Substituting $C_x=\frac{1}{4}$ and $C_y=\frac{9}{4}$ back into the equation we have
\begin{align*}
    x^2 + x + C_x + y^2 - 3y + C_y & = \frac{45}{2} + C_x + C_y\\
    x^2 + x + \frac{1}{4} + y^2 - 3y + \frac{9}{4} & = \frac{45}{2} + \frac{1}{4} + \frac{9}{4}\\
    \left(x+\frac{1}{2}\right)^2 + \left(y-\frac{3}{2}\right)^2 & = 25
\end{align*}
Therefore, the center of the graph is $(-\frac{1}{2},\frac{3}{2})$ and the radius is $r=5$.

Remember the standard form is $(x-h)^2+(y-k)^2=r^2$. We can rewrite our result as follows to identify the center and radius clearly:
\begin{align*}
    \left(x+\frac{1}{2}\right)^2 + \left(y-\frac{3}{2}\right)^2 & = 25\\
    \left(x-(-\frac{1}{2})\right)^2 + \left(y-\frac{3}{2}\right)^2 & = 5^2
\end{align*}
:::
::::

::::{prf:example}
:label: genSndCircle
Given $x^2+y^2+6x+8y+9=0$. Rewrite the equation in the form $(x-h)^2+(y-k)^2=r^2$ then find the center and radius of the resulting circle.
:::{dropdown} Solution:
First, we will set up the completing the square:

$$x^2 + 6x + C_x + y^2 + 8y + C_y = -9 + C_x + C_y$$

Next, we will find $C_x$ and $C_y$.

$$C_x = \left(\frac{6}{2}\right)^2 = (3)^2 = 9$$

and

$$C_y=\left(\frac{8}{2}\right)^2 = (4)^2 = 16$$

Substituting those values we have:
\begin{align*}
    x^2 + 6x + 9 + y^2 + 8y + 16 & = -9 + 9 + 16\\
    (x+3)^2 + (y+4)^2 & = 16
\end{align*}
Therefore, the center of the circle is $(-3,-4)$ and the radius is $r=4$.
:::
::::

