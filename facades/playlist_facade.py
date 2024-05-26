import models
import schemas
from facades.base_facade import BaseFacade

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


playlist_facade = PlaylistFacade()
