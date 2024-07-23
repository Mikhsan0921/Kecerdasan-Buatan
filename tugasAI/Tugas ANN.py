import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Data input dan output
x1 = np.array([5, 3, 9, 4, ])
x2 = np.array([2, 8, 1, 4, ])
y = np.array([19, 11, 23, 8, ])

X = np.column_stack((x1, x2))

# membangun model ANN
model = Sequential()
model.add(Dense(2, activation='relu',)) 
model.add(Dense(500, activation='relu', ))  
model.add(Dense(500, activation='relu', ))  
model.add(Dense(500, activation='relu', ))  
model.add(Dense(1, activation='linear', ))  

# Kompilasi model
model.compile(optimizer='adam', loss='mean_squared_error')

# Latih model 
model.fit(X, y, epochs=500,)

x1_new = 9
x2_new = 1
X_new = np.array([[x1_new, x2_new]])
y_pred = model.predict(X_new)

print(f'\nPrediksi y untuk x1={x1_new} dan x2={x2_new} adalah {y_pred[0][0]}')
