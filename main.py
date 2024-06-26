from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
import users
from async_db import get_db
from facades.artist_facade import artist_facade
from facades.genre_facade import genre_facade
from facades.album_facade import album_facade
from facades.song_facade import song_facade
from facades.favorite_song_facade import favorite_song_facade
from facades.playlist_facade import playlist_facade

import admin
import views


def set_db_for_facades(db):
    artist_facade.set_db(db)
    genre_facade.set_db(db)
    album_facade.set_db(db)
    song_facade.set_db(db)
    favorite_song_facade.set_db(db)
    playlist_facade.set_db(db)


OAUTH2_SCHEME = OAuth2PasswordBearer('users/login/')

app = FastAPI()


@app.on_event('startup')
async def startup_event():
    async for db in get_db():
        set_db_for_facades(db)
        break


app.include_router(users.router)
app.include_router(admin.router)
app.include_router(views.router)


@app.get('/')
async def index():
    return {'message': 'Hello world'}


