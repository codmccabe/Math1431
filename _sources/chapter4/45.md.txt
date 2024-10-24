# Section 4.5

Remember 
* $a^x=a^y$ if and only if $x=y$,
* $\log_a(x)=\log_a(y)$ if and only if $x=y$,
* $f(f^{-1}(x))=x$ and $f^{-1}(f(x))=x$, and
* $\log_a(a^x)=x$ and $a^{\log_a(x)}=x$.

## Solve Exponential Equations
::::{prf:example}
:label: expSolveExam1
Solve $8^x=24$
:::{dropdown} Solution:
First, we will compose both sides by the natural log function:

$$\ln(8^x)=\ln(24)\to x\ln(8)=\ln(24)$$

Then we will divide both sides by $\ln(8)$.

$$\frac{x\cancel{\ln(8)}}{\cancel{\ln(8)}}=\frac{\ln(24)}{\ln(8)}$$

Therefore, the solution set is $\{\frac{\ln(24)}{\ln(8)\}$.
:::
::::

The previous answer can be represented in many different ways. 

$$\frac{\ln(24)}{\ln(8)}=\log_8(24)$$

which could lead to:

$$\log_8(24)=\log_8(8\cdot 3)=\log_8(8)+\log_8(3)=1+\log_8(3)$$

or

$$1+\log_8(3) = 1+\frac{\ln(8)}{\ln(3)}$$

It is also important to notice that $\frac{\ln(24)}{\ln(8)}\ne \ln(3)$.

::::{prf:example}
:label: expSolveExam2
Solve $e^{4x}e^{x-1}=5e$.
:::{dropdown} Solution:
First, we will apply the law $a^m a^n = a^{m+n}$

$$e^{4x}e^{x-1}=e^{4x+(x-1)}=e^{5x-1}$$

Then we have:

$$e^{5x-1}=5e$$

Next, we will compose both sides by the natural log

\begin{align*}
    \ln(e^{5x-1}) & = \ln(5e)\\
    (5x-1)\ln(e) & = \ln(5e)\\
    5x-1 & = \ln(5e)
\end{align*}

Next, add one to both sides then divide by 5 to solve for $x$.

\begin{align*}
    5x-1 & = \ln(5e)\\
    5x & = \ln(5e)+1\\
    x & = \frac{\ln(5e)+1}{5}
\end{align*}

Which can written as

\begin{align*}
    \frac{\ln(5e)+1}{5} & = \frac{\ln(5)+\ln(e)+1}{5}\\
    & = \frac{\ln(5)+1+1}{5}\\
    & = \frac{\ln(5)+2}{5}
\end{align*}

The solution set is $\{\frac{\ln(5)+2}{5}\}$
:::
::::

::::{prf:example}
:label: expSolveExam3
Solve $e^{2x}-4e^x+3=0$
:::{dropdown} Solution:
First, we will rewrite the equation in the following way

$$\left(e^x\right)^2-4\left(e^x\right)+3=0$$

Then see this is a "quadratic-like" equation. Let $u=e^x$, then $u^2=e^{2x}$ and

\begin{align*}
    u^2 - 4u + 3 & = 0\\
    (u-3)(u-1) & = 0
\end{align*}

With $u=3$ and $u=1$ as solutions, we substitute $u=e^x$.

In the case $u=3$, we have, $e^x=3$. After composing both sides of the equation by the natural log we have $x=\ln(3)$.

In the case $u=1$, we have $e^x=1$. After composing both sides of the equation by the natural log we have $x=\ln(1)=0$.

Therefore, the solution set is $\{0,\ln(3)\}$.
:::
::::

::::{prf:example}
:label: expSolveExam4
Solve $e^{2x}+e^x-6=0$.

:::{dropdown} Solution:
First, rewrite the equation as follows

$$\left(e^x)\right)^2+\left(e^x\right)-6=0$$

Let $u=e^x$, then $u^2=e^{2x}$ and 

\begin{align*}
    u^2 + u - 6 & = 0\\
    (u+3)(u-2) & = 0
\end{align*}

For the case $u=-3$, we have, $e^x=-3$ which has no solution. Remember $\ln(-3)$ is undefined.

For the case $u=2$, we have, $e^x=2$ which has a solution of $x=\ln(2)$.

Therefore, the solution set is $\{\ln(2)\}$.
:::
::::

## Solve Logarithmic Equations

