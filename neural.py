import numpy as np 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot as plt

dataset= np.loadtxt("dataset.txt", delimiter=" ")
x=dataset[:,0:2]
y=dataset[:,2]
y=np.reshape(y,(-1,1))

scaler_x=MinMaxScaler()
xscaler=scaler_x.fit_transform(x)

scaler_y=MinMaxScaler()
yscaler=scaler_y.fit_transform(y)

print(x)
print(y)

#Build model
model = Sequential()
model.add(Dense(7, input_dim=2, kernel_initializer='normal', activation='relu'))
model.add(Dense(7, activation='relu'))
model.add(Dense(1, activation='relu' ))
model.summary()

model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])

history= model.fit(xscaler, yscaler, epochs=100, batch_size=2,  verbose=1, validation_split=0.2)


# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()