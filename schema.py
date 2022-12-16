from pydantic import BaseModel

class SongRecommendation(BaseModel):
    song_name : str
    number_of_songs : int