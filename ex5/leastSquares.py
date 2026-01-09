import numpy as np
import matplotlib.pyplot as plt

def PALU(A,b):
    n = len(A)
    U = A
    L = np.identity(n)


    # LU αναλυση
    for i in range(n-1):
        for j in range(n):
            if j>i:
                L[j][i]=U[j][i]/U[i][i]
                for z in range(n):
                    U[j][z]-= L[j][i]*U[i][z]

    y = np.zeros(n)
    for i in range(n):
        Sum=0
        for j in range(n):
            if(i!=j):
                Sum += L[i,j]*y[j]
        y[i]=(b[i]-Sum)/L[i][i]

    #Backward substitution Ux= y
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        Sum=0
        for j in range(n):
            if(i!=j):
                Sum+= U[i][j]*x[j]
        x[i]=(y[i]-Sum)/U[i][i]

    return x

n= 10
angles = [-np.pi,-np.pi/2, -np.pi/3, -np.pi/6 , 0 , np.pi/6,  (np.pi)/4, np.pi/3, np.pi/2, np.pi]
newAngles = np.linspace(-np.pi, np.pi ,200)

y = np.sin(angles)

A = np.zeros((n,8))
for i in range(n):
    for j in range(8):
        A[i][j]= angles[i] ** j

AT = np.zeros((8,n)) #Transoped A
for i in range(8):
    for j in range(n):
        AT[i][j] = A[j][i]

# Multiply Transposed A with A
AT_A = np.zeros((8,8))
for i in range(8):
    for j in range(8):
        for k in range(n):
            AT_A[i][j] += AT[i][k] * A[k][j]

AT_b = np.zeros((8))
for i in range(8):
    for j in range(n):
        AT_b[i] += AT[i][j] * y[j]

palu = PALU(AT_A,AT_b)



approximatedSin = np.zeros((200))
print("Γωνια σε μοιρες \tΠροσεγγιση με ελ.Τετραγωνα\tΣφαλμα")
for i in range(200):
    approximatedSin[i] = palu[0] + palu[1]*newAngles[i] + palu[2]*(newAngles[i]**2) + palu[3]*(newAngles[i]**3) + palu[4]*(newAngles[i]**4) + palu[5]*(newAngles[i]**5) + palu[6]*(newAngles[i]**6) + palu[7]*(newAngles[i]**7)
    print(f"{np.degrees(newAngles[i]):.2f}\t\t\t{approximatedSin[i]:.5f} \t\t\t{abs(approximatedSin[i]-np.sin(newAngles[i])):.20f}")


plt.plot(np.degrees(newAngles), np.abs(approximatedSin - np.sin(newAngles)))
plt.title('Σφάλμα ελάχιστων τετραγώνων')
plt.xlabel('Γωνία')
plt.ylabel('Σφάλμα')
plt.show()