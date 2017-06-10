# Random Forest Classification
from sklearn import model_selection
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import pandas


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin',
         'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]


# Create tree object
#model = tree.DecisionTreeClassifier(criterion='gini')
model = tree.DecisionTreeRegressor()  # for regression
# model= RandomForestClassifier(n_estimators=1000) # for random forest

# Train the model using the training sets and check score
model.fit(X, Y)
print model.score(X, Y)
# Predict Output
x_test = [2, 174, 88, 37, 120, 44.5, 0.646, 40]
predicted = model.predict(x_test)


print predicted


"""
8,120,86,0,0,28.4,0.259,22,1
2,174,88,37,120,44.5,0.646,24,1
2,106,56,27,165,29.0,0.426,22,0
2,105,75,0,0,23.3,0.560,53,0
4,95,60,32,0,35.4,0.284,28,0
0,126,86,27,120,27.4,0.515,21,0
8,65,72,23,0,32.0,0.600,42,0
2,99,60,17,160,36.6,0.453,21,0
1,102,74,0,0,39.5,0.293,42,1
"""
