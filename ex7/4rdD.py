import numpy as np

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


dates = np.array([4,5,6,7,8,9,10,11,12,13])
BTC = np.array([87222.20 , 90623.56, 89961.73, 86742.67, 86154.59, 80601.04, 78532.00, 82862.21, 83722.36, 81066.70])
ETH = np.array([2170.02, 2241.98, 2202.48, 2138.99, 2201.51, 2015.51, 1861.15, 1919.84, 1908.98, 1862.97])

n = len(dates)

xBTC = np.zeros((n,5))
xETH = np.zeros((n,5))
for i in range(n):
    for j in range(5):
        xBTC[i][j]= dates[i] ** j
        xETH[i][j]= dates[i] ** j



# Calculate the Transposed Array
BTC_T = np.zeros((5,n))
ETH_T = np.zeros((5,n))
for i in range(5):
    for j in range(n):
        BTC_T[i][j] = xBTC[j][i]
        ETH_T[i][j] = xETH[j][i]


# Multiply xBTC with Transposed xBTC
xBTC_BTCT = np.zeros((5,5))
xETH_ETHT = np.zeros((5,5))
for i in range(5):
    for j in range(5):
        for k in range(n):
            xBTC_BTCT[i][j] += BTC_T[i][k] * xBTC[k][j]
            xETH_ETHT[i][j] += ETH_T[i][k] * xETH[k][j]

#Multiply xBTC with BTC
BTCT_BTC = np.zeros((5))
ETHT_ETH = np.zeros((5))

for i in range(5):
    for j in range(n):
        BTCT_BTC[i] += BTC_T[i][j] * BTC[j]
        ETHT_ETH[i] += ETH_T[i][j] * ETH[j]

palu_BTC = PALU(xBTC_BTCT,BTCT_BTC)
palu_ETH = PALU(xETH_ETHT,ETHT_ETH)


a = palu_BTC[0]
b = palu_BTC[1]
c = palu_BTC[2]
d = palu_BTC[3]
e = palu_BTC[4]

closeBTC14 = a + b*14 + c*(14**2) + d*(14**3) + e*(14**4)
print(f"Closing Price of BTC on 14/03/2025 : {closeBTC14:.2f} USD, Actual prize: 83969.10")
closeBTC15 = a + b*15 + c*(15**2) + d*(15**3) + e*(15**4)
print(f"Closing Price of BTC on 15/03/2025 : {closeBTC15:.2f} USD, Actual prize: 84343.11")
closeBTC16 = a + b*16 + c*(16**2) + d*(16**3) + e*(16**4)
print(f"Closing Price of BTC on 16/03/2025 : {closeBTC16:.2f} USD, Actual prize: 82579.69")
closeBTC17 = a + b*17 + c*(17**2) + d*(17**3) + e*(17**4)
print(f"Closing Price of BTC on 17/03/2025 : {closeBTC17:.2f} USD, Actual prize: 84075.69")
closeBTC18 = a + b*18 + c*(18**2) + d*(18**3) + e*(18**4)
print(f"Closing Price of BTC on 18/03/2025 : {closeBTC18:.2f} USD, Actual prize: 82718.50")
closeBTC19 = a + b*19 + c*(19**2) + d*(19**3) + e*(19**4)
print(f"Closing Price of BTC on 19/03/2025 : {closeBTC19:.2f} USD, Actual prize: 86854.23")

print("-"*60)

a_ETH = palu_ETH[0]
b_ETH = palu_ETH[1]
c_ETH = palu_ETH[2]
d_ETH = palu_ETH[3]
e_ETH = palu_ETH[4]

closeETH14 = a_ETH + b_ETH*14 + c_ETH*(14**2) + d_ETH*(14**3) + e_ETH*(14**4)
print(f"Closing Price of ETH on 14/3/2025 : {closeETH14:.2f} USD, Actual prize: 1909.47")
closeETH15 = a_ETH + b_ETH*15 + c_ETH*(15**2) + d_ETH*(15**3) + e_ETH*(15**4)
print(f"Closing Price of ETH on 15/3/2025 : {closeETH15:.2f} USD, Actual prize: 1937.39")
closeETH16 = a_ETH + b_ETH*16 + c_ETH*(16**2) + d_ETH*(16**3) + e_ETH*(16**4)
print(f"Closing Price of ETH on 16/3/2025 : {closeETH16:.2f} USD, Actual prize: 1887.44")
closeETH17 = a_ETH + b_ETH*17 + c_ETH*(17**2) + d_ETH*(17**3) + e_ETH*(17**4)
print(f"Closing Price of ETH on 17/3/2025 : {closeETH17:.2f} USD, Actual prize: 1927.00")
closeETH18 = a_ETH + b_ETH*18 + c_ETH*(18**2) + d_ETH*(18**3) + e_ETH*(18**4)
print(f"Closing Price of ETH on 18/3/2025 : {closeETH18:.2f} USD, Actual prize: 1932.54")
closeETH19 = a_ETH + b_ETH*19 + c_ETH*(19**2) + d_ETH*(19**3) + e_ETH*(19**4)
print(f"Closing Price of ETH on 19/3/2025 : {closeETH19:.2f} USD, Actual prize: 2057.75")