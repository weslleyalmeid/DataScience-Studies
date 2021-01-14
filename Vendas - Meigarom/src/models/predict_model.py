import numpy as np
import pandas as pd
import os.path
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score, cross_val_predict


from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

DIR_FILE = os.path.abspath('.')
DIR_DATA = os.path.join(DIR_FILE, 'data')
DIR_BASE = os.path.join(DIR_DATA, 'processed')

df_train = pd.read_csv(os.path.join(DIR_BASE, 'train.csv'))
df_test = pd.read_csv(os.path.join(DIR_BASE, 'test.csv'))

X_train = df_train.drop(labels=['id', 'Response'], axis=1)
X_test = df_test.drop(labels=['id', 'Response'], axis=1)
y_train = df_train['Response']
y_test = df_test['Response']

estimators = [
    RandomForestClassifier(),
    XGBClassifier(),
    LGBMClassifier(),
    CatBoostClassifier()
]

for estimator in estimators:
    estimator.fit(X_train, y_train)

    name = estimator.__class__.__name__

    result = estimator.predict(X_test)




