import numpy as np

def f(x):
    return np.sin(x)

def d4_f(x):
    return f(x)

n = 10
a = 0.0
b = (np.pi)/2.0
interval = (b-a) /n

x = []
for i in range(n+1):
    x.append(a+i * interval)

fx = np.zeros(n+1)
for i in range(1,n,2):
    fx[i]= 4 * f(x[i])

for i in range(2, n, 2):
    fx[i] = 2 * f(x[i])

fx[0] = f(a)
fx[n] = f(b)
stable = fx[0] + fx[n]

Sum = 0.0
for i in range(n):
    Sum+= fx[i]

sum1 = stable + Sum
integral = (interval/3.0)*sum1
print(f"Το ολοκληρωμα της sin(x) στο διαστημα [0,π/2] με την μεθοδο Simphson ειναι : {integral:.10f}")

M = 0.0
for i in range(i+1):
    max_val = abs(d4_f(x[i]))
    if (max_val>M):
        M = max_val

nominator = M * (b - a) ** 5
denominator = 180 * n ** 4
error = nominator / denominator
print(f"Το σφάλμα προσέγγισης αριθμητικά είναι: {error:.15f}")
print(f"Το σφάλμα προσέγγισης θεωρητικά είναι: {abs(1.00 - integral):.15f}")