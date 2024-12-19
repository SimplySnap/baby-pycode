from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process.kernels import RBF
from sklearn.svm import SVC
#Decision tree


#X,Y as data of height, weight, shoe-size (X) and gender (Y)
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#Decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

nvb = GaussianNB()
nvb.fit(X,Y)

rbf = SVC(kernel='rbf', gamma=2, C=1, random_state=42)
rbf.fit(X,Y)

#Scoring data using test data points
X_test = [[170, 65, 41],  # Example 1
    [160, 55, 38],  # Example 2
    [180, 75, 43],  # Example 3
    [175, 68, 42],  # Example 4
    [165, 60, 39],  # Example 5
    [190, 85, 46],  # Example 6
    [155, 50, 37],  # Example 7
    [185, 80, 44]]

Y_test = ['male', 'female', 'male', 'male', 'female', 'male', 'female', 'male']


print(f"The decision tree's score is {clf.score(X_test,Y_test)}")
print(f"The Naive Bayes' score is {nvb.score(X_test,Y_test)}")
print(f"The RBF kernel score is {rbf.score(X_test,Y_test)}")