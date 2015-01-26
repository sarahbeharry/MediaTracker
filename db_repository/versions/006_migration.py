from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
episode = Table('episode', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('media_id', INTEGER, nullable=False),
    Column('number', VARCHAR(length=10)),
)

episode = Table('episode', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('media_id', Integer, nullable=False),
    Column('episode_number', Numeric),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['episode'].columns['number'].drop()
    post_meta.tables['episode'].columns['episode_number'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['episode'].columns['number'].create()
    post_meta.tables['episode'].columns['episode_number'].drop()
