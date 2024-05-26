import models
import schemas
from facades.base_facade import BaseFacade
from fastapi import HTTPException, status
from sqlalchemy.future import select


class PlaylistFacade(BaseFacade):

    async def add_playlist_to_user(self,  playlist_name: str, user_id: int) -> schemas.PlaylistCreate:
        new_playlist = models.Playlist(name=playlist_name, user_id=user_id,)
        self.db.add(new_playlist)
        await self.db.commit()
        await self.db.refresh(new_playlist)

        return new_playlist

    async def get_playlist_songs(self, playlist_id: int, user_id: int) -> list[models.Playlist]:
        songs = select(models.PlaylistSong) \
            .join(models.Playlist, models.PlaylistSong.playlist_id == models.Playlist.id) \
            .where(models.Playlist.id == playlist_id) \
            .where(models.Playlist.user_id == user_id)
        playlist_songs = await self.db.execute(songs)
        return playlist_songs.scalars().all()

    async def add_song_to_playlist(self, song_id: int, playlist_id: int) -> schemas.PlaylistSong:
        song = await self.db.get(models.Song, song_id)
        if not song:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Song not found')

        playlist = await self.db.get(models.Playlist, playlist_id)
        if not playlist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Playlist not found')

        existing_playlist_song = await self.db.execute(
            select(models.PlaylistSong)
            .filter_by(song_id=song_id, playlist_id=playlist_id)
        )
        if existing_playlist_song.scalars().first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Song is already in this playlist')

        playlist_song = models.PlaylistSong(song_id=song_id, playlist_id=playlist_id)
        self.db.add(playlist_song)
        await self.db.commit()
        await self.db.refresh(playlist_song)

        return schemas.PlaylistSong.from_orm(playlist_song)


playlist_facade = PlaylistFacade()
