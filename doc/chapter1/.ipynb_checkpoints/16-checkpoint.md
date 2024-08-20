# Section 1.6

We will start this section with some basic review.

## Review

A set of numbers can be written as $\{1,2,3,...\}$. 

The set of real numbers is denoted: $\mathbb{R}$.

The set of natural numbers is denoted as $\mathbb{N}$ and is equal to $\{1,2,3,...,\}$.

The set of whole numbers is the set of natural numbers including the zero element.

The set of integers is denoted $\mathbb{Z}$ and equal to $\{...,-2,-1,0,1,2,...\}$.

The set of rational numbers is denoted $\mathbb{Q}$ and equal to $\{\frac{p}{q}\,|\,p\in \mathbb{Z},q\in\mathbb{Z}-\{0\}\}$.

The set of irrational numbers are real numbers that are not rational numbers.

Given $i=\sqrt{-1}$ we have the set of complex numbers denoted $\mathbb{C}$ and equal to $\{a,b\in\mathbb{R}\,|\,a+ib\}$.

:::{prf:example}
:label: complexSolutions
The equation $x^2-1=0$ has two solutions $x=1$ and $x=-1$. However, the equation $x^2+1=0$ has no real solutions. Unless we consider $i=\sqrt{-1}$. Then we say $x^2+1=0$ has two solutions $x=i$ and $x=-i$.
:::

Suppose $n$ is a natural number then $a^n=a\cdot a\cdot a \cdots a$ where $a$ is multiplied $n$ amount of times. Considering this we have the following properties.

:::{prf:property} Laws of Exponents
:label: lawsExponents
$a^m\cdot a^n = a^{m+n}$, $\left(a^m\right)^n = a^{mn}$, $\frac{a^n}{a^m}=a^{n-m}$, $a^{-n}=\frac{1}{a^n}$, and $\frac{1}{a^n} = a^{-n}$.

Also,

$(ab)^n = a^n\cdot b^n$ and $\left(\frac{a}{b}\right)^n=\frac{a^n}{b^n}$.

For radical notation, we have:

$$\sqrt[n]{x} = x^{\frac{1}{n}}$$
:::

:::{prf:example}
:label: freshmanDream
Remember $(ab)^n=a^n\cdot b^n$; however, $(a+b)^n\ne a^n +b^n$.

That is, $(x+y)^2\ne x^2 +y^2$ because
\begin{align*}
    (x+y)^2 & = (x+y)(x+y)\\
    & = x^2+xy+xy+y^2\\
    & = x^2 + 2xy + y^2
\end{align*}
:::

## Application Problem(s)

The amount of work is equal to the rate of work times the amount of time worked, or,

$$W=rt$$

This can also be used for distance, rate, and time:

$$d=rt$$

::::{prf:example}
:label: workProblem
One printer can do a job twice as fast as another. Working together, both printers can do the job in 2 hours. How long would it take each printer, working alone, to do the job?
:::{dropdown} Solution
We know the work done for the faster printer plus the work done for the slower printer equals one job done.

$$W_f+W_s = 1 $$

Let $x$ be the number of hours the faster printer takes to complete one job. Then the rate for the faster printer is 

$$\frac{1}{x}$$ 

and the rate of the slower printer is 

$$\frac{1}{2x}$$ 

since "One printer can do a job twice as fast as another".

The time $t=2$ for the job to be done. Therefore, we have the following equation to solve:

$$\frac{1}{x}\cdot 2 + \frac{1}{2x}\cdot 2 = 1$$

Simplifying we have:
\begin{align*}
    \frac{1}{x}\cdot 2 + \frac{1}{2x}\cdot 2 & = 1\\
    \frac{2}{x}+\frac{1}{x} & = 1\\
    \frac{3}{x} & = 1
\end{align*}

This means $x=3$ is the solution to the equation.

That is, the faster printer will take 3 hours and the slower printer will take 6 hours to complete one job by them selves.
:::
::::