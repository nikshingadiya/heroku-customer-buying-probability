from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold, train_test_split
import numpy as np

def validation(clf, X, y):
    lst_accu_stratified = []
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    skf = StratifiedKFold(n_splits=12, shuffle=True, random_state=1)
    for train_index, test_index in skf.split(X, y):
        x_train_fold, x_test_fold = X.loc[train_index, :], X.loc[test_index, :]
        y_train_fold, y_test_fold = y[train_index], y[test_index]
        clf.fit(x_train_fold, y_train_fold)
        y_pre = clf.predict(X_test)
        print(classification_report(y_test, y_pre))
        lst_accu_stratified.append(clf.score(x_test_fold, y_test_fold))

    print('List of possible accuracy:', lst_accu_stratified)
    print('\nMaximum Accuracy That can be obtained from this model is:',
          max(lst_accu_stratified) * 100, '%')
    print('\nMinimum Accuracy:',
          min(lst_accu_stratified) * 100, '%')
    print('\nAverage Accuracy That can be obtained from this model is::', np.mean(lst_accu_stratified))
    print('\n Median Accuracy That can be obtained from this model is::', np.median(lst_accu_stratified))
    print('\nStandard Deviation is:', np.std(lst_accu_stratified))

    return None