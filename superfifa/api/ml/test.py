# Random Forest Classification
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin',
         'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]
seed = 7
num_trees = 100
max_features = 2
kfold = model_selection.KFold(n_splits=10, random_state=seed)
model = RandomForestClassifier(
    n_estimators=num_trees, max_features=max_features)
results = model_selection.cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
