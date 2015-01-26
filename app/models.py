from app import db

class Media(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(256), index=True, unique=True)
	current_episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
	notes = db.Column(db.String(256))

	episodes = db.relationship('Episode', backref='media', #lazy='dynamic',
			foreign_keys='Episode.media_id', #cascade='all, delete, delete-orphan',
			order_by='Episode.episode_number')
	current_episode = db.relationship('Episode', foreign_keys='Media.current_episode_id')

	def __repr__(self):
		return '<Media: ID {0}, Name {1}, Current episode ID {2}>'.format(self.id, self.name, self.current_episode_id)
	

class Episode(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	media_id = db.Column(db.Integer, db.ForeignKey('media.id', ondelete="CASCADE"),
				 nullable=False)
	episode_number = db.Column(db.Numeric, unique=True)
	
        def __repr__(self):
                return '<Episode: ID {0}, {1} - {2}>'.format(self.id, self.media.name, self.number)

