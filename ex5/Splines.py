import numpy as np
import matplotlib.pyplot as plt

def PALU(A, b):
    n = len(A)
    U = A.copy()
    L = np.identity(n)

    # LU αναλυση
    for i in range(n-1):
        for j in range(n):
            if j > i:
                L[j][i] = U[j][i] / U[i][i]
                for z in range(n):
                    U[j][z] -= L[j][i] * U[i][z]

    y = np.zeros(n)
    for i in range(n):
        Sum = 0
        for j in range(n):
            if i != j:
                Sum += L[i, j] * y[j]
        y[i] = (b[i] - Sum) / L[i][i]

    # Backward substitution Ux = y
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        Sum = 0
        for j in range(n):
            if i != j:
                Sum += U[i][j] * x[j]
        x[i] = (y[i] - Sum) / U[i][i]

    return x

def cubic_spline(x,y):
    n = len(x)
    h = []
    for i in range(n-1):
        h.append(x[i+1] - x[i])

    A = np.zeros((n, n))
    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, n-1):
        A[i, i-1:i+2] = [h[i-1], 2*(h[i-1] + h[i]), h[i]]


    b = np.zeros(n)
    for i in range(1, n-1):
        b[i] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])

    c = PALU(A, b)
    a = y
    b = [0] * n
    d = [0] * n

    for i in range(n-1, 0, -1):
        b[i-1] = (a[i] - a[i-1]) / h[i-1] - h[i-1] * (c[i] + 2 * c[i-1]) / 3
        d[i-1] = (c[i] - c[i-1]) / (3 * h[i-1])

    return a, b, c, d

def eval_cubic_spline(x_eval, x, a, b, c, d):
    n = len(x)
    result = np.zeros((200))

    for i in range(n-1):
        mask = (x_eval >= x[i]) & (x_eval <= x[i+1])
        result[mask] = a[i] + b[i] * (x_eval[mask] - x[i]) + c[i] * (x_eval[mask] - x[i])**2 + d[i] * (x_eval[mask] - x[i])**3

    return result


angles = [-np.pi,-np.pi/2, -np.pi/3, -np.pi/6 , 0 , np.pi/6,  (np.pi)/4, np.pi/3, np.pi/2, np.pi]
newAngles = np.linspace(-np.pi,np.pi, 200)

y = np.sin(angles)

a, b, c, d = cubic_spline(angles, y)
approximatedSin = eval_cubic_spline(newAngles,angles,a,b,c,d)
error = abs(np.sin(newAngles) - approximatedSin)

print(f"{approximatedSin} | {error}")

plt.plot(newAngles, approximatedSin, label='Splines')
plt.plot(newAngles, np.sin(newAngles), label='sin(x)')
plt.title('Προσέγγιση sin(x) με Splines')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.show()

plt.plot(newAngles, error, label='Σφάλμα')
plt.title('Σφάλμα προσέγγισης με Splines')
plt.xlabel('x')
plt.ylabel('Σφάλμα')
plt.legend()
plt.show()
