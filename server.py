from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
import uvicorn
import pandas as pd
import numpy as np
from main import *
from schema import *

app = FastAPI()
recommendation = SpotifyRecommendation(model_data)
@app.get('/')
def home():
    return {"status":"Server is Running"}

@app.post('/Recommendation_system')

async def song_recommder(x:SongRecommendation, request: Request):
    result = await request.json()
    rec = recommendation.recommend(result['song_name'],result['number_of_songs'])
    song = dict(rec['track_name'])

    return song

if __name__=="__main__":
    uvicorn.run('server:app',port=1234,reload=True)