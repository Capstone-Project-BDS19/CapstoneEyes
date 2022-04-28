#used to test logics. useless on the web app
import numpy as np

a = [i for i in range(1,10)]
print(a)
print(np.mean(a))

a = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
b = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
from scipy.stats import linregress
print(linregress(a, b)[0])