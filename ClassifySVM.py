def classify(features_train, labels_train):   

    
    
    from sklearn import svm
    ce=13
    gm=1
    clf = svm.SVC(kernel="rbf", gamma=gm, C=ce)
    clf.fit(features_train, labels_train)
    return [clf, ce, gm]
