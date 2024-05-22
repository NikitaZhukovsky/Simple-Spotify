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


playlist_facade = PlaylistFacade()
