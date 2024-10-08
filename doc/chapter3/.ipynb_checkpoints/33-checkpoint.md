# Section 3.3

## Factor Theorem and Rational Zero Theorem
:::{prf:theorem} Factor Theorem
:label: factorThm
For any polynomial $f(x)$, $x-k$ is a factor of $f(x)$ if and only if $f(k)=0$.
:::

:::{prf:theorem} Rational Zero Theorem
:label: ratZeroThm
Let $f(x)$ be a polynomial function

$$f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots +a_1x+a_0$$

If $f(\frac{p}{q})=0$, then $p$ is proportional to $a_0$ and $q$ is proportional to $a_n$.
:::

From the previous theorem, it is important to remember that it is $\frac{p}{q}$ where $p$ is associated with $a_0$ (the constant term) and $q$ is associated with $a_n$ (the leading coefficient).

### Example(s)

::::{prf:example}
:label: zeroExam1
Let $f(x)=18x^6-21x^5-49x^4+21x^3+35x^2-4$. 

List all possible rational zeros (or roots).

:::{dropdown} Solution:
Remember $p$ is associated with the constant value, $-4$. Also, $q$ is associated with the leading coefficient, $18$. Next, we will list all the factors of for $p$ and $q$.

$$p=-4:\pm 1, \pm 2, \pm 4$$

$$q=18: \pm 1, \pm 2, \pm 3, \pm 6, \pm 9, \pm 18$$

Next, we will list all the possible rational zeros with redundant ratios.

\begin{alignat*}{3}
\pm\frac{1}{1}, & \pm\frac{1}{2}, & \pm\frac{1}{3}, & \pm\frac{1}{6}, & \pm\frac{1}{9}, & \pm\frac{1}{18},\\
\pm\frac{2}{1}, & \pm\frac{2}{2}, & \pm\frac{2}{3}, & \pm\frac{2}{6}, & \pm\frac{2}{9}, & \pm\frac{2}{18},\\
\pm\frac{4}{1}, & \pm\frac{4}{2}, & \pm\frac{4}{3}, & \pm\frac{4}{6}, & \pm\frac{4}{9}, & \pm\frac{4}{18}
\end{alignat*}

Eliminating redundancy we have the following as the possible rational roots.

$$\pm 1, \pm 2, \pm 4, \pm \frac{1}{2},\pm \frac{1}{3},\pm \frac{1}{6},\pm \frac{1}{9},\pm \frac{1}{18}$$
$$\pm \frac{2}{3},\pm \frac{2}{9},\pm \frac{4}{3}, \pm \frac{4}{9}$$
:::

Factor $f(x)$ into products of linear binomials.

:::{dropdown} Solution:
From the list of possible rational zeros, we will do synthetic division.

We will first try $x=1$ (or $k=1$). After synthetic division we will discover $f(1)=0$ and $q_1(x)=18x^5-3x^4-52x^3-31x^2+4x+4$. That is,

\begin{align*}
    f(x) & = (x-1)q_1(x)\\
    & = (x-1)(18x^5-3x^4-52x^3-31x^2+4x+4)
\end{align*}

Next, we will do synthetic division on $q_1(x)$ using $k=-1$. We will get $q_1(-1)=0$ and $q_2(x)=18x^4-21x^3-31x^2+4$. That is,

\begin{align*}
    f(x) & = (x-1)q_1(x)\\
    & = (x-1)\left((x+1)q_2(x)\right)\\
    & = (x-1)(x+1)(18x^4-21x^3-31x^2+4)
\end{align*}

Next, we will do synthetic division on $q_2(x)$ using $k=2$. We will get $q_2(2)=0$ and $q_3(x)=18x^3+15x^2-x-2$. That is,

\begin{align*}
    f(x) & = (x-1)(x+1)q_2(x)\\
    & = (x-1)(x+1)\left((x-2)q_3(x)\right)\\
    & = (x-1)(x+1)(x-2)(18x^3+15x^2-x-2)
\end{align*}

Next, we will do synthetic division on $q_3(x)$ using $k=-2$. We will get $q_3(-2)=-84$. This means $x=-2$ is not a zero of the original function. We then move down the list of possible rational zeros. We will find

\begin{align*}
    q_3(4) & = 1386\\
    q_3(-4) & = -910\\
    q_3(\frac{1}{2})) & = \frac{7}{2}\\
    q_3(-\frac{1}{2})) & = 0
\end{align*}

We finally discover that $q_3(-\frac{1}{2})=0$. This means we will use synthetic division on $q_3(x)$ with $k=-\frac{1}{2}$. We will then get $q_4(x)=18x^2+6x-4$. That is,

\begin{align*}
    f(x) & = (x-1)(x+1)(x-2)q_3(x)\\
    & = (x-1)(x+1)(x-2)\left((x+\frac{1}{2})q_4(x)\right)\\
    & = (x-1)(x+1)(x-2)(x+\frac{1}{2})(=18x^2+6x-4)
\end{align*}

To find the last factors we then factor $=18x^2+6x-4$. First, $18\cdot(-4)=-72$, $12\cdot (-6)=-72$, and $12-6=6$. With that information, we can begin to factor.

\begin{align*}
    18x^2+6x-4 & = 18x^2+12x-6x-4\\
    & = 6x(3x+2)-2(3x+2)\\
    & = (3x+2)(6x-2)\\
    & = (6x-2)(3x+2)\\
    & = 2(3x-1)(3x+2)
\end{align*}

Putting everything together we have:

$$f(x)=2(x-1)(x+1)(x-2)(x+\frac{1}{2})(3x-1)(3x+2)$$
:::

List all the zeros for the function $f(x)$

:::{dropdown} Solution:
Since we know

$$f(x)=2(x-1)(x+1)(x-2)(x+\frac{1}{2})(3x-1)(3x+2)$$

The zeros of the function $f$ is: $1$, $-1$, $2$, $-\frac{1}{2}$, $\frac{1}{3}$, and $-\frac{2}{3}$.
:::
::::

## Fundamental Theorem of Algebra and Number of Zeros Theorem

:::{prf:theorem} Fundamental Theorem of Algebra
:label: FTA
Every function defined by a polynomial of degree 1 or more has at least one complex root.
:::

:::{prf:theorem} Number of Zeros Theorem
:label: numberZerosThm
A function defined by a polynomial of degree $n$ has at most $n$ distinct zeros.
:::

:::{prf:definition} Multiplicity
:label: multiplicity
The number of times a zero occurs is called the multiplicity of the zero.
:::

:::{prf:example}
:label: multExam1
Let $f(x)=(x+1)^3(x+3)(x-2)^2$. We know that the zeros of the function are $-1$, $-3$, and $2$. However, we can also say that $f$ has a zero at $x=-1$ with a multiplicity of $3$, $x=-3$ with a multiplicity of $1$, and $x=2$ with a multiplicity of $2$. The power on the individual factors determines the multiplicity.
:::

::::{prf:example}
:label: multExam2
Find a polynomial of degree three with real coefficient, zeros at $x=-3$, $x=-2$, and $x=5$, and $f(-1)=6$.
:::{dropdown} Solution:
We know that with the zeros 

$$f(x)=a(x+3)(x+2)(x-5)$$

In order to find $a$ we use $f(-1)=6$. That is, solve the following equation.

\begin{align*}
    a(-1+3)(-1+2)(-1-5) & = 6\\
    a(2)(1)(-6) & = 6\\
    a & = -\frac{6}{-12} = -\frac{1}{2}
\end{align*}

Therefore, $f(x)=-\frac{1}{2}(x+3)(x+2)(x-5)$. In expanded form we have:

$$f(x)=-\frac{1}{2} x^3 + \frac{19}{2} x + 15$$
:::
::::

## Complex Numbers

Remember $\sqrt{-1}=i$ and the following hold true.

\begin{align*}
    i & = \sqrt{-1}\\
    i^2 & = -1\\
    i^3 & = -i\\
    i^4 & = 1
\end{align*}

:::{prf:definition} Complex Conjugate
:label: complexConj
Let $z=a+ib$ where $a$ and $b$ are real numbers and $i=\sqrt{-1}$. Then we say $\overline{z}=a-ib$ and $\overline{z}$ is the conjugate of $z$.
:::

:::{prf:property} Conjugate Properties
:label: complexConjProp
Let $c$ and $d$ be complex number. Then
* $\overline{c+d} = \overline{c}+\overline{d}$
* $\overline{c\cdot d} = \overline{c}\cdot\overline{d}$
* $\overline{c^n} = \left(\overline{c}\right)^n$
:::

:::{prf:theorem} Conjugate Zero Theorem
:label: conjZeroThm
If $f(x)$ defines a polynomial having **only real coefficients** and if $z=a+ib$ is a zero of $f(x)$, then $\overline{z}=a-ib$ is also a zero..
:::

::::{prf:example}
:label: conjZeroExam1
If $f(x)=x^2-8x+25$. Find $f(4+i3)$
:::{dropdown} Solution:
\begin{align*}
    f(4+i3) & = (4+i3)^2 - 8(4+i3) + 25\\
    & = 7 + i24 - 32 - i24 + 25\\
    & = 0
\end{align*}

This means $x=4+i3$ is a zero for the function.
:::

Since $f(4+i3)$ is ??. Find all the zeros for $f$.

:::{dropdown} Solution:
Since $x=4+i3$ is a zero by the Conjugate Zero Theorem we know $x=4-i3$ is also a zero. That is,

\begin{align*}
    f(4-i3) & = (4-i3)^2 - 8(4-i3)+25\\
    & = 7-i24-32+i24+25\\
    & = 0
\end{aling*}

Therefore, the zeros for $f$ is $x=4+i3$ and $x=4-i3$.
:::
::::

::::{prf:example}
:label: conjZeroExam2
Find the polynomial with least degree having only real coefficient and zeros $x=-4$ and $x=3-i$.
:::{dropdown} Solution:
Since the polynomial has real coefficient and $x=3-i$ is a zero by the conjugate zero theorem we also know $x=3+i$ is a zero. Since $x=-4$, $x=3-i$, and $x=3+i$ are roots we have

$$f(x)=(x-(-4))(x-(3-i))(x-(3+i))$$

If we distribute we have:

$$f(x)= x^3 -2x^2 -14x +40$$
:::
::::

::::{prf:example}
:label: conjZeroExam3
Given $f(2+i)=0$, find all the zeros for the function $f(x)=x^4-x^3-17x^2+55x-50$.

Since we know $f(2+i)=0$ we have the following from polynomial long division (using sythentic division).

:::{dropdown} Solution:
$$ f(x) = (x-(2+i))(x^3 + (1+i)x^2 + (-16+3i)x + (20-i10))$$
:::

Next, using conjugate zero theorem we know $f(2-i)=0$. Using synthetic division we know.

:::{dropdown} Solution:
$$ f(x)= (x-(2+i))(x-(2-i))(x^2+3x-10)$$
:::

Next, using the remaining factor: $x^2+3x-10$ we can find the remaining zeros.

:::{dropdown} Solution:
$$x^2+3x-10=(x+5)(x-2)$$

and $x=-5$, $x=2$ are the last zeros.
:::


With all the previous work we know the zeros for $f(x)=x^4-x^3-17x^2+55x-50$ is $x=\{2,-5,2+i,2-i\}.
::::
