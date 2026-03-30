from sympy import Symbol, diff, factorial, sympify, Matrix, pprint, zeros, sqrt, solve, pretty, exp, integrate, simplify, ones
from sympy.core.numbers import NumberSymbol
from sympy.matrices.common import MatrixError
from sympy.matrices.dense import MutableDenseMatrix
from typing import List, Tuple

def T(n: int, a: float|int|NumberSymbol, x: Symbol, f: Symbol) -> NumberSymbol:
    """
    Required for MTH107. Compute n-degree Taylor Polynomial of function f(x) at x = a
    """
    g = sympify(0)
    for i in range(n):
        f1 = f.subs(x, a) * (x - a)**i / factorial(i)
        g += f1 
        f = diff(f, x)
    return g

def gcd(a0: int, b0: int) -> int:
    """
    Required for MTH105. Compute the Greatest Common Divisor using Euclid's Algorithm and find integers m, n such that m*a + n*b = gcd(a, b)
    """
    a, b = a0, b0
    print("computing gcd of", a, "and", b, "\n")

    l = max(len(str(a)), len(str(b)))
    equations = []

    print("Start Euclidean Algorithm")
    print("========================")
    # standard euclidean algorithm
    while b != 0:
        q, r = a//b, a%b
        equations.append([a, b, q, r])
        print(str(a).rjust(l, " "), "=", str(q).rjust(l, " "), "*", str(b).rjust(l, " "), "+", r)        
        a, b = b, r

    # last equation is not needed for additional processing
    equations.pop()
    d = a
    print("\ngcd".rjust(l, " "), "=", d, "\n")

    print("Calculating Linear Integral Combination")
    print("=======================================")

    # back substitution is the textbook method to calculate the linear integral combination
    # back substitution is achieved with dynamic programming

    # initialise memoization table for dynamic programming
    table = {}
    table[a0] = [1, 0]
    table[b0] = [0, 1]

    for eq in equations:
        a, b, q, r = eq
        a1, b1, = table[a]
        a2, b2 = table[b]
        # this is the key subproblem for formulating back substitution as a dynamic programming problem
        table[r] = [a1-q*a2, b1-q*b2]
        print(" ".join([str(r).rjust(l, " "), "=", str(table[r][0]).rjust(l, " "), "*", str(a0).rjust(l, " "), "+", str(table[r][1]).rjust(l, " "), "*", str(b0)]))

    #  beautify the printing of the linear integral combination result
    x, y = table[d]
    plus = "+"
    y0 = y
    if y < 0:
        y0, plus = -y, "-"
    print("\ngcd".rjust(l, " "), "=", str(d).rjust(l, " "), "=", str(x).rjust(1, " "), "*", str(a0).rjust(l, " "), plus, str(y0).rjust(l, " "), "*", str(b0).rjust(l, " "), "\n")

    return d

def reducedEchelonForm(m: MutableDenseMatrix) -> MutableDenseMatrix:
    """
    Required for MTH207. m is an augmented m-by-n matrix 
    """
    m1: MutableDenseMatrix = MutableDenseMatrix(m)
    pivots = []
    # convert m1 to echeleon form
    for pivot in range(min(m1.cols,m1.rows)):
          print(" |")
          print("\\|/")
          pprint(m1)
          print(" |")
          if m1[pivot, pivot] == 0:
            for row in range(pivot+1, m1.rows):
                if m1[row, pivot] != 0:
                    print("a", row, pivot)
                    print(f" | row{row+1} = row{pivot+1}")
                    print(f" | row{pivot+1} = row{row+1}")
                    r0, r1 = m1.row(pivot), m1.row(row)
                    m1.row_del(pivot)
                    m1 = m1.row_insert(pivot, r1)
                    m1.row_del(row)
                    m1 = m1.row_insert(row, r0)
                    break
            print(" |")
            print("\\|/")
            pprint(m1)
            print(" |")
          if m1[pivot, pivot] != 0:
               pivots.append(pivot)
               row_pivot = f"row{pivot+1}" 
               if m1[pivot, pivot] != 1:                    
                    c = m1[pivot, pivot]
                    r0 = m1.row(pivot) / c
                    r0.simplify()
                    m1.row_del(pivot)
                    m1 = m1.row_insert(pivot, r0)
                    row_pivot = f"row{pivot+1}/({c})"                    
                    print(f" | row{pivot+1} =", row_pivot)

               for row in range(pivot+1, m1.rows):
                    c = m1[row, pivot]
                    if c != 0:
                         r0 = m1.row(row) - c*m1.row(pivot)
                         r0.simplify()
                         m1.row_del(row)
                         m1 = m1.row_insert(row, r0)
                         print(f" | row{row+1} = row{row+1} - ({c})*{row_pivot}")

    # convert m1 from echeleon form to reduced echeleon form
    print(" |")
    print("\\|/")
    pprint(m1)
    for pivot in pivots[1:][::-1]:
        print(" |")
        for row in range(pivot-1, -1, -1):
            c = m1[row, pivot]            
            if c != 0:
                r0 = m1.row(row) - c*m1.row(pivot)
                r0.simplify()
                m1.row_del(row)
                m1 = m1.row_insert(row, r0)
                print(f" | row{row+1} = row{row+1} - ({c})*row{pivot+1}")
        if pivot != pivots[0]:
            print(" |")
            print("\\|/")
            pprint(m1)
    
    # move all zero rows to the bottom of m1
    print(" |")
    z0 = zeros(1, m1.cols)
    for row in range(m1.rows-1, -1, -1):
        if m1.row(row) == z0:
            m1.row_del(row)
            m1 = m1.row_insert(m1.rows, z0)
            print(f" | set row{row+1} to last row")
    print(" |")
    print("\\|/")
    pprint(m1)
    return m1

def identity(n: int) -> Matrix:
    """
    Returns a n x n Identity Matrix
    """
    m = [0] * n**2
    j = 0
    for i in range(0,n**2,n):
        m[i+j] = 1
        j += 1
    return Matrix(n, n, m)

def vector(L: List[NumberSymbol]):
    return Matrix(len(L), 1, L)

def diagonal(L: List[NumberSymbol]):
    """
    Returns a diagonal matrix
    """
    n = len(L)
    m = Matrix(len(L), len(L), [0]*n**2)
    row, col = 0, 0
    for i in L:
        index = row * n + col
        m[index] = i
        row += 1
        col += 1
    return m

def quadratic(a:NumberSymbol, b: NumberSymbol, c: NumberSymbol):
    return (-b + sqrt(b**2 - 4*a*c))/2*a, (-b - sqrt(b**2 - 4*a*c))/2*a

def lu_decomposition(m: MutableDenseMatrix, toPrint=True) -> Tuple[MutableDenseMatrix, MutableDenseMatrix, List[MutableDenseMatrix]]:
    """
    Required for MTh355. Assumes m is n x n square matrix. Returns L, U and the list of elementary matrices [E1, E2, ... ]
    """
    if m.det() == 0:
        raise Exception("Matrix is not LU decomposible")
    n = m.shape[0]
    L = identity(n)
    U = m.copy()
    elem_ops = []
    k = 1
    for j in range(n):
        for i in range(j+1,n):
            e = identity(n)
            e[i,j] = - U[i,j] / U[j, j]
            elem_ops.append(e)
            if toPrint:
                print(f"\nrow operation: r{i+1} = r{i+1} + ({e[i,j]})*r{j+1} \n")
                print(f"Elementary Matrix E{k}")
                pprint(e)
            k += 1
            L = L*e.inv()
            U = e*U
            if toPrint:
                print("Updated U after row operation")
                pprint(U)
    if toPrint:
        print("\nU is")
        pprint(U)
        print("\nL is")
        pprint(L)
    return L, U, elem_ops

def isDiagonalDominant(m: MutableDenseMatrix) -> bool:
    """
    Returns True if the n x n matrix m is diagonally dominant
    """
    n = m.shape[0]
    for i in range(n):
        s = sum([abs(m[i,j]) for j in range(n) if i != j])
        if abs(m[i,i]) < s:
            return False
    return True

def jacobiIteration(A: MutableDenseMatrix, b: MutableDenseMatrix, initial_values: MutableDenseMatrix, relative_tolerance: float, maxIteration=100) -> MutableDenseMatrix:
    """
    Required for MTH355. This solves Ax = b using the Jacobi Iteration Method
    """
    if not isDiagonalDominant(A):
        raise Exception("Matrix A is not diagonally dominant.")
    n = A.shape[0]
    x = vector([Symbol(f"x_{i+1}") for i in range(n)])
    y0 = A*x - b
    y1 = vector([solve(y0[i,0], x[i])[0] for i in range(n)])
    for i in range(n):
        print(pretty(x[i]) + " is")
        pprint(y1[i,0], use_unicode=True)
        print()
    xr = [initial_values, None, None]
    prev, next, err = 0, 1, 2
    error = 2*relative_tolerance
    r = 0
    w1, w2 = 5, 18
    print("r".center(w1), " ".join([pretty(x[i]).center(w2) for i in range(n)]))
    print("".center(w1,"-"), " ".join([f"".center(w2,"-") for i in range(n)]))
    print("1".center(w1), " ".join([f"{xr[prev][i]}".center(w2) for i in range(n)]))
    while error > relative_tolerance:
        if r > maxIteration:
            raise Exception("Max Iteration reached. No solution found.")
        y2 = y1
        for i in range(n):
            y2 = y2.subs(x[i], xr[prev][i]).evalf()
        xr[next] = y2
        print(f"{r+2}".center(w1), " ".join([f"{xr[next][i]:.6f}".center(w2) for i in range(n)]))
        xr[err] = xr[next] - xr[prev]
        for i in range(n):
            xr[err][i,0] = abs(xr[err][i,0]/xr[prev][i,0])
        error = max(xr[err])
        prev, next = next, prev
        r += 1
    print()
    print("\t".join([f"{pretty(x[i])} = {xr[prev][i]:.6f}" for i in range(n)]))
    return xr[prev]

def gaussSeidelIteration(A: MutableDenseMatrix, b: MutableDenseMatrix, initial_values: MutableDenseMatrix, relative_tolerance: float, maxIteration=100) -> MutableDenseMatrix:
    """
    Required for MTH355. This solves Ax = b using the Gauss-Seidel Iteration Method
    """
    if not isDiagonalDominant(A):
        raise Exception("Matrix A is not diagonally dominant.")
    n = A.shape[0]
    x = vector([Symbol(f"x_{i+1}") for i in range(n)])
    y0 = A*x - b
    y1 = vector([solve(y0[i,0], x[i])[0] for i in range(n)])
    for i in range(n):
        print(pretty(x[i]) + " is")
        pprint(y1[i,0], use_unicode=True)
        print()
    xr = initial_values
    error = [2*relative_tolerance] * n
    r = 0
    w1, w2 = 5, 18
    print("r".center(w1), " ".join([pretty(x[i]).center(w2) for i in range(n)]))
    print("".center(w1,"-"), " ".join([f"".center(w2,"-") for i in range(n)]))    
    print(f"1".center(w1), " ".join([f"{xr[i]:.6f}".center(w2) for i in range(n)]))
    while max(error) > relative_tolerance:
        if r > maxIteration:
            raise Exception("Max Iteration reached. No solution found.")
        for i in range(n):
            y2 = y1[i,0]
            for j in range(n):
                if i != j:
                    y2 = y2.subs(x[j], xr[j])
            y2_e = y2.evalf()
            error[i] = abs((y2_e - xr[i])/xr[i])
            xr[i] = y2_e
        print(f"{r+2}".center(w1), " ".join([f"{xr[i]:.6f}".center(w2) for i in range(n)]))
        r += 1
    print()
    print("\t".join([f"{pretty(x[i])} = {xr[i]:.6f}" for i in range(n)]))
    return xr

def duhamel(A: MutableDenseMatrix, f: MutableDenseMatrix, x0: MutableDenseMatrix, t: Symbol) -> None:
    """
    Required by MTH320. Implementation of Duhamel's Principle.
    This solves x' = Ax + f(t) where
        x' = transpose of [ x_1', x_2', ... , x_n' ]
        x = [ x_1(t), x_2(t), ... , x_n(t) ]
        x0 = [ x_1(0), x_2(0), ... , x_n(0) ]
        A = n x n matrix
        f(t) = transpose of [ f_1(t), f_2(t), ... , f_n(t) ]
    """
    s = Symbol("s")
    eAt = exp(A*t)
    eAt_x0 = simplify(eAt*x0)
    pprint(eAt_x0)
    eAts_fs = simplify(eAt.subs(t, t-s)*f.subs(t,s))
    pprint(eAts_fs)
    return simplify(eAt_x0 + integrate(eAts_fs, (s, 0, t)))

def odd_signal(x_t: Symbol, t: Symbol) -> Symbol:
    """
    Required by ENG201
    """
    soln = (x_t - x_t.subs(t, -t))/2
    return soln.simplify()

def even_signal(x_t: Symbol, t: Symbol) -> Symbol:
    soln = (x_t + x_t.subs(t, -t))/2
    return soln.simplify()

def linear_regression(x: MutableDenseMatrix, y: MutableDenseMatrix) -> Tuple[MutableDenseMatrix, Symbol]:
    A = x.row_join(ones(len(y),1))
    v = (A.transpose()*A).inv() *(A.transpose() * y)    
    r = y-A*v
    sse = (r.transpose()*r)[0]
    return v, sse

# rotatory shift right
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

# rotatoy shift left
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

def display_tableau(A:MutableDenseMatrix, symbols:list[Symbol], basis:list[Symbol]) -> MutableDenseMatrix:
    b = Symbol("basis")
    basis_col = [b] + basis
    return Matrix(basis_col).row_join(Matrix(symbols).transpose().col_join(A))

def simplex_rowops(A:MutableDenseMatrix, entering: Symbol, leaving:Symbol, symbols:list[Symbol], basis:list[Symbol]) -> MutableDenseMatrix:
    col = symbols.index(entering)
    row = basis.index(leaving)
    B1 = A.row(row) / A[row, col]
    B = A.row(0) - A[0,col]*B1
    rows = A.shape[0]
    for i in range(1, rows):
        if i == row:
            B = B.col_join(B1)
        else:
            B = B.col_join(A.row(i) - A[i, col]*B1)
    return B

def choose(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def RiemannSum(f, x, partition):
    s = 0
    for a, b, tag in partition:
        s += (b - a)*f.subs(x, tag)
    return s

if __name__ == "__main__":
    t = Symbol("t")
    A = Matrix(2,2,[-5,3,-3,1])
    x0 = vector([1,0])
    f = vector([exp(t), 0])
    pprint(duhamel(A,x0,f,t))



