import numpy as np
import pandas as pd
import os.path
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score, cross_val_predict

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

np.random.seed(42)

DIR_FILE = os.path.abspath('.')
DIR_DATA = os.path.join(DIR_FILE, 'data')
DIR_BASE = os.path.join(DIR_DATA, 'processed')

df_train = pd.read_csv(os.path.join(DIR_BASE, 'train.csv'))
df_test = pd.read_csv(os.path.join(DIR_BASE, 'test.csv'))

X_train = df_train.drop(labels=['Response'], axis=1)
X_test = df_test.drop(labels=['id', 'Response'], axis=1)
y_train = df_train['Response']
y_test = df_test['Response']

estimators = [
    RandomForestClassifier(),
    XGBClassifier(),
    LGBMClassifier(),
    CatBoostClassifier(verbose=False)
]

for estimator in estimators:
    estimator.fit(X_train, y_train)
    result = estimator.predict(X_test)
    name = estimator.__class__.__name__

    # accuracy = cross_val_score(estimator, X_train, y_train, cv=5, scoring='accuracy', n_jobs=3).mean()
    # precicion = cross_val_score(estimator, X_train, y_train, cv=5, scoring='precicion', n_jobs=3).mean()
    # f1 = cross_val_score(estimator, X_train, y_train, cv=5, scoring='f1', n_jobs=3).mean()
    # recall = cross_val_score(estimator, X_train, y_train, cv=5, scoring='recall', n_jobs=3).mean()
    # roc_auc = cross_val_score(estimator, X_train, y_train, cv=5, scoring='roc_auc', n_jobs=3).mean()

    print('Estimator: ' + name)
    print(classification_report(y_test, result))
    print(confusion_matrix(y_test, result))

    # print('accuracy: ' + accuracy)
    # print('precicion: ' + precicion)
    # print('f1: ' + f1)
    # print('recall: ' + recall)
    # print('roc_auc: ' + roc_auc)
    




