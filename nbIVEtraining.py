import numpy as n
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

#load the training data as numpy arrays
trFeatureArr=n.loadtxt('IVEfeattrain.txt', delimiter=',')
trTargetArr=n.loadtxt('IVEtargettrain.txt', delimiter=',')
print(trFeatureArr.shape, '\n')
print(trTargetArr.shape, '\n')
print(trTargetArr)
for i in range(20):
    print(i+10000, '=',trFeatureArr[i+10000])
#fit the training dataset of 20000 ticks using Gaussian naive Bayes
estimator=GaussianNB().fit(trFeatureArr, trTargetArr)

#save the estimator for later use use joblib
joblib.dump(y_estimator, 'GaussianNBIVE.pkl')

testingFeatureArr=n.loadtxt('IVEfeattest.txt', delimiter=',')
prediction=estimator.predict(testingFeatureArr)
#find out how many times the model found that the price move in the right direction
acc=0
for i in range(prediction.size-1):
    actualNow=testinFeatureArr[i,4]
    predNow=prediction[i]
    predNext=prediction.item[i+1]
    if (actualNow < predNext and predNow < predNext) or (actualNow > predNext and predNow > predNext):
        acc+=1
print('accuracy=', acc/19999.0*100, '%')


