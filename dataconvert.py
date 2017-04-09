import h5py
import numpy as np
'''
f = h5py.File('train_Label.mat','r')
variables = f.items()
f = open('writelabel.txt','w+')
for var in variables:
    labels = np.asarray(var[1].value)
    for i in labels[0]:
        l = int(labels[0][i])
        f.write(str(l))
        f.write('\n')
'''

f = h5py.File('testing_features3_normalized.mat','r')
variables = f.items()
f = open('testfeatures.txt','w+')

for var in variables:
    data = np.asarray(var[1].value)
    data = np.transpose(data)
    for col in data:
        for row in col:
            f.write(str(row))
            f.write(' ')
        f.write('\n')
