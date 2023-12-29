import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class Track(BaseModel):
    track_id: str
    artists: str
    album_name: str
    track_name: str
    popularity: int
    duration_ms: int
    explicit: bool
    danceability: float
    energy: float
    key: int
    loudness: float
    mode: int
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    time_signature: int
    track_genre: str
    
class Tracks(BaseModel):
    tracks: List[Track]

app = FastAPI(
    title="Spotify Tracks Data Server",
    description="Servidor para visualizar datos de pistas de Spotify",
    version="1.0.0",
)

def load_data(file_path: str) -> Optional[pd.DataFrame]:
    try:
        df = pd.read_csv(file_path)
        df.fillna(0, inplace=True)
        return df
    except FileNotFoundError:
        return None
    except pd.errors.ParserError:
        return None

@app.get("/tracks/", response_model=Tracks)
def get_tracks():
    track_data = pd.read_csv('train.csv')
    track_data.fillna(0, inplace=True)
    tracks_dict = track_data.to_dict(orient='records')
    tracks_list = Tracks(tracks=tracks_dict)
    return tracks_list

'''@app.get("/tracks/", response_model=Tracks)
def get_tracks():
    track_data = load_data('train.csv')
    if track_data is None:
        raise HTTPException(status_code=404, detail="Archivo de datos no encontrado o formato inválido.")
    
    tracks_dict = track_data.to_dict(orient='records')
    tracks_list = Tracks(tracks=tracks_dict)
    return tracks_list'''

df = pd.read_csv('train.csv', index_col=0)

