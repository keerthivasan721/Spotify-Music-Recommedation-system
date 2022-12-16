import pandas as pd
import numpy as np
from tqdm import tqdm
from source import *

class SpotifyRecommendation():
    def __init__(self, dataset):
        self.dataset = dataset
    def recommend(self, songs, amount = 5):
        distance = []
        song_data = self.dataset[(self.dataset.track_name.str.lower() == songs.lower())].head(1).values[0]
        rec_data = self.dataset[(self.dataset.track_name.str.lower() != songs.lower())]

        for songs in tqdm(rec_data.values):
            dist = 0
            for col in np.arange(len(rec_data.columns)):
                if not col in [0]:
                    dist = dist + np.abs(float(song_data[col]) - float(songs[col]))
            distance.append(dist)
        
        rec_data['distance'] = distance

        rec_sorted = rec_data.sort_values('distance')
        rec_sorted.reset_index(drop = True, inplace = True)

        columns = ['track_name']
        return rec_sorted[columns][:amount]


recommendation = SpotifyRecommendation(model_data)