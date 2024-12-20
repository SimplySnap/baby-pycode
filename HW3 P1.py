import numpy as np
import matplotlib as plt

#Problem 1: use power iteration to approximate dominant eigenvecs of M
def PageRankAnswer():
    M = np.array([[0,0,1/2,0],[1/3,0,0,1/2],[1/3,1/2,0,1/2],[1/3,1/2,1/2,0]])

    #Base vector of 1's, which we then iterate over to converge on a dominant eigenvector
    v = np.ones(4)
    v0 = v
    v = M@v
    v = v / np.linalg.norm(v,2)
    v1 = v

    #Convergence criterion
    while (abs(np.linalg.norm(v1)-np.linalg.norm(v0)) > 1e-5):
        v = M@v
        v = v / np.sum(v)
        v0 = v1
        v1 = v
    print(v)

    print("The entries of the eigenvector represent the 'most dominant' ranking of different webpages.\n Each entry represents a different likelihood of being on a different page")
    print("Pages 3 and 4 are equally ranked as the highest, because they have the same values in the dominant eigenvector")

PageRankAnswer()
