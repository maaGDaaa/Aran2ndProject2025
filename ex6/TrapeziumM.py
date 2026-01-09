import numpy as np

def f(x):
    return np.sin(x)
def d2_F(x):
    return - np.sin(x)

n = 10
a = 0.0
b = np.pi /2.0
interval = (b-a)/n

x = []
for i in range(n + 1):
    x.append(a + i * interval)

fx = []
for i in range(1, n):
    fx.append(2 * f(x[i]))

_sum = sum(fx)
sum1 = _sum + f(x[0]+f(b))

integral = sum1*(interval/2)

print(f"Το ολοκληρωμα του sin(x) με την Μεθοδο Τραπεζιου στο [0,π/2] ειναι : {integral:.10f}")

M = 0.0
for xi in x:
    max_val = abs(d2_F(xi))
    if max_val > M:
        M = max_val

nominator = M * pow((b - a), 3)
denominator = 12 * pow(n, 2)
error = nominator / denominator
print(f"Το σφάλμα προσέγγισης αριθμητικά είναι: {error:.15f}")
print(f"Το σφάλμα προσέγγισης θεωρητικά είναι: {abs(1.00 - integral):.15f}")