import numpy as np
import matplotlib.pyplot as plt

n = 10
angles = [-np.pi,-np.pi/2, -np.pi/3, -np.pi/6 , 0 , np.pi/6,  (np.pi)/4, np.pi/3, np.pi/2, np.pi]
newAngles = np.linspace(-np.pi, np.pi ,200)


def lagrange(x,y,xi):
    n = len(x)
    m = len(xi)
    result = np.zeros(m)

    for i in range(m):
        sum = 0
        for j in range(n):
            term = y[i]
            for z in range(n):
                if z != j :
                    term *= (xi[i]-x[z]) / (x[j] - x[z])
            sum += term
        result[i] = sum

    return result

approximatedSin = np.zeros((200))
error = np.zeros((200))
approximatedSin = lagrange(angles,np.sin(newAngles),newAngles)


for j in range(200):
    error[j] = abs(np.sin(newAngles[j]) - approximatedSin[j])
    print("Γωνια σε μοιρες \t Προσεγγιση με Lagrange \t Σφαλμα")
    print(f"{np.degrees(newAngles[j]):.2f}\t\t\t{approximatedSin[j]:.10f}\t\t\t{error[j]:.20f}")

plt.plot(np.degrees(newAngles), error)
plt.title('Σφάλμα προσέγγισης Lagrange')
plt.xlabel('Γωνία (μοίρες)')
plt.ylabel('Σφάλμα')
plt.show()