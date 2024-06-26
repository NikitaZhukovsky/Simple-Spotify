"""version_4

Revision ID: 588293fd98fd
Revises: 0d682ae74d54
Create Date: 2024-05-15 20:32:47.155668

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '588293fd98fd'
down_revision: Union[str, None] = '0d682ae74d54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_songs',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'song_id')
    )
    op.drop_table('favourite_songs')
    op.add_column('playlist_songs', sa.Column('playlist_id', sa.Integer(), nullable=False))
    op.drop_constraint('playlist_songs_user_id_fkey', 'playlist_songs', type_='foreignkey')
    op.create_foreign_key(None, 'playlist_songs', 'playlists', ['playlist_id'], ['id'])
    op.drop_column('playlist_songs', 'user_id')
    op.alter_column('song_genre_association', 'genre_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('song_genre_association', 'genre_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('playlist_songs', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'playlist_songs', type_='foreignkey')
    op.create_foreign_key('playlist_songs_user_id_fkey', 'playlist_songs', 'playlists', ['user_id'], ['id'])
    op.drop_column('playlist_songs', 'playlist_id')
    op.create_table('favourite_songs',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('song_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], name='favourite_songs_song_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='favourite_songs_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', 'song_id', name='favourite_songs_pkey')
    )
    op.drop_table('favorite_songs')
    # ### end Alembic commands ###
