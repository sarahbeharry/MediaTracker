from app import app, models
from flask import render_template, redirect, flash, url_for
from ..forms import MediaForm
from ..controllers import media_controller


@app.route('/', methods=['GET', 'POST'])
def index():
	media_list = media_controller.get_all_media()	
	form = create_new_media_form()
	return render_template('index.html', 
				media_list = media_list,
				mediaForm = form)

@app.route('/media', methods=['POST'])
def add_media():
	form = create_new_media_form()
	if form.validate_on_submit():
		media = models.Media(name = form.name.data, notes = form.notes.data)
		media_controller.add_media(media)
		flash('Added {0}'.format(media.name))
		return redirect(url_for('index'))
	else:
		flash('Some of your fields need fixing!')
		return render_template('index.html',
					mediaForm = form,
					media_list = media_controller.get_all_media())

@app.route('/media/<media_id>', methods=['GET'])
def media_details(media_id):
	episodeForm = EpisodeForm()
	episodeGenerationForm = EpisodeGenerationForm()
	media = media_controller.get_media(media_id)
	if media:
		mediaForm = create_new_media_form(media)
		mediaForm.name.data = media.name
		mediaForm.current_episode_id.data = media.current_episode
		mediaForm.notes.data = media.notes
		return render_template('media_details.html',
					media = media,
					episodes = media.episodes,
					episodeForm = episodeForm,
					episodeGenerationForm = episodeGenerationForm,
					mediaForm = mediaForm)
	else:
		flash('I couldn''t find any media with ID {0}: sadface.'.format(media_id))
		return redirect(url_for('index'))


@app.route('/media/<media_id>', methods=['POST'])
def edit_media(media_id):
	media = media_controller.get_media(media_id)
	mediaForm = create_new_media_form(media)
	
	if mediaForm.validate_on_submit():
		current_episode_id = mediaForm.current_episode_id.data.id if mediaForm.current_episode_id.data else None
		media_controller.edit_media(media_id, mediaForm.name.data, current_episode_id, mediaForm.notes.data)
		flash('Changes to {0} have been saved.'.format(mediaForm.name.data))
	else:
		flash('Some of your fields need fixing!')
		return render_template('media_details.html',
					media = media,
					episodeForm = EpisodeForm(),
					episodeGenerationForm = EpisodeGenerationForm(),
					mediaForm = mediaForm)
	
	return redirect(url_for('media_details', media_id = media_id))

@app.route('/media/<media_id>/delete', methods=['GET'])
def delete_media(media_id):
	media_name = media_controller.get_media(media_id).name
	if media_controller.delete_media(media_id):
		flash('{0} is gone now. Forever...'.format(media_name))
		return redirect(url_for('index'))
	else:
		flash('Something went wrong when deleting {0}.'.format(media_name))
		return redirect(url_for('media_details', media_id = media_id))
	
@app.route('/media/<media_id>/episode', methods=['POST'])
def add_episode(media_id):
	form = EpisodeForm()
	if form.validate_on_submit():
		episode = models.Episode(episode_number = form.number.data,
					media_id = media_id)
		media_controller.add_episode(episode)
	else:
                flash('Episode numbers should probably be numbers...')

	return redirect(url_for('media_details', media_id = media_id))

@app.route('/media/<media_id>/episode/<episode_id>/delete', methods=['GET'])
def delete_episode(media_id, episode_id):
	if media_controller.delete_episode(episode_id):
		flash('You deleted an episode!')
	else:
		flash('Something went wrong when deleting that episode.')
	
	return redirect(url_for('media_details', media_id = media_id))

@app.route('/media/<media_id>/episode/deleteAll', methods=['GET'])
def delete_all_episodes(media_id):
	if media_controller.delete_all_episodes(media_id):
		flash('No more episodes!')
	else:
		flash('Something went wrong when deleting all those episodes.')

	return redirect(url_for('media_details', media_id = media_id))

@app.route('/media/<media_id>/episode/increment', methods=['GET'])
def increment_episode(media_id):
	media_name = media_controller.get_media(media_id).name
	if media_controller.increment_episode(media_id):
		flash('Thanks for watching {0}!'.format(media_name))
	else:
		flash('You have just watched the last episode of {0}!'.format(media_name))
	return redirect(url_for('index'))

@app.route('/media/<media_id>/episode/generate', methods=['POST'])
def generate_episodes(media_id):
	form = EpisodeGenerationForm()
	count = form.number.data

	if count:
		count = form.number.data
		media_controller.generate_episodes(media_id, count)
		flash('You just made {0} new episodes!'.format(count))
	else:
		flash('You should probably put nicer numbers in that episode generation form.')


	return redirect(url_for('media_details', media_id = media_id))


# Helper functions
def create_new_media_form(media = None):
	form = MediaForm()
	 # Need to populate episode dropdown choices, otherwise null error during validation
	if media:
		form.current_episode_id.query = media_controller.get_episodes_for_media_query(media.id).order_by(models.Episode.episode_number)
	
	return form


# Error pages
@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	return render_template('500.html'), 500

@app.errorhandler(503)
def method_not_supported(error):
        return render_template('500.html'), 503

