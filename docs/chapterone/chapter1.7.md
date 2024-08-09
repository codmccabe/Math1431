# Section 1.7 - Inequalities

An **inequality** says that one expression is greater than, greater than, or equal to, less than, or less than or equal to another.

:::{prf:property} Properties of Inequality
Let $a$, $b$, and $c$ represent real numbers.

1.  If $a<b$, then $a+c<b+c$.

2.  If $a<b$ and $c>0$, then $ac<bc$.

3.  If $a<b$ and $c<0$, then $ac>bc$.
:::
(Replace $<$ with {$>$, $\le$, or $\ge$} and results are similar. Except for when looking at conditions on $c$.)

## Linear Inequalities

:::{prf:definition}
A linear inequality in one variable is an inequality that can be written in the form $$ax+b>0,$$ where $a$ and $b$ are real numbers and $a\ne0$.
:::
(Replace $<$ with {$>$, $\le$, or $\ge$} and results are similar.)

:::{table}
| Set-Builder Notation| Verbal Description| Interval Notation|
|---|---|---|
|$\{x\,\|\,x>a\}$|The set of real numbers greater than $a$.|$(a,\infty)$|
|$\{x\,\|\,x\ge a\}$|The set of real numbers greater than or equal to $a$.|$[a,\infty)$|
|$\{x\,\|\,x<a\}$|The set of real numbers less than $a$.|$(-\infty,a)$|
|$\{x\,\|\,x\le a\}$|The set of real numbers less than or equal to $a$.|$(-\infty,a]$|
|$\{x\,\|\,a<x<b\}$|The set of real numbers between $a$ and $b$.|$(a,b)$|
|$\{x\,\|\,a\le x\le b\}$|The set of real numbers between $a$ and $b$, inclusive.|$[a,b]$|
|$\{x\,\|\,a<x\le b\}$|The set of real numbers greater than $a$ and less than or equal to $b$.|$(a,b]$|
|$\{x\,\|\,a\le x<b\}$|The set of real numbers greater than or equal to $a$ and less than $b$.|$[a,b)$|
|$\{x\,\|\,x<a\text{ or }x>b\}$|The set of real numbers less than $a$ or greater than $b$.|$(-\infty,a)\cup(b,\infty)$|
|$\{x\,\|\,x\in\mathbb{R}\}$|The set of all real numbers|$(-\infty,\infty)$|
:::
::::{prf:example}
In Business, the Profit function is the difference between the Revenue function and the Cost function, i.e., $$P(x)=R(x)-C(x)$$ where $x$ is the number of units produced and sold.

Ideally business would like Profit to be positive: $$P(x)>0.$$

Use $P(x)=R(x)-C(x)$ and rewrite $P(x)>0$ in terms of $R(x)$ and $C(x)$.
:::{dropdown} Solution:
\begin{align*}
P(x) & >0\iff R(x)-C(x)>0\\
 & \iff R(x)>C(x)
\end{align*}
:::
Let $R(x)=45x$ and $C(x)=30x+5250$. Find when the profit is positive.
:::{dropdown} Solution:
\begin{align*}
R(x) & >C(x)\\
45x & >30x+5250\\
15x & >5250\\
x & >\frac{5250}{15}\\
x & >350
\end{align*}
:::
Interpret the results.
:::{dropdown} Solution:
This means we expect to maintain positive profits when more than 350 units are produced and sold. (Why?)
:::
::::
## Quadratic Inequality

:::{prf:definition}
A quadratic inequality is an inequality that can be written in the form $$ax^{2}+bx+c*0,$$ where $*$ is $\{<,>,\le,\ge\}$, $a,b,c\in\mathbb{R}$, and $a\ne0$.
:::
:::::{prf:example}
Solve the quadratic inequality $$x^{2}-x-12<0$$
::::{dropdown} Solution:
Note $x^{2}-x-12<0$ occurs at the red curve:
:::{tikz}
    [scale=0.2]
    \draw[latex-latex,blue,domain=-3.66:4.65]
		plot(\x,{pow(\x,2)-\x-12})
	;
	\draw[red,domain=-3:4,thick]
		plot(\x,{pow(\x,2)-\x-12})
	;
	\draw[<->](-5,0)--(5,0)node[below right]{$x$};
	\draw[<->](0,-15)--(0,5)node[above right]{$y$};
	\draw
		(-3,2pt)--(-3,-2pt)node[below]{-3}
		(4,2pt)--(4,-2pt)node[below]{4}
	;
	\foreach \x in {5,4,...,-13,-14}
		\draw(-2pt,\x)--(2pt,\x);
:::
Notice that if we first know when $x^{2}-x-12=0$ we can start to figure out when $x^{2}-x-12<0$ .

When is $x^{2}-x-12=0$?

$$\begin{aligned}
x^{2}-x-12 & =0\\
(x-4)(x+3) & =0\\
x & =4\\
x & =-3\end{aligned}$$

When is $x^{2}-x-12$ positive?

* If $x$ is $-4$ then what? (why ask about when $x=-4$?)
* If $x$ is $5$ then what? (why ask about when $x=5$?)

what is $x^{2}-x-12$ negative?

* If $x=0$ then what? (why ask when $x=0$?)
::::
:::::

This method can be generalized in the following way.

:::{prf:algorithm} Solving quadratic inequality
:nonumber:
1.  What was the first thing we did to solve the original inequality? ($ax^{2}+bx+c=0$)
2.  After finding when $ax^{2}+bx+c=0$ we identified how many subintervals? (three (or two) subintervals)
3.  In those three subintervals we did what in those subintervals? (we tested if $ax^{2}+bx+c$ is positive or negative)
:::

:::::{prf:example}
:label: firstinequality
Solve $$2x^{2}+5x-12\ge0$$
::::{dropdown} Solution:
First, we will solve $$\begin{aligned}
2x^{2}+5x-12 & =0\\
2x^{2}+8x-3x-12 & =0\\
2x(x+4)-3(x+4) & =0\\
(x+4)(2x-3) & =0\\
x & =\{-4,\frac{3}{2}\}\end{aligned}$$

Second, identify three subintervals: $(-\infty,-4]\cup[-4,\frac{3}{2}]\cup[\frac{3}{2},\infty)$.

Third, $$\begin{aligned}
2*(-5)^{2}+5*(-5)-12 & =13\\
2*(0)^{2}+5*(0)-12 & =-12\\
2*(2)^{2}+5*(2)-12 & =6\end{aligned}$$ From the test values we see the solution set is: $$\{x\,|\,x\le-4\lor\frac{3}{2}\le x\}=(-\infty,-4]\cup[\frac{3}{2},\infty)$$
:::{tikz}
    \draw[white](0,-1)--(0,1);
    \draw[<->](-4,0)--(4,0)node[below right]{$x$};
	\draw[latex-{]},thick,blue](-4,0)--(-1,0)node[below]{$-4$};
	\draw[{[}-latex,thick,blue](1,0)node[below]{$\frac{3}{2}$}--(4,0);
:::
::::
:::::
::::{prf:example}
:label: 17rocket
If an object is launched from ground level with an initial velocity of 144 feet per second, its height $s$ in feet $t$ seconds after launching is $$s=-16t^{2}+144t.$$ When will the object be greater than 128 feet above ground level?
:::{dropdown} Solution:
Solve the inequality $$128>-16t^{2}+144t$$ First, we will solve $$\begin{aligned}
128 & =-16t^{2}+144t\\
16t^{2}-144t+128 & =0\\
16\left(t-8\right)\left(t-1\right) & =0\end{aligned}$$ The solution set is $t=\{1,8\}$.

Second, identify the three subintervals $$[0,1],[1,8],[8,9].$$

Third, test values at each subinterval. $$\begin{aligned}
-16(0)^{2}+144*(0) & =0<128\\
-16(2)^{2}+144*(2) & =224>128\checkmark\\
-16(9)^{2}+144*(9) & =0<128\end{aligned}$$

This means the solution set for the inequality $$\{x\,|\,1\le x\le8\}=[1,8]$$
:::
::::

## Other Inequalities

::::{prf:example}
:label: 17rationalInequality1
Solve $$\dfrac{6x+1}{2x-3}<6$$
:::{dropdown} Solution:
First, we solve $$\dfrac{6x+1}{2x-3}=6$$ and note that $\dfrac{6x+1}{2x-3}$ is defined for all $x$ such that $x\ne\frac{3}{2}$. Since $x\ne\frac{3}{2}$ we can validly multiply by $2x-3$ to both sides of the original equation. (It is important to make this observation before multiplying by $2x-3$ to both sides.) $$\begin{aligned}
\dfrac{6x+1}{2x-3} & =6\\
\cancel{(2x-3)}\left(\dfrac{6x+1}{\cancel{2x-3}}\right) & =6(2x-3)\\
6x+1 & =12x-18\\
\cancel{6x-6x}+1+18 & =12x-6x\cancel{-18+18}\\
19 & =6x\\
x & =\{\frac{19}{6}\}.\end{aligned}$$ 
Important to identify: $$\dfrac{6x+1}{2x-3}=6\iff x=\frac{19}{6}$$ $$\dfrac{6x+1}{2x-3}\text{ is undefined when $x=\frac{3}{2}.$}$$

Second, identify the different subintervals $$(-\infty,\frac{3}{2}),(\frac{3}{2},\frac{19}{6}],[\frac{19}{6},\infty)$$

Third, test each of the subintervals $$\begin{aligned}
\dfrac{6*(0)+1}{2*(0)-3} & =-\frac{1}{3}<6\checkmark\\
\dfrac{6*(2)+1}{2*(2)-3} & =13>6\\
\dfrac{6*(6.5)+1}{2*(6.5)-3} & =4<6\checkmark\end{aligned}$$

This means the solution set for the inequality $$\{x\,|\,x<\frac{3}{2}\lor x>\frac{19}{6}\}=(-\infty,\frac{3}{2})\cup[\frac{19}{6},\infty)$$
:::
::::
::::{prf:example}
:label: 17rationalInequality2
Solve $$-3\le\dfrac{3x-4}{-5}<4$$
:::{dropdown} Solution:
In this case there is two inequalities to solve $$-3\le\dfrac{3x-4}{-5}\text{ and }\dfrac{3x-4}{-5}<4$$

First, solve the following two cases:

Solve $-3=\dfrac{3x-4}{-5}$ $$\begin{aligned}
-3 & =\dfrac{3x-4}{-5}\\
(-5)\cdot\left(-3\right) & =\left(\dfrac{3x-4}{\cancel{-5}}\right)\cancel{(-5)}\\
15 & =3x-4\\
15+4 & =3x\cancel{-4+4}\\
19 & =3x\\
x & =\frac{19}{3}\end{aligned}$$

Solve $\dfrac{3x-4}{-5}=4$ $$\begin{aligned}
\dfrac{3x-4}{-5} & =4\\
(-5)\cdot\left(\dfrac{3x-4}{-5}\right) & =(4)\cdot(-5)\\
3x-4 & =-20\\
3x\cancel{-4+4} & =-20+4\\
3x & =-16\\
x & =-\dfrac{16}{3}\end{aligned}$$

Second, identify the different subintervals $$(-\infty,-\frac{16}{3}),(-\frac{16}{3},\frac{19}{3}),(\frac{19}{3},\infty)$$

Third, test each subinterval for validity $$-3\le\dfrac{3x-4}{-5}<4$$

Test $x=-10$ $$-3\le\dfrac{3(-10)-4}{-5}<4$$ $$-3\le\frac{34}{5}\nless4$$ This means $(-\infty,-\frac{16}{3})$ is not part of the solution set.

Test $x=0$ $$-3\le\dfrac{3(0)-4}{-5}<4$$ $$-3\le\frac{4}{5}<4$$ This means $[-\frac{16}{3},\frac{19}{3})$ is part of the solution set.

Test $x=10$ $$-3\le\dfrac{3(10)-4}{-5}<4$$ $$-3\nleq-\frac{26}{5}<4$$ This means that $[\frac{19}{3},\infty)$ is not part of the solution set.

Solve the following rational inequality. $$\dfrac{1-x}{x+2}<-1$$

Note that $\dfrac{1-x}{x+2}$ is undefined when $x=-2$.

First, we will solve $$\begin{aligned}
\dfrac{1-x}{x+2} & =-1\to1-x=-(x+2)\\
 & \to1-x=-x-2\\
 & \to1\ne2\end{aligned}$$ This means for all $x$ the rational expression will not equal negative one. (Also, $y=-1$ is a horizontal asymptote for the plot of $y=\dfrac{1-x}{x+2}$.)

Since there isn't an $x$ such that $\dfrac{1-x}{x+2}=-1$ and $\frac{1-x}{x+2}$ is undefined at $x=-2$. We will consider two subintervals: $$(-\infty,-2)\cup(-2,\infty)$$

Test $x=-10$ $$\dfrac{1-(-10)}{(-10)+2}<-1$$ $$-\frac{11}{8}<-1$$ This means $(-\infty,-2)$ is part of the solution set.

Test $x=0$ $$\dfrac{1-(0)}{(0)+2}<-1$$ $$\frac{1}{2}\nless-1$$ This means $(-2,\infty)$ is not part of the solution set.

Therefore, the solution set for the inequality is $$(-\infty,-2)$$ or the set of all $x$ such that $x<-2$.

Solve the following inequality $$\dfrac{(x^{2}-4)^{2}}{(x-5)(x-3)}<0$$

Note,

$\dfrac{(x^{2}-4)^{2}}{(x-5)(x-3)}$ is undefined when $x=5$ and $x=3$.

$\dfrac{(x^{2}-4)^{2}}{(x-5)(x-3)}=0$ when $x=\pm2$.

$\dfrac{(x^{2}-4)^{2}}{(x-5)(x-3)}=\frac{(x-2)^{2}(x+2)^{2}}{(x-5)(x-3)}$

This means we have the following subintervals $$(-\infty,-2)\cup(-2,3)\cup(3,5)\cup(5,\infty)$$

Test $x=-3$ $$\frac{(x-2)^{2}(x+2)^{2}}{(x-5)(x-3)}\to\dfrac{(+)(+)}{(-)(-)}=(+).$$ This means $\dfrac{(x^{2}-4)^{2}}{(x-5)(x-3)}\nless0$ and $(-\infty,-2)$ is not part of the solution set.

Test $x=0$ $$\frac{(x-2)^{2}(x+2)^{2}}{(x-5)(x-3)}\to\dfrac{(+)(+)}{(-)(-)}=(+).$$ This means $\dfrac{(x^{2}-4)^{2}}{(x-5)(x-3)}\nless0$ and $(-2,3)$ is not part of the solution set.

Test $x=4$ $$\frac{(x-2)^{2}(x+2)^{2}}{(x-5)(x-3)}\to\dfrac{(+)(+)}{(-)(+)}=(-).$$ This means $\dfrac{(x^{2}-4)^{2}}{(x-5)(x-3)}<0$ and $(3,5)$ is part of the solution set.

Test $x=6$ $$\frac{(x-2)^{2}(x+2)^{2}}{(x-5)(x-3)}\to\dfrac{(+)(+)}{(+)(+)}=(+).$$ This means $\dfrac{(x^{2}-4)^{2}}{(x-5)(x-3)}\nless0$ and $(5,\infty)$ is not part of the solution set.

therefore, the solution set is $$(3,5)$$ or the set of all $x$ such that $3<x<5$.