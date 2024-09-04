# Section 2.5

Consider a fixed point on a line and call it $(x_1,y_1)$. Next, consider any other point on the line and call it $(x,y)$. Then the slope of the line would be:

$$m=\frac{y-y_1}{x-x_1}$$

The equivalent equation would be: $y-y_1=m(x-x_1)$; provided $(x,y)$ is different from the fixed point. This leads to the point-slope form equation of a line.

:::{prf:definition} Point-Slope Form
:label: pointSlopeForm
The point-slope form of the equation of a line with a slope of $m$ and a point $(x_1,y_1)$ is 

$$y-y_1=m(x-x_1)$$
:::

::::{prf:example}
:label: lineExample1
Write the equation of a line passing through the point $(-4,1)$ and has a slope of $3$. Finish the equation in slope-intercept form ($y=mx+b$).
:::{dropdown} Solution:
We are given $(x_1,y_1)=(-4,1)$ and $m=3$. Plugging these values into the point-slope form equation we have:

$$y-1=3(x+4)$$

Now, solve for $y$ to get into slope-intercept form
\begin{align*}
    y-1 & = 3(x+4)\\
    y-1 & = 3x+12\\
    y & = 3x+12+1\\
    & = 3x+13
\end{align*}
Therefore, the equation of the line passing through $(-4,1)$ and has a slope of $3$ is: $y=3x+13$.
:::
::::
::::{prf:example}
:label: lineExample2
Write the equation of the line passing through the points $(-4,3)$ and $(5,-1)$. Finish the equation in slope-intercept form ($y=mx+b$).
:::{dropdown} Solution:
We are given $(x_1,y_1)=(-4,3)$ and $(x_2,y_2)=(5,-1)$. In order to find the equation of the line we must first find the slope of the line. Using $m=\frac{y_2-y_1}{x_2-x_1}$ we have
\begin{align*}
    m & = \frac{-1-3}{5-(-4)}\\
    & = \frac{-4}{9}
\end{align*}
Next, we pick one of the two points, $(-4,3)$, and use $m=-\frac{4}{9}$ to find the equation of the line:
\begin{align*}
    y-3 & =-\frac{4}{9}(x+4)\\
    y-3 & = -\frac{4}{9}x-\frac{16}{9}
    y & = -\frac{4}{9}x +\frac{27-16}{9}\\
    & = -\frac{4}{9}x + \frac{11}{9}
\end{align*}
Therefore, the equation of the line is $y=-\frac{4}{9}x+\frac{11}{9}$.
:::
::::
::::{prf:example}
:label: lineExample3
Given the following graph. Find the equation of the line.
![Graph of a line](images/graphline1.png)
:::{dropdown} Solution:
One way to find the equation of the line is to have two points, find the slope, plug the point and slope into the point-slope, and then solve for $y$. Given the graph of a line, we have many points to choose from. However, two points seem to be clearly on the line: $(0,2)$ and $(3,0)$. We will use these points to find the equation of the line. First, we will find the slope:
\begin{align*}
    m & = \frac{0-2){3-0}\\
    & = \frac{-2}{3}
\end{align*}
Using the point $(0,2)$ and slope $m=-\frac{2}{3}$ we have:
\begin{align*}
    y-2&=-\frac{2}{3}(x-0)\\
    y & = -\frac{2}{3}x+2
\end{align*}
Therefore, the equation of the graphed line is: $y=-\frac{2}{3}x+2$.
:::
::::