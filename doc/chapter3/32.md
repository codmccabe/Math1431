# Section 3.2

## Real Number Division Algorithm

:::{prf:definition} Division Algorithm (Real Numbers)
:label: divAlgRealNumbers
Let $a$ and $b$ be any real number where $b\ne0$. Then there exists a unique real number $q$ and $r$ such that 

$$a=b\cdot q+r$$

where $0<r<b$ or $r=0$.
:::

:::{prf:example}
:label: divExample1
If we look at $12$ and $3$ we know that

$$12=3\cdot 4 + 0$$

This can be shown by doing long division:

\begin{alignat*}{10}
& \phantom{11}4\\
3 & )\overline{12}\\
- & \underline{\phantom{)}12} & \leftarrow4(3)\phantom{--}\\
 & \phantom{)1}0 & \leftarrow12-12
\end{alignat*}

If we look at $13$ and $3$ we know that

$$13 = 3\cdot 4 + 1$$

This can be shown by doing long division:

\begin{alignat*}{10}
& \phantom{11}4\\
3 & )\overline{13}\\
- & \underline{\phantom{)}12} & \leftarrow4(3)\phantom{--}\\
 & \phantom{)1}1 & \leftarrow13-12
\end{alignat*}