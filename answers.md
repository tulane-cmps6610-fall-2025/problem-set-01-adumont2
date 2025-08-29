  # CMPS 6610 Problem Set 01
## Answers

**Name:**__ Aaron Dumont_______________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**
  - 1a **TRUE. Yes**, $2^{n+1} \in O(2^n)$.

    **Reasoning:**
    Per Big O ntation, we must show that there exist positive constants $c$ and $n_0$ such that $f(n) \le c \cdot g(n)$ for all $n \ge n_0$.

    Let $f(n) = 2^{n+1}$ and $g(n) = 2^n$.

    $f(n) = 2^{n+1} = 2^1 \cdot 2^n = 2 \cdot 2^n$.

    $2 \cdot 2^n \le c \cdot 2^n$.

    Divide both sides by $2^n$, we get $2 \le c$.

    We can choose $c \ge 2$ and this inequailty holds for all $n \ge 0$ (so we can set $n_0 = 0$).

    Since we found constants $c \ge 2$ and $n_0 = 0$ that satisfy the definition, $2^{n+1}$ is in $O({2^n})$. 


  - 1b  **FALSE. No**, $2^{2^n} \in O(2^n)$.

    **Reasoning:** In class we have demonstrated that any polylogarithmic function grows slower than any polynomial function. Expressed differently, $log^i(n) \in O(n^j)$ $\forall$ $i, j \gt 0$. Conversely $n^j \in \Omega(log^i(n))$ $\forall$ $i, j \gt 0$

    Let $f(n) = 2^{2^n}$ and $g(n) = 2^n$.
    
    Inequality: $2^{2^n} \le c \cdot 2^n$. We must check if there is a constant c that satisfies this.

    Let $a = 2^n$

    THen $2^a \le c \cdot a$.
    
    Take $log_2$ of both sides.

    $a \le log_2 c + log_2a$

    Therefore there is no c that satisfies this inequality as the left polynomial which grows lineraly always grows faster than the right polylogarithmic function.   
 
  - 1c
    **FALSE. No**, $n^{1.01} \in O(log^2n)$.

    **Reasoning:** As above, any polylogarithmic function grows slower than any polynomial function. Expressed differently, $log^i(n) \in O(n^j)$ $\forall$ $i, j \gt 0$. Conversely $n^j \in \Omega(log^i(n))$ $\forall$ $i, j \gt 0$. The polynomial function $n^{1.01}$ grows much faster than a constant multiple of $logn$ (in this case $log^2n$).
  - 1d
    **TRUE. Yes**, $n^{1.01} \in \Omega(log^2n)$.

    **Reasoning:** As above,as we have shown in class, $n^j \in \Omega(log^i(n))$ $\forall$ $i, j \gt 0$.Therefore, the statement is true.
  - 1e
    **FALSE. No**, $\sqrt{n} \in O(log^3n)$.

    **Reasoning:** As above, any polylogarithmic function grows slower than any polynomial function. Expressed differently, $log^i(n) \in O(n^j)$ $\forall$ $i, j \gt 0$. Conversely $n^j \in \Omega(log^i(n))$ $\forall$ $i, j \gt 0$. The polynomial function $\sqrt{n}$ which is $n^{0.5}$ grows faster than a constant multiple of $logn$ (in this case $log^3n$).

  - 1f
     **TRUE. Yes**, $\sqrt{n} \in \Omega(log^3n)$.

    **Reasoning:** As above,as we have shown in class, $n^j \in \Omega(log^i(n))$ $\forall$ $i, j \gt 0$.Therefore, the statement is true.
  - 1g
    We will assume that there exists a function, $f(n)$, in the intersection of $o(g(n))$ and $\omega(g(n))$. By definition:

    1. $f(n) \in o(g(n))$, for any constant $c_1 \gt 0$ and there is an $n_1$ such that $f(n) \lt c_1g(n)$ for all $n \ge n_1$.
    2. $f(n) \in \omega(g(n))$, for any constant $c2 \gt 0$ and there is an $n_2$ such that $c_2g(n) \lt f(n)$ for all $n \ge n_2$.

    The above must hold for every positive constant c. So let $c_1 = c_2$. We can also select $n_0 = max (n_1, n_2)$.By selecting  $n_0 = max (n_1, n_2)$, we establish a threshold. For any $n \ge n_0$, we are guaranteed that $n \ge n_1$ AND $n \ge n_2$, meaning both inequalities must hold. Therfore:

    $c_2g(n) \lt f(n) \lt c_1g(n)$. $c_1 = c_2$. Therefore, $c_1g(n) \lt f(n) \lt c_1g(n)$. Since this is a strict inequality definition, there is no $f(n)$ that exists to satisfy this strict inequality.
2. **SPARC to Python**

  - 2b

3. **Parallelism and recursion**

  - 3b

  - 3d

  - 3e
  
4. **GCD**
