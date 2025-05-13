import pickle
import pandas as pd


def predict_location(hour_list):
    with open('src/models/kmeans.pkl', 'rb') as f:
        model = pickle.load(f)

    data = pd.DataFrame.from_dict(data, orient="index")
    data = data.T

    return model.transform(data)
