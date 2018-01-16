import numpy as np
import keras
from keras.models import Sequential
from sklearn.metrics import confusion_matrix
from keras.layers import Dense, Dropout
import pandas as pd



df = pd.read_csv('RevData/bottleTrain/bottleMyoData1.csv')
df.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']

for i in range(2,21):
	df2 = pd.read_csv('RevData/bottleTrain/bottleMyoData%d.csv' % i)
	df2.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']	
	df = df.append(df2)
	

#print(df)

df3 = pd.read_csv('RevData/bottleIncorrect/bottleMyoData1.csv')
df3.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']

for i in range(2,21):
	df4 = pd.read_csv('RevData/bottleIncorrect/bottleMyoData%d.csv' % i)
	df4.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']	
	df3 = df3.append(df4)

#print(df)


# SWAP out

#x_train = np.append(df.values, df3.values)
x_train = np.vstack((df.values, df3.values))

y_train = [1] * len(df.values) + [0] * len(df3.values)


df5 = pd.read_csv('RevData/bottleCorrect/bottleMyoData1.csv')
df5.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']

for i in range(2,4):
	df6 = pd.read_csv('RevData/bottleCorrect/bottleMyoData%d.csv' % i)
	df6.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']	
	df5 = df5.append(df6)

df7 = pd.read_csv('RevData/bottleIncorrect/bottleMyoData21.csv')
df7.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']

for i in range(22,30):
	df8 = pd.read_csv('RevData/bottleIncorrect/bottleMyoData%d.csv' % i)
	df8.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']	
	df7 = df7.append(df8)



x_test = np.vstack((df5.values, df7.values))
y_test = [1] * len(df5.values) + [0] * len(df7.values)

model = Sequential()
model.add(Dense(1024, input_dim=8, activation='sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(32, input_dim=8, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='relu'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=5,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)

print('Test score:', score[0])
print('Test accuracy:', score[1])