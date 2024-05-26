from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    email: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class ArtistBase(BaseModel):
    name: str
    description: str


class ArtistCreate(ArtistBase):
    pass


class Artist(ArtistBase):
    id: int

    class Config:
        from_attributes = True


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        from_attributes = True


class AlbumBase(BaseModel):
    title: str
    description: str
    artist_id: int


class AlbumCreate(AlbumBase):
    pass


class Album(AlbumBase):
    id: int

    class Config:
        from_attributes = True


class SongBase(BaseModel):
    title: str
    text: str
    album_id: int

    class Config:
        from_attributes = True


class SongCreate(SongBase):
    genres: List[int]


class Song(SongBase):
    id: int
    file_path: str
    class Config:
        from_attributes = True


class FavoriteSongBase(BaseModel):
    song_id: int
    user_id: int


class FavoriteSongCreate(BaseModel):
    song_id: int


class FavoriteSong(FavoriteSongBase):

    class Config:
        from_attributes = True


class PlaylistBase(BaseModel):
    class Config:
        from_attributes = True


class Playlist(PlaylistBase):
    name: str
    
    class Config:
        from_attributes = True


class PlaylistCreate(PlaylistBase):
    name: str


class PlaylistSongBase(BaseModel):
    song_id: int
    playlist_id: int


class PlaylistSongCreate(PlaylistSongBase):
    pass


class PlaylistSong(PlaylistSongBase):

    class Config:
        from_attributes = True






