# Section 4.1

:::{prf:definition} Relation
:label: relation
A relation is a set of ordered pairs.
:::

:::{prf:definition} Function
:label: function
A function is a relation in which, for each distinct value of the first component of the ordered pair, there is **exactly one** value of the second component.
:::

Functions are a special type of relation. The following is a special condition on functions.

:::{prf:definition} One-to-one Functions
:label: onetooneFunction
A function $f$ is one-to-one function if, for each element $a$ and $b$ in the domain of $f$

$$ a\ne b \implies f(a)\ne f(b)$$

That is, different values in the domain correspond to different range values.
:::

* The following set $\{(1,4),(1,5),(2,6),(3,7)\}$ is a relation but not a function since $1\to4$ and $1\to 5$.
* The following set $\{(1,4),(2,4),(3,4)\}$ is a relation and a function, but not a one-to-one function since $4$ corresponds to $1$, $2$, and $3$.
* The following set $\{(1,4),(2,5),(3,6)\}$ is a relation, a function, and a one-to-one function.

:::{prf:example}
:label: listOnetooneFunctions
* $f(x)=x$ is a one-to-one function.
* $f(x)=mx+b$ is a one-to-one function.
* $f(x)=x^2$ is not a one-to-one function since $1\ne-1$, $f(-1)=(-1)^2=1$, and $f(1)=(1)^2=1$.
* $f(x)=x^2$ with a domain of $[0,\infty)$ is a one-to-one function.
* $f(x)=x^3$ is a one-to-one function.
:::

We have the following, like the vertical line test for determining if a graph is for a function.

:::{prf:property}
:label: horLineTest
Horizontal line test for one-to-one function. A function is one-to-one if every horizontal line intersects the graph of the function at most once.
:::

A function must be one-to-one in order for the function to have an inverse.

:::{prf:definition}
:label: inverseFunction
Let $f$ be a one-to-one function. Then $g$ is the inverse of $f$ if $f(g(x))=x$ for all $x$ in the domain of $g$ and $g(f(x))=x$ for all $x$ in the domain of $f$.
:::

:::{prf:property}
:label: domRangeProp
Let $f$ and $f^{-1}$ exists. 
* The domain of $f$ is equal to the range of $f^{-1}$.
* The randge of $f$ is equal to the domain of $f^{-1}$.
* The graph of $y=f^{-1}(x)$ is the graph of $y=f(x)$ but reflected about the line $y=x$.
:::

::::{prf:example}
:label: inverseFunctionExam1
Let $f(x)=8x+5$ and $g(x)=\frac{1}{8}x-\frac{5}{8}$. Show $g$ is the inverse of $f$.

Scratch work:

:::{dropdown} Solution:
\begin{align*}
    f(g(x)) & = 8\left(\frac{1}{8}x-\frac{5}{8}\right)+5\\
    & = x-5+5\\
    & = x
\end{align*}
\begin{align*}
    g(f(x)) & = \frac{1}{8}\left(8x+5\right)-\frac{5}{8}\\
    & = x+\frac{5}{8}-\frac{5}{8}\\
    & = x
\end{align*}
:::

:::{dropdown} "Proof:"
Since $f$ is a linear function we say $f$ is a one-to-one function. Furthermore, since $f(g(x))=x$ and $g(f(x))=x$ we say $g$ is the inverse of $f$.
:::
::::

When $g(x)$ is the inverse of $f(x)$, we say, $g(x)=f^{-1}(x)$.  

::::{prf:example}
:label: inverseExam2
Let $f(x)=2x+5$ and $g(x)=\frac{1}{2}x-5$. Show $g$ is not the inverse of $f$.
:::{dropdown} Solution:
\begin{align*}
    f(g(x)) & = 2\left(\frac{1}{2}x-5\right)+5\\
    & = x-\frac{5}{2}+5\\
    & = \ne x
\end{align*}

Since $f(g(x))\ne x$ we know $g$ is not the inverse of $f$.
:::
::::

:::{prf:exmaple}
:label: inverseExam3
Let $f(x)=8x+5$ and $g(x)=\frac{1}{8}x-\frac{5}{8}$. We have shown, $g(x)=f^{-1}(x)$.

Before the discussion of the inverse function, we would solve the equation $f(x)=2$ in the following way.

\begin{align*}
    f(x) & = 2\\
    8x+5 & = 2\\
    8x & = -3\\
    x & = -\frac{3}{8}
\end{align*}

After the discussion of the inverse function, we would solve the equation $f(x)=2$ in the following way.

\begin{align*}
    f(x) & = 2\\
    f^{-1}(f(x)) & = f^{-1}(2)\\
    x & = \frac{1}{8}(2)-\frac{5}{8}\\
    & = -\frac{3}{8}
\end{align*}
:::

