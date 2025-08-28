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
    
    Inequality: $2^{2^n} \le c \cdot 2^n$. We must check if there is a constant c that satisfies this
    
    Take $log_2$ of both sides.

    $2^n \le c \cdot n$   
 
  - 1c

  - 1d

  - 1e

  - 1f

  - 1g

2. **SPARC to Python**

  - 2b

3. **Parallelism and recursion**

  - 3b

  - 3d

  - 3e
  
4. **GCD**
