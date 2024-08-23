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

That is, the faster printer will take 3 hours and the slower printer will take 6 hours to complete one job by themselves.
:::
::::

## Solving Equations

::::{prf:example}
:label: rationalEquation1
Solve 

$$\frac{3x-1}{3} - \frac{2x}{x-1} = x$$

:::{dropdown} Solution:
First, we notice that $x\ne1$. To solve this equation we will first subtract the two rational expressions.
\begin{align*}
    \left(\frac{x-1}{x-1}\right)\cdot \frac{3x-1}{3} - \left(\frac{3}{3}\right)\cdot \frac{2x}{x-1} & = x \\
    \frac{(x-1)(3x-1)-2x(3)}{3(x-1)} & = x\\
    \frac{3x^2-4x+1-6x}{3(x-1)} & = x\\
\end{align*}

Next, we will subtract $x$ from both sides and compute the two expressions:

\begin{align*}
    \frac{3x^2-4x+1-6x}{3(x-1)} - x & = 0\\
    \frac{3x^2-4x+1-6x}{3(x-1)} - \frac{x(3(x-1))}{3(x-1)} & = 0\\
    \frac{3x^2-4x+1-6x-3x^2+3x}{3(x-1)} & = 0\\
    \frac{-7x+1}{3(x-1)} & = 0
\end{align*}

We know that $\frac{-7x+1}{3(x-1)}$ is zero whenever $-7x+1=0$ and $x\ne1$. Furthermore, we know $-7x+1=0$ whenever $x=\frac{1}{7}$. After checking we know the solution set for the equation is: $\{\frac{1}{7}\}$.
:::
::::
::::{prf:example}
:label: rationalEquation2
Solve 

$$\frac{3x+2}{x-2}+\frac{1}{x} = \frac{-2}{x^2-2x}$$

:::{dropdown} Solution:
First, notice that $x\ne2$ and $x\ne0$. To solve this equation we will add the two expressions on the left-hand side and see that the two expressions on either side of the equation share the same denominator. This means we can then set the numerator of both sides of the equation equal to each other.
\begin{align*}
    \left(\frac{x}{x}\right)\cdot \frac{3x+2}{x-2} + \frac{1}{x}\cdot \left(\frac{x-2}{x-2}\right) & = \frac{-2}{x(x-2)}\\
    \frac{3x^2 +2x +x -2}{x(x-2)} & = \frac{-2}{x(x-2)}
\end{align*}
Since the denominator of the left-hand side is equal to the right-hand side, we have, provided $x\ne2$ and $x\ne0$
\begin{align*}
    3x^2+3x-2 & = -2\\
    3x^2 + 3x & = 0\\
    3x(x+1) & = 0
\end{align*}
That is $x=0$ or $x=-1$. We claim the solution set to the equation is $\{0,-1\}$. However, $x\ne0$. Therefore, after checking we see that the solution set is: $\{-1\}$.
:::
::::
Before, we use a composition of inverse functions to solve equations like $\sqrt{x}=c$ first consider the square root operator. That is, $\sqrt{4}=2$ because $4=2^2$. In general, for all $c\ge0$, $\sqrt{x}=c$ whenever $x=c^2$. When solving the following equation we don't need to compose both sides by the $x^2$ function because we can use knowledge of the square function to find the solution intuitively.

::::{prf:example}
:label: radicalEquation1
Solve 

$$\sqrt{x}-5=2$$

:::{dropdown} Solution:

\begin{align*}
    \sqrt{x}-5 & = 2\\
    \sqrt{x} & = 7\\
    x & = 49
\end{align*}

This hold true since $\sqrt{x}=7$ because $x=7^2=49$. Therefore, the solution set for the equation (after a quick mental check) is $\{49\}$.
:::
::::

In some cases solving a rational equation isn't intuitive. In the next example, we will rely on prerequisite knowledge.

::::{prf:example}
:label: radicalEquation1
Solve 

$$\sqrt{3x+1} - \sqrt{x+4} = 1 $$

:::{dropdown} Solution:
For solving this equation we will be composing both sides by the $x^2$ function to eliminate the radical. In fact, we will be composing both sides by the $x^2$ function twice. First, we will isolate on of the radial expressions.
\begin{align*}
    \sqrt{3x+1} - \sqrt{x+4} & = 1\\
    \sqrt{3x+1} & = \sqrt{x+4} + 1\\
    \left(\sqrt{3x+1}\right)^2 & = \left(\sqrt{x+4}+1\right)^2 \\
    3x+1 & = (x+4) + 2\sqrt{x+4} + 1\\
    3x+1 & = x+5 + 2\sqrt{x+4}\\
    2x-4 & = 2\sqrt{x+4}\\
    x-2 & = \sqrt{x+4}
\end{align*}
Next, we will compose both sides by the $x^2$ function again to eliminate the last radical expression. Then we will solve for $x$.
\begin{align*}
    \left(x-2\right)^2 & = \left(\sqrt{x+4}\right)^2\\
    x^2 - 4x + 4 & = x+4\\
    x^2 -5x & = 0\\
    x(x-5) & = 0
\end{align*}
The solution to the last equation (by the zero product property) is $x=0$ and $x=5$. Claim, the solution set to the equation is $\{0,5\}$. However, to verify this claim we will check the solutions against the original equation.

When $x=0$, we have,
\begin{align*}
    \sqrt{3(0)+1} - \sqrt{0+4} & = 1\\
    \sqrt{1} - \sqrt{4} & \ne 1
\end{algin*}
This shows that $x=0$ is not a solution to the original equation.

When $x=5$, we have,
\begin{align*}
    \sqrt{3(5)+1} - \sqrt{5+4} & = 1\\
    \sqrt{9} - \sqrt{4} & = 1 \checkmark
\end{align*}
This shows that $x=5$ is a solution to the original equation.

Therefore, the solution set for the equation is $\{5\}$.
:::
::::

A quadratic equation is

$$ax^2+bx+c=0$$

where $a$, $b$, and $c$ are constants and $a\ne0$. 

We have already seen how to solve quadratic equations using GCF factoring and zero product property. In this next example, we will use "ac" method of factoring and then zero product property to solve the equation.

::::{prf:example}
:label: quadEquation1
Solve the following equation allowing real or non-real solutions.

$$x^2+3x-10=0$$

:::{dropdown} Solution:
The equation $x^2+3x-10=0$ has $a=1$ and $c=-10$. Evaluating $ac$ we have $-10$. Now, we want to find two numbers that multiply to $ac=-10$ and add to $b=3$. The two numbers are $5$ and $-2$. Next, we will rewrite the equation and use factor by grouping to complete the factoring of the quadratic expression.
\begin{align*}
    x^2+3x-10 & = 10\\
    x^2 +5x - 2x -10 & = 0\\
    x(x+5)-2(x+5) & = 0\\
    (x+5)(x-2) & = 0
\end{align*}
By the zero product property, we see that the solution to the equation is when $x=-5$ and $x=2$. Therefore, the solution set for the equation is $\{-5,2\}$.
:::
::::

The next example is a quadratic-like equation. That is, the expression can be "transformed" into a quadratic equation in order to use quadratic equation techniques to solve.

::::{prf:example}
:label: quadLikeEquation
Solve the following equation allowing real or non-real solutions.

$$x^4 + 3x^2 - 10 = 0$$

:::{dropdown} Solution:
To demonstrate how this is a quadratic-like equation consider the original equation can be rewritten as the following:

$$\left(x^2\right)^2 - 3\left(x^2\right) - 10 = 0$$

If we let $u=x^2$, then we have $u^2=x^4$ and can solve the following equation:
\begin{align*}
    u^2 + 3u - 10 & = 0\\
    (u+5)(u-2) & = 0
\end{align*}
By the zero product property, we have $u=-5$ and $u=2$. However, we want to solve for $x$. Using the fact that $u=x^2$ we have:
\begin{align*}
    u & = -5 & u & = 2\\
    x^2 & = -5 & x^2 & = 2\\
    x & = \pm i\sqrt{5} & x & = \pm \sqrt{2}
\end{align*}
Therefore, the solution set for the equation is $\{\pm i\sqrt{5},\pm \sqrt{2}\}$.
:::
::::