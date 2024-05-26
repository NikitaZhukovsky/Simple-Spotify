import models
import schemas
from facades.base_facade import BaseFacade
from fastapi import HTTPException, status
from sqlalchemy.future import select


class PlaylistSongFacade(BaseFacade):
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


playlist_song_facade = PlaylistSongFacade()
