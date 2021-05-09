import  pandas as pd
import  numpy as np
from sklearn.model_selection import train_test_split
from validation_model import  validation
fd_ran = pd.read_csv("../jupyter/data/Banglore_food_delivery/onlinedeliverydata.csv")

print(fd_ran.head())

fd_ran = fd_ran[['Age',
                 'Ease and convenient',
                 'Time saving',
                 'More restaurant choices',
                 'Easy Payment option',
                 'More Offers and Discount',
                 'Good Food quality',
                 'Good Tracking system',
                 'Unaffordable',
                 'Maximum wait time', 'Output']]

print(fd_ran.info())

print(fd_ran.head())

fd_ran['Age'] = fd_ran['Age'].astype(str)



fd_ran.columns

enc_dict = {}
for i in fd_ran.columns:
    if i == 'Maximum wait time':
        enc_dict[i] = {'30 minutes': 2,
                       '45 minutes': 3,
                       '60 minutes': 1,
                       'More than 60 minutes': 0,
                       '15 minutes': 4}
    elif i == 'Age':
        enc_dict[i] = {'20': 20,
                       '24': 24,
                       '22': 22,
                       '27': 27,
                       '23': 23,
                       '21': 21,
                       '28': 28,
                       '25': 25,
                       '32': 32,
                       '30': 30,
                       '31': 31,
                       '26': 26,
                       '18': 18,
                       '19': 19,
                       '33': 33,
                       '29': 29}
    elif i == 'Output':
        enc_dict[i] = {'Yes': 1, 'No': 0}

    elif i == 'Unaffordable':
        enc_dict[i] = {'Neutral': 2,
                             'Strongly agree': 3,
                             'Agree': 0,
                             'Disagree': 1,
                             'Strongly disagree': 4}
    else:
        enc_dict[i] = {'Neutral': 2,
                                    'Strongly agree': 3,
                                    'Agree': 0,
                                    'Strongly disagree': 4,
                                    'Disagree': 1}

        # enc_dict[i] = {'Neutral': 2,
        #                'Strongly agree': 4,
        #                'Agree': 3,
        #                'Strongly disagree': 0,
        #                'Disagree': 1}

print(enc_dict)

encoded_data = fd_ran.apply(lambda col: col.map(enc_dict[col.name]))

encoded_data.head()

len(fd_ran.columns)

from imblearn.over_sampling import RandomOverSampler

X = encoded_data.iloc[:, 0:10]
y = encoded_data.iloc[:, 10]
nm = RandomOverSampler()  # try to making data balanced
X, y = nm.fit_resample(X, y)

## model building

from sklearn.ensemble import RandomForestClassifier


X_train, X_test, y_train, y_test = train_test_split(X, y)

clf = RandomForestClassifier(max_depth=5, oob_score=True)
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

y_pre = clf.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pre))

from sklearn import metrics

pred_train = np.argmax(clf.oob_decision_function_, axis=1)
metrics.roc_auc_score(y_train, pred_train)

validation(clf, X, y)

# from sklearn.model_selection import GridSearchCV
# clf=RandomForestClassifier()
# parameter=({"n_estimators":[10,20,25,30,40],
#             "criterion":["gini","entropy"],"max_depth":[1,2,4],
#            "min_samples_split":[1,2,4,8,10],"min_samples_leaf":[2,4,8,10,12],
#             "max_features":["auto", "sqrt", "log2"]})

# grid_clf_f = GridSearchCV(estimator=clf, param_grid=parameter,
#                                 scoring='f1', cv = 5, verbose=2,
#                                 n_jobs=-1, return_train_score=True)

# grid_clf_f.fit(X_train, y_train)
# print(grid_clf_f.best_params_)

params = {'criterion': 'gini', 'max_depth': 4, 'max_features': 'auto', 'min_samples_leaf': 10, 'min_samples_split': 8,
          'n_estimators': 50}

clf_f = RandomForestClassifier(**params)
clf_f.fit(X_train, y_train)
clf_f.score(X_test, y_test)

validation(clf_f, X, y)

import pickle

pickle.dump(clf_f, open('model_2.pkl', 'wb'))

model = pickle.load(open('model_2.pkl', 'rb'))

print(clf_f.predict_proba(np.array([20, 2, 3, 4, 3, 1, 1, 3, 4, 5]).reshape(1, -1))[0][1])
