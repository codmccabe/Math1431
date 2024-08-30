# Section 2.3

:::{prf:definition} Relation
:label: relation
A relation is a set of ordered pairs.
:::

A relation is a correspondence from one set of numbers to another set of numbers.

:::{prf:definition} Independent and Dependent Variables
:label: indepDepVariables
Given an ordered pair, $(x,y)$:
* The first component is the independent variable.
* The second component is the dependent variable.
:::

Next, is a definition of a special kind of relation that we commonly use in mathematics.

:::{prf:definition} Function
:label: function
A function is a relation in which, for each distinct value of the first component of the ordered pair, there is **exactly one** value of the second component.
:::

## Evaluate vs. Solve

::::{prf:example}
:label: evalVsolve1
Let $f(x)=x^2+x-6$.

Evaluate $f(0)$.
:::{dropdown} Solution:
$$f(0)=(0)^2+(0)-6=-6$$
:::

Solve $f(x)=0$.
:::{dropdown}
\begin{align*}
    x^2 + x - 6 & = 0\\
    (x+3)(x-2) & = 0
\end{align*}
The solution set is $\{-3,2\}$.
:::
::::

## Basic Function Arithmetic
::::{prf:example}
:label: basicFArith
Let $f(x)=x^2+x+1$.

Find $f(q)$.
:::{dropdown} Solution:
$$f(q)=q^2+q+1$$
:::

Find $f(x)+q$.
:::{dropdown} Solution:
$$f(x)+q = x^2+x+1+q$$
:::

Find $f(x+q)$.
:::{dropdown} Solution:
$$f(x+q)=(x+q)^2+(x+q)+1=x^2+2qx+q^2+x+q+1$$
:::

Find $f(x)+f(q)$.
:::{dropdown} Solution:
$$f(x)+f(q)=x^2+x+1+q^2+q+1$$
:::
::::

## Increasing, Decreasing, and Constant
Remember, functions are a  collection of ordered pairs. Graphing a function is a way to represent all of the ordered pairs.

:::{prf:definition} Increasing, Decreasing, and Constant.
:label: monotonicity
Suppose $f$ is defined on an interval $(a,b$. Let $x_1$ and $x_2$ be elements in the interval $(a,b$ such that $x_1<x_2$.

The function $f$ is increasing over $(a,b)$ if and only if $f(x_1)<f(x_2)$ for all $x_1,x_2$.
![Increasing over (a,b)](images/inc.png)

The function $f$ is decreasing over $(a,b)$ if and only if $f(x_1)>f(x_2)$ for all $x_1,x_2$.
![Decreasing over (a,b)](images/dec.png)

The function $f$ is constant over $(a,b)$ if and only if $f(x_1)=f(x_2)$ for all $x_1,x_2$.
![Constant over (a,b)](images/constant.png)
:::

::::{prf:example}
:label: exampleIncDecCons
Given the graph of $y=f(x)$ determine the following using open intervals:

![Graph of y=f(x)](images/exampleIncDecCons.png)

Where is $f$ increasing?
:::{dropdown} Solution:
$$(-1,0)$$
:::
Where is $f$ decreasing?
:::{dropdown} Solution:
$$(-3,-1)$$
:::
Where is $f$ constant?
:::{dropdown} Solution:
$$(0,3)$$
:::
::::

Remember when finding intervals where a function is increasing, decreasing, or constant we orientate concerning the $x$-axis. That is, when finding intervals of increasing for a function $f$ we want to see all $x$ values such that $f$ satisfies the increasing function definition.

## Domain
We will be considering the following domain situations for the beginning of the semester.

:::{prf:definition} Domain
:label: keyDomain
* The domain for the function $f(x)=x$ is the set of all $x$ such that $x$ is a real number. Or, $$\text{dom}(x)=\mathbb{R}$$
* The domain for the function $f(x)=\frac{1}{x}$ is the set of all $x$ such that $x$ is not zero. Or, $$\text{dom}(\frac{1}{x})=\{x|x\ne0\}$$
* The domain for the function $f(x)=\sqrt{x}$ is the set of all $x$ such that $x$ is greater than or equal to zero. Or, $$\text{dom}(\sqrt{x})=\{x|x\ge0\}$$
:::

:::{prf:example}
:label: exampleDomain1
Let $f(x)=\frac{x^2+x-12}{x+4}$. Find the domain of $f$.
:::{dropdown} Solution:
Remember, $\text{dom}(\frac{1}{x})=\{x|x\ne0\}$. We can use this information to find the domain of $f$. That is, we want to say the domain of $f$ is the set of all $x$ such that $x+4\ne0$. Or,

$$\text{dom}(f)=\{x|x\ne -4\}$$ 

The interval notation for this set would be $(-\infty,-4)\cup(-4,\infty)$.
:::
::::

It is important to notice in the last example that we did not simplify the function before finding the domain. Consider what would happen if we simplified $f$ and tried to find the domain. We would be very confused. The moral is; that when finding the domain of a function, do not simplify the function.