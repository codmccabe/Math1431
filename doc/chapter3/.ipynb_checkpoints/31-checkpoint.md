# Section 3.1

## Definitions

:::{prf:definition}
:label: polynomial
A polynomial function $f$ of degree $n$ is a non-negative integer of the form:

$$f(x)=a_n x^n + a_{n-1} x^{n-1}+\dots + a_1 x + a_0$$

where $a_n$, $a_{n-1}$, $\dots$ , $a_1$, and $a_0$ are complex numbers and $a_n\ne0$.
* We say $a_n$, $a_{n-1}$, $\dots$ , $a_1$ and $a_0$ are coefficients.
* We say $a_n$ is the leading coefficient.
:::

We have already seen two polynomial functions.

$$f(x)=c$$ 

where $c$ is some real number.
* We call this function the constant function.
* This is a monomial.
* This has a degree of zero.
* The graph of the function is a horizontal line.

$$f(x)=mx+b$$
where $m$ is the slope of the line and $b$ is the $y$ component of the $y$-intercept. Assuming $m\ne0$ we have
* This function is called a linear funciton.
* The is a binomial
* This has a degree of one.
* The graph of the function is a slanted line. Where the slant is quantified by $m$.

The next polynomial function we will look at is the **quadratic function**.

:::{prf:definition}
:label: quadFunction
A quadratic function $f$ is of the form

$$f(x)=ax^2+bx+c$$

where $a$, $b$, and $c$ are complex numbers and $a\ne0$.
* This is a trinomail
* The degree is two.
* The graph is a parabola
:::

When graphing a quadratic function we want write $ax^2+bx+c$ in the form $a(x-h)^2+k$. We do this to use translating and scaling of graph techniques learned in chapter 2.

## Vertex Formula

The graph of the parabola has two directions and has the following labels:

When $a>0$ 

![Graph of a facing up parabola labeled with vertex and axis of symmetry](images/parabolaGraph1.png)

When $a<0$

![Graph of a facing down parabola labeled with vertex and axis of symmetry](images/parabolaGraph2.png)

By writing $ax^x+bx+c$ in the form $a(x-h)^2+k$ we will know that the vertex is located at $(h,k)$. Next, we will try to find $h$ and $k$ in terms of $a$, $b$, and $c$.

First, we write $ax^2+bx+c$ in the following way and then factor out an $a$

\begin{align*}
    ax^2+bx+c & = ax^2 +b\left(\frac{a}{a}\right)x+c\\
    & = ax^2 + a\left(\frac{b}{a}\right)x+c\\
    & = a\left(x^2 + \frac{b}{a}x\right) + c
\end{align*}

Next, we look specifically at $x^2+\frac{b}{a}x$ in order to complete the square on these two terms we do the following:

$$\left(\frac{\frac{b}{a}}{2}\right)^2=\left(\frac{b}{2a}\right)^2=\frac{b^2}{4a^2}$$

This means that the term $\frac{b^2}{4a^2}$ must be added to the expression $x^2+\frac{b}{a}x$ in order to complete the square. However, we do not want to change that expression. Therefore, we do the following:

\begin{align*}
    x^2+\frac{b}{a}x & = x^2+\frac{b}{a}x + \frac{b^2}{4a^2} - \frac{b^2}{4a^2}\\
    & = \left(x+\frac{b}{2a}\right)^2 - \frac{b^2}{4a^2}
\end{align*}

We now rewrite and simplify $a\left(x^2 + \frac{b}{a}x\right) + c$ in the following way:

\begin{align*}
    a\left(x^2 + \frac{b}{a}x\right) + c & = a\left(\left(x+\frac{b}{2a}\right)^2 - \frac{b^2}{4a^2}\right)+c\\
    & = a\cdot \left(x+\frac{b}{2a}\right)^2 - a\cdot\frac{b^2}{4a^2} + c\\
    & = a\left(x+\frac{b}{2a}\right)^2 - \frac{b^2}{4a} + c\\
    & = a\left(x+\frac{b}{2a}\right)^2 + \frac{4ac-b^2}{4a}
\end{align*}

From the last step we see:

$$a\left(x+\frac{b}{2a}\right)^2 + \frac{4ac-b^2}{4a} = a\left(x-\left(-\frac{b}{2a}\right)\right)^2 + \frac{4ac-b^2}{4a}$$

This means $h=-\frac{b}{2a}$ and $k=f(-\frac{b}{2a})$ or $k=\frac{4ac-b^2}{4a}$.

With this in mind we have the following properties for graph a quadratic function.

:::{prf:property} Quadratic Function Graph
:label: graphQuadFunction
Given $f(x)=ax^2+bx+c$ we can write in the form:

$$f(x)=a(x-h)^2+k$$

where $a\ne0$, $h=-\frac{b}{2a}$ and $k=f(-\frac{b}{2a})$.

* The vertex of the parabola is at $(h,k)$ and the axis of symmetry is at $x=h$.
* If $a>0$, then the parabola opens up.
* If $a<0$, then the parabola opens down.
* If $|a|>1$, then the parabola is narrower (than $y=x^2$).
* If $0<|a|<1$, then the parabola is wider (than ($y=x^2$.
* The value of $h$ describes the horizontal shift of the parabola.
* The value of $k$ describes the vertical shift of the parabola.
:::

When it comes to the $x$ and $y$ intercepts we will go into more detail in the following sections.

### Example of Vertex and Axis of Symmetry

::::{prf:example}
:label: vertexAxisSymm
Find the axis and vertex of the parabola $f(x)=-3x^2+12x-8$.
:::{dropdown} Solution:

:::
::::