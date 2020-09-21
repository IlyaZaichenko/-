#1) I_n = 1/n - a(I_n-1) - рекуррентное соотношение I_n и I_n-1
# 2) I_0 = log(1+ 1/a) -явное выражение I_0
#3) Обратная рекурсия:
def recur(a):
    n = 100
    z = 0
    while n >= 25:
        n = n - 1
        z = (1/n - z)/a
        return(z)
print(recur(0.1))
print(recur(10))

# Обычная рекурсия:
import numpy as np
def recur(a):
   n = 0
   z = np.log(1+ 1/a)
   while n <= 25:
       n= n + 1
       z =1/n - a*z
       return(z)
print( recur(0.1))
print( recur(10))











