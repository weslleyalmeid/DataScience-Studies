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
    print(classification_report(y_test, result, zero_division=True))
    print(confusion_matrix(y_test, result, labels=[0, 1]))

    # print('accuracy: ' + accuracy)
    # print('precicion: ' + precicion)
    # print('f1: ' + f1)
    # print('recall: ' + recall)
    # print('roc_auc: ' + roc_auc)


# Random forest se saiu melhor quanto a classificação nos dados de testes, por esse motivo será utilizado o fine-tuning apenas nele
# qual irá perfomar melhor.

paramers = {
    'n_estimators': [10, 100, 500, 1000],
    'max_features': ['auto', 'sqrt'],
    'max_depth': [8, 16, 32, 64],
    'min_samples_split': [2, 4, 8],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

rfc = RandomForestClassifier()
rfc_random = RandomizedSearchCV(estimator=rfc, param_distributions=paramers, n_iter=50, cv=5, verbose=1, random_state=42, n_jobs=-1)
rfc_random.fit(X_train, y_train)
result = rfc_random.predict(X_test)

with open(f'{rfc.__class__.__name__}.txt', 'a') as f:
    f.write('Melhores parametros \n')
    f.write(str(rfc_random.best_params_))

    f.write('\n\nMatriz de confusão \n')
    f.write(str(confusion_matrix(y_test, result, labels=[0, 1])))

    f.write('\n\nClassification Report \n')
    f.write(str(classification_report(y_test, result, zero_division=True)))

    f.write('\n----- ENCERRADO ----- \n\n')

# cb = CatBoostClassifier(verbose=False)
# cb_random = RandomizedSearchCV(
#     estimator=cb, param_distributions=paramers['cb'], n_iter=100, cv=10, verbose=1, random_state=42, n_jobs=-1)
# cb_random.fit(X_train, y_train)