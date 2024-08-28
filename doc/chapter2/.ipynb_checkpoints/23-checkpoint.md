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