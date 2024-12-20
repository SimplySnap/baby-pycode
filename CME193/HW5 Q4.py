import numpy as np
import scipy
from matplotlib import pyplot as plt

#functions
def funct_X(X_flat, A_flat) -> float:
    diff = X_flat - A_flat
    fX = 0.5 * np.sum(diff ** 2)
    return fX

def gradient_X(X_flat, A_flat):
    '''Calculate the gradient of f(X) with respect to X'''
    return X_flat - A_flat

def gradient_wrapper(X_flat):
    '''Wrapper to pass into scipy's optimize function'''
    return gradient_X(X_flat, A_flat)

def loss_funct(X_flat):
    return funct_X(X_flat, A_flat)

def callback(X_flat):
    '''Callback function to record loss values'''
    lossvec.append(loss_funct(X_flat))

def plot(lossvec):
    plt.plot(lossvec)
    plt.xlabel("Iteration")
    plt.ylabel("Loss Value")
    plt.title("Loss Convergence over Iterations")
    plt.show()



#Initialisation
lossvec = []
X = 100*np.random.rand(100,50)
A = 100*np.random.rand(100,50)
A_flat = A.flatten()


# Minimize the loss function using gradient descent (BFGS algorithm)
result = scipy.optimize.minimize(
    fun=loss_funct,
    x0=X.flatten(),  # Flatten X_initial for the optimizer
    jac=gradient_wrapper,
    callback=callback,
    options={'gtol': 1e-6, 'maxiter': 1000}
)
X = result.x.reshape(100,50)



plot(lossvec)
print(f"Our final loss is{lossvec[-1]}")
