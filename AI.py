import tensorflow as tf
import pandas as pd

model = tf.keras.models.load_model('model_Ulan-Ude.h5')
def estimation (floor,count_floor,rooms,district,square):
    data = {
        'floor' : [floor],
        'count_floor': [count_floor],
        'rooms': [rooms],
        'square': [square],
        'district': [district],
    }
    print(data)
    row_labels = [0]
    df = pd.DataFrame(data=data, index=row_labels)
    print(df)
    res = model.predict(df)
    return (int(res[0][0]))

# floor - этаж квартиры (int)
# count_floor - этажность дома (int)
# rooms - количество комнат (int)
# district - район (число от 1 до кол-во районов (1 - Октябрьский район, 2 - Железнодорожный район, 3 - Советский район))
# square - площадь квартиры (float)

print (estimation(4,5,2,1,50)) #пример из презентации