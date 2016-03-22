import numpy as np 
import matplotlib.pyplot as plt

# NumPy Overview
a = [1, 2, 3, 4]
a = np.array(a)
print a # [1 2 3 4]
print type(a)
a = a + 1
print a # [2 3 4 5]
b = np.array([2, 3, 4, 5])
print b # [2 3 4 5]
print a + b  # [ 4  6  8 10]
print a * b  # [ 4  9 16 25]
print a ** b # [   4   27  256 3125]
print a[0] # 2
print a[:2] # [2 3]
print a[-2:] # [4 5]
print a[:2] + a[-2:] # [6 8]
print a.shape # (4,)

# shape can be changed on the fly
a.shape = 2,2
print a
# [[2 3]
#  [4 5]]
print a + a
# [[ 4  6]
#  [ 8 10]]
print a * a  # element by element operation
# [[ 4  9]
#  [16 25]]

a = np.linspace(0, 2 *np.pi, 21)
print a
b = np.sin(a)

plt.plot(a,b)
mask = b > 0
plt.plot(a[mask], b[mask], 'ro')
plt.show()





