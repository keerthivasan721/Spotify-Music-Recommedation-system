from fastapi import FastAPI,Request
import uvicorn
import pandas as pd
import numpy as np
from main import *

app = FastAPI()

@app.get('/')
def home():
    return {"status":"Server is Running"}

#@app.post('/recommend')

# async def song_rec(x: input(), y: input(), request: Request):
#     result = await request.json()
#     recommendation = SpotifyRecommendation(model_data)

#     rec = recommendation.recommend(x,y)

#     return {rec}

if __name__=="__main__":
    uvicorn.run('server:app',port=1234,reload=True)





