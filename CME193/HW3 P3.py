import numpy as np
import matplotlib as plt

X = np.array([[2100,3,20],[2500,4,15],[1800,2,30],[2200,3,25]])
y = np.array([460,540,330,400])

'''We want to solve for an eigenvector, which we define as beta. We want to closely approximate
the vector 'beta' that determines the relative 'weight' of square footage, bedrooms and age
in the final price
'''

beta, _, _, _ = np.linalg.lstsq(X,y,rcond=None) 
print(beta)

priceHouse = (2400*beta[0]+3*beta[1]+20*beta[2])
print(priceHouse) #This doesn't seem right... but my code seems fine?

'''4. The least-squares method is better in this prediction task, as
M is not a square matrix. Thus, we can't use linalg.solve().
In this sense, an iterative method is better suited even if it might in general take longer
'''
