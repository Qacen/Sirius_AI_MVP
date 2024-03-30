import warnings
from sklearn.model_selection import train_test_split
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import nltk

nltk.download('all')
from nltk.stem import WordNetLemmatizer

lemm = WordNetLemmatizer()

warnings.filterwarnings("ignore")


data = pd.read_csv("Ulan-Ude_DataSet.csv")
print(data.values)
features = data[['floor','count_floors','rooms','square','district']]
prices = data['price']

X_train, X_test, y_train, y_test = train_test_split(features, prices, test_size=0.1, random_state=56)
print(X_train.shape)

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(128, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

# Компиляция модели
model.compile(optimizer='adam', loss='mean_squared_error')

# Обучение модели
model.fit(X_train, y_train, epochs=1000, batch_size=16, validation_split=0.2)

model.save('model_Ulan-Ude.h5')




