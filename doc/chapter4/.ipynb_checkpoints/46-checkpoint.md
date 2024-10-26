# Section 4.6

:::{prf:definition}
:label: expModelDef
Let $y_0$ be the amount or number present at time $t=0$. Then, under certain conditions, the amount $y$ at any time $t$ is modeled by 

$$y=y_0e^{kt}$$

where $k$ is some constant.
:::

* If $k>0$, then the model is called exponential growth.
* If $k<0$, then the model is called exponential decay.

## Exponential Growth Model

::::{prf:example}
:label: expGrowthProb1
In the year 1990 the amount of atmospheric carbon dioxide was $353$ parts per million and then in the year 2000 the amount was $375$ parts per million. Asssuming the model is exponential find the function.

:::{dropdown} Solution:
We want to find the function $f(x)=y_0e^{kx}$ where $x$ is the number of years after 1990 and $f(x)$ is the amount of atmospheric carbon dioxide in units of parts per million.

First, we will use the fact that $f(0)=353$ to find $y_0$.

\begin{align*}
    f(0) & = y_0e^{k(0)}\\
    353 & = y_0e^{0}\\
    y_0 & = 353
\end{align*}

This means the function is $f(x)=353e^{kx}$. The year 2000 means $x=10$. We will then use $f(10)=375$ to solve for $k$.

\begin{align*}
    f(10) & = 353e^{k(10)}\\
    375 & = 353e^{10k}\\
    e^{10k} & = \frac{375}{353}
\end{align*}

After composing both sides by the natural log function we have 

\begin{align*}
    \ln(e^{10k}) & = \ln\left(\frac{375}{353}\right)\\
    10k\ln(e) & = \ln\left(\frac{375}{353}\right)\\
    k & = \frac{1}{10}\cdot\ln\left(\frac{375}{353}\right)
\end{align*}

This gives the function:

$$f(x)=353e^{\frac{1}{10}\cdot\ln\left(\frac{375}{353}\right)x}$$
:::

How much atmospheric carbon dioxide will there be in the year 2020?

:::{dropdown} Solution:
The year 2020, $x=30$. That means we want to evaluate $f(30)$.

$$f(30)=353e^{\frac{1}{10}\cdot\ln\left(\frac{375}{353}\right)(30)}\approx 423$$

That is, in the eyar 2020 there will be 423 parts per million atomspheric carbon dioxide.
:::

In what year will the amount double from the amount in 2000?

:::{dropdown} Solution:
In the year 2000 the amount was 375 parts per million. We want to find $x$ such that $f(x)=560$ (double the amount in 2000).

\begin{align*}
    f(x) & = 560\\
    353e^{\frac{1}{10}\cdot\ln\left(\frac{375}{353}\right)x} & = 560\\
    e^{\frac{1}{10}\cdot\ln\left(\frac{375}{353}\right)x} & = \frac{560}{353}\\
    \ln\left(e^{\frac{1}{10}\cdot\ln\left(\frac{375}{353}\right)x}\right) & =\ln\left(\frac{560}{353}\right)
\end{align*}
:::
::::