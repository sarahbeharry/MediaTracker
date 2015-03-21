from app import app, models
from flask import render_template, redirect, flash, url_for, request
from .forms import *
from . import media_controller, tag_controller


@app.route('/', methods=['GET', 'POST'])
def index():
    tag_id = request.args.get('tag')
    if tag_id:
        media_list = media_controller.get_all_media(tag_id)
    else:
        media_list = media_controller.get_all_media()
    form = create_new_media_form()
    return render_template('index.html', 
                media_list = media_list,
                mediaForm = form,
                filter_tag = tag_controller.get_tag(tag_id) if tag_id else None)

# Helper functions
def create_new_media_form(media = None):
    form = MediaForm()
     # Need to populate episode dropdown choices, otherwise null error during validation
    if media:
        form.current_episode_id.query = media_controller.get_episodes_for_media_query(media.id).order_by(models.Episode.episode_number)
        form.tags.choices = [(tag.id, tag.name) for tag in tag_controller.get_all_tags()]
        
        form.tags.data = [tag.id for tag in media.tags]
        
    return form
    
def read_media_form(media = None):
    form = MediaForm()
     # Need to populate episode dropdown choices, otherwise null error during validation
    if media:
        form.current_episode_id.query = media_controller.get_episodes_for_media_query(media.id).order_by(models.Episode.episode_number)
        form.tags.choices = [(tag.id, tag.name) for tag in tag_controller.get_all_tags()]
        
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

