import pandas as pd
import numpy as np 
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("Dataset/preprocessed_data.csv")

model_data = data.drop(columns= 'artist')

numerical = model_data.select_dtypes(exclude='object')

cluster_model = KMeans(n_clusters= 25, max_iter= 1250, random_state= 35)
cluster = cluster_model.fit_predict(numerical)
model_data['cluster'] = cluster