from app import db, models

# database i/o
# media
def get_all_media():
	return models.Media.query.all()

def get_media(media_id):
	return models.Media.query.filter_by(id=media_id).first()

def add_media(media):
	db.session.add(media)
	db.session.commit()

def edit_media(media_id, name, current_episode_id, notes):
	media = get_media(media_id)
	if media:
		media.name = name
		media.current_episode_id = current_episode_id
		media.notes = notes
		update_media(media)

def update_media(media):
	db.session.merge(media)
	db.session.commit()

def delete_media(media_id):
	media = get_media(media_id)
	if media:
		# TODO: Get sql-alchemy to handle episode deletes for me
		get_episodes_for_media_query(media_id).delete(synchronize_session='fetch')
		db.session.delete(media)
		db.session.commit()
		return True
	else:
		return False

# episode

def get_episodes_for_media_query(media_id):
	return models.Episode.query.filter_by(media_id = media_id)

def increment_episode(media_id):
	media = get_media(media_id)
	if media.episodes:
		if media.current_episode:
			# Only change if this episode is not the last one
			i = iter(media.episodes)
			for item in i:
				if item.id == media.current_episode_id and item.id != media.episodes[-1].id:
					media.current_episode_id = next(i).id
					update_media(media)
					return True
					break
				
		else:
			# Current episode is the first one
			media.current_episode_id = iter(media.episodes).next().id
			update_media(media)
			return True
	
	return False

def add_episode(episode):
	db.session.add(episode)
	db.session.commit()

def delete_episode(episode_id):
	episode = models.Episode.query.filter_by(id = episode_id).first()
	if episode:
		db.session.delete(episode)
		db.session.commit()
		return True
	else:
		return False

# Generate n episodes 
def generate_episodes(media_id, count):
	media = get_media(media_id)
	if media.episodes:
		last_episode = media.episodes[-1]
		last_episode_number_floor = int(last_episode.episode_number)
	else:
		last_episode_number_floor = 0
	for i in range(last_episode_number_floor + 1, last_episode_number_floor + 1 + count):
                episode = models.Episode(episode_number = i,
                                        media_id = media_id)
                add_episode(episode)

def delete_all_episodes(media_id):
	get_episodes_for_media_query(media_id).delete(synchronize_session='fetch')
	db.session.commit()
	return True
