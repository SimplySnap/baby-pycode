import numpy as np

#We multiply by 100 to create matrices of non-trivial sizes (based on our error threshold)
X = 100*np.random.rand(100,50)
A = 100*np.random.rand(100,50)
alpha = 0.05 #Arbitrary learning rate
lossVec = [] #Initialise losses

def funct_X(X,A)->float:
    '''Run f(X) on X'''
    fX = 0 #Initialise f(X) on first iteration
    for p in range(100):
        for q in range(50):
            fX += ((X[p,q]-A[p,q])**2)
    fX *= 0.5
    return fX

for i in range (1000):
    '''The for loop where we update our X matrix'''
    fX = funct_X(X,A)
    grad = X-A
    Xnew = X - alpha*grad
    #fXnew = funct_X(Xnew,A)

    lossVec.append(fX)
    if i>1 and abs(lossVec[i]-lossVec[i-1]) < 10**(-6): #Getout clause
        print(f"This took {i} iterations")
        break
    
    X = Xnew
print(f"Our losses are{lossVec}")

