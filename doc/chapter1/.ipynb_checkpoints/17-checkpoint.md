# Section 1.7

:::{prf:definition}
:label: inequality
An inequality says that one expressions is:
* greater than ($>$)
* greater than equal to ($\ge$)
* less than ($<$), or
* less than equal to ($\le$)
another expression.
:::

![inequality!](images/inequality.png "Table of information about inequality notations")

![inequality2!](images/inequality2.png "Second part of the information")

First, we will look at a simple example involving inequality notations.

::::{prf:example}
:label: linearInequality1
Solve $1-5x>11$.

:::{dropdown} Solution:
We solve the inequality the following way. Notice that when dividing by $-5$ we flip the inequality.
\begin{align*}
    1-5x & > 11\\
    -5x & > 10\\
    x & < -2
\end{align*}

Next, we consider what the graph will look like. To do this, we will test a value against the original inequality. If $1-5x>11$ at $x=0$ then we will graph towards zero on the number line. If the inequality is false then we graph away from zero.

Testing $x=0$ we have:
\begin{align*}
    1-5(0) & > 11\\
    1 & \not> 11
\end{align*}

This means we graph away from zero as follows:

The graph of the solution is: ![graph!](images/linearInequality1.png)

From the graph, we see the solution set is $\{x\,|\,x<-2\}$. Also, the interval notation is $(-\infty,-2)$.
:::
::::

Next, we will look at a nonlinear inequality. Remember, if $ab=0$ then $a=0$ or $b=0$ by the zero product property. However, we do not use this property for nonlinear inequalities.

::::{prf:example}
:label: nonlinearInequality1
Solve $x^2-x-12>0$.

:::{dropdown} Solution:
First, we want to know where $x^2-x-12$ is zero. 
\begin{align*}
    x^2-x-12 & = 0\\
    (x-4)(x+3) & = 0
\end{align*}
By the zero product property, we know $x=4$ or $x=-3$.

With this information we have now partitioned the real number line into three subintervals: $(-\infty,-3)$, $(-3,4)$, and $(4,\infty)$. Since the polynomial is defined everywhere and is continuous everywhere we know that if $x^2-x-12$ is greater than zero at some point on a subinterval then the expression is greater than zero for all $x$ values in that subinterval.

That is, we will test values in each subinterval.

* When $x=-4$ we have $(-4)^2-(-4)-12 > 0$ which is **true**. This means we will shade to the left of $x=-3$ on the number line.
* When $x=0$ we have $(0)^2-(0)-12 > 0$ which is **false**. This means we will not shade the middle interval.
* When $x=5$ we have $(5)2-(5)-12 > 0$ which is **true**. This means we will shade to the right of $x=4$.

The graph of the solution should look like the following: ![Nonlinear Inequality!](images/nonlinearInequality1.png)

Based on the graph the solution set is $\{x\,|\,x<-3\text{ or }4<x\}$. The interval notation would be $(-\infty,-3)\cup(4,\infty)$.
:::
::::