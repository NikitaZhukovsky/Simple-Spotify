import models
import schemas
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status, Depends, APIRouter
from async_db import get_db
from users import get_current_user
from facades.file_facade import FILE_MANAGER
from facades.song_facade import song_facade
from facades.genre_facade import genre_facade
from facades.favorite_song_facade import favorite_song_facade
from facades.playlist_facade import playlist_facade

router = APIRouter(
    prefix='/api',
    tags=['API']
)


@router.post('/favorites/', response_model=schemas.FavoriteSong)
async def add_favourite_song(
        song_data: schemas.FavoriteSongCreate,
        current_user: models.User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    favorite_song = await favorite_song_facade.add_favorite_song(
        song_id=song_data.song_id, user_id=current_user.id
    )
    return favorite_song


@router.post('/playlists/', response_model=schemas.Playlist)
async def add_playlist(
        playlist_data: schemas.PlaylistCreate,
        current_user: models.User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    playlist = await playlist_facade.add_playlist_to_user(
        playlist_name=playlist_data.name, user_id=current_user.id,
    )
    return playlist


@router.get('/favorites/', response_model=list[schemas.Song])
async def get_user_favourites(
        current_user: models.User = Depends(get_current_user)
):
    favorite_songs = await favorite_song_facade.get_user_favorites(user_id=current_user.id)
    return favorite_songs


@router.get('/songs/genre/{genre_id}/', response_model=list[schemas.Song])
async def get_songs_by_genre(
        genre_id: int,
        current_user: models.User = Depends(get_current_user)
):
    songs = await song_facade.get_songs_by_genre(genre_id)
    return songs
