import numpy as np
import pandas as pd
import os.path
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score, cross_val_predict, RandomizedSearchCV

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
    print(confusion_matrix(y_test, result, labels=[0, 1]))

    # print('accuracy: ' + accuracy)
    # print('precicion: ' + precicion)
    # print('f1: ' + f1)
    # print('recall: ' + recall)
    # print('roc_auc: ' + roc_auc)


# Random forest e CatBoost se sairam melhores quanto a classificação nos dados de testes, por esse motivo será utilizado o fine-tuning em ambos para verificar
# qual irá perfomar melhor.

paramers = {
    'rfc': {
        'n_estimators': [10, 50, 100, 200],
        'max_features': ['auto', 'sqrt'],
        'max_depth': [8, 16, 32],
        'min_samples_split': [5, 10],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False]
    },

    'cb': {
        'depth': [2, 4, 8, 10],
        'iterations': [250, 100, 500, 1000],
        'learning_rate': [0.03, 0.001, 0.01, 0.1, 0.2, 0.3],
        'l2_leaf_reg': [3, 1, 5, 10, 100],
        'border_count': [32, 5, 10, 20, 50, 100, 200],
        'ctr_border_count': [50, 5, 10, 20, 100, 200],
        'thread_count': 4
    }
}

rfc = RandomForestClassifier()
rf_random = RandomizedSearchCV(estimator=rfc, param_distributions=paramers['rfc'], n_iter=100, cv=3, verbose=1, random_state=42, n_jobs=-1)
rf_random.fit(X_train, y_train)

# RandomForestClassifier(bootstrap=False, max_depth=32, max_features='sqrt',
#                        min_samples_split=5, n_estimators=200)

# rfc_best = {'n_estimators': 200,
#  'min_samples_split': 5,
#  'min_samples_leaf': 1,
#  'max_features': 'sqrt',
#  'max_depth': 32,
#  'bootstrap': False}