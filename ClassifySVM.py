def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    
    
    from sklearn import svm
    ce=1
    gm=100
    clf = svm.SVC(kernel="rbf", gamma=gm, C=ce)
    clf.fit(features_train, labels_train)
    return [clf, ce, gm]