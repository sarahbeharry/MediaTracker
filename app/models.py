from app import db

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(256), index=True, unique=True)
    current_episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
    notes = db.Column(db.Unicode(256))

    episodes = db.relationship('Episode', 
                                backref='media',
                                foreign_keys='Episode.media_id',
                                order_by='Episode.episode_number')
    current_episode = db.relationship('Episode', foreign_keys='Media.current_episode_id')
    
    tags = db.relationship('Tag',
                            secondary='media_tag')
    last_updated = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<Media: ID {0}, Name {1}, Current episode ID {2}>'.format(self.id, self.name, self.current_episode_id)
    

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id', ondelete="CASCADE"),
                 nullable=False)
    episode_number = db.Column(db.Numeric, unique=True)
    
    def __repr__(self):
        return '<Episode: ID {0}, {1} - {2}>'.format(self.id, self.media.name, self.number)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(256), index=True, unique=True)
    colour = db.Column(db.Unicode(7))
    tagged_media = db.relationship('Media',
                            secondary='media_tag')
    
class Media_Tag(db.Model):
    __tablename__ = 'media_tag'
    media_id = db.Column('media_id', db.Integer, db.ForeignKey('media.id'), primary_key = True)
    tag_id = db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key = True)

