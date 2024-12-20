import numpy as np
import scipy

X = np.array([[2100,3,20],[2500,4,15],[1800,2,30],[2200,3,25]])
y = np.array([460,540,330,400])

beta, residue, rank, sing_vals = scipy.linalg.lstsq(X, y)
print(f"{beta} is our solution beta")

price_house_1 = (beta @ np.array([2400,3,20]))
print(price_house_1)

'''4. The least-squares method is better in this prediction task, as
M is not a square matrix. Thus, we can't use linalg.solve().
In this sense, an iterative method is better suited even if it might in general take longer
'''
