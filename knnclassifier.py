from sklearn.neighbors import KNeighborsClassifier
import numpy as np

f = open('writelabel.txt','r+')
labels = []
for i in f:
    a,b = i.split('\n')
    a = int(a)

    labels.append(a)

del f,a,b

g = open('writefeatures.txt','r+')
count = 0
features = []
for i in g:
    count = count + 1
    list = i.split()
    newlist = [float(i) for i in list]
    del list
    features.append(newlist)
    del newlist
    print (count)
del i,g,count
neigh = KNeighborsClassifier(n_neighbors=50)
neigh.fit(features, labels)
print ("done")
count = 0
h = open('testfeatures.txt','r+')
testfeatures = []
for i in h:
    count = count + 1
    list = i.split()
    newlist = [float(i) for i in list]
    del list
    testfeatures.append(newlist)
    del newlist
    print (count)
del i,h,count
prob = []

for i in testfeatures:
    prob.append(neigh.predict_proba(i))

k = open('probabilities.txt','w+')
k.write(str(prob))
