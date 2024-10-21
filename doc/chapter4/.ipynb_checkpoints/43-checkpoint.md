# Section 4.3

The exponential function is $f(x)=a^x$.

Let $f(x)=2^x$. Consider $f(2)=2^2=4$ and $f(3)=2^3=8$. Since $f$ is continous on $[2,3]$, $f(2)=4$, and $f(3)=8$, we know, by the intermediate value theorem there exists a $c$ in $[2,3]$ such that $f(c)=7$. In fact, there is a number such that $2^x$ is 5,6, or 7.

Remember, $\sqrt{4}=2$ because $2^2=4$. We want to find/name a function such that $f(8)=3$ becuase $2^3^=8$.

:::{prf:definition}
:label: log
For all real numbers $y$ and all positive numbers $a$ and $x$, where $a\ne 1$. Then $y=\log_a (x)$ if and only if $x=a^y$.
:::

Like, $\sqrt{4}=2$ because $2^2=4$ we have: $3=\log_2(8)$ beacuse $2^4=8$.

:::{prf:definition}
:label: logFunc
If $a>0$, $a\ne 1$ and $x>0$, then the logarithm function with base $a$ is

$$f(x)=\log_a(x)$$

* The domain is $(0,\infty)$ (which is the range of $a^x$ function).
* The range is $(-\infty,\infty)$ (which is the domain of $a^x$ function).
* The function $f$ is continuous on $(0,\infty)$.
* If $0<a<1$, then $f$ is decreasing on its domain.
* if $a>1$, then $f$ is increasing on its domain.
* The graph of $f$ has vertical asymptote $x=0$.
* The graph passes through $(\frac{1}{a},-1)$, $(1,0)$, and $(a,1)$.
:::

The graph of the logarithmic function changes based on the value of $a$.

The graph of $f(x)=\log_a(x)$ when $a>1$ we have:

![The graph of an exponential function where the base if greater than 1](images/agreateronelog.png)

The graph of $f(x)=\log_a(x)$ where $0<a<1$ we have:

![the graph of an exponentiial function where the base is between 0 and 1](images/abwzeroandoneelog.png)