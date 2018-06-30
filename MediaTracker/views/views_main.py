from __future__ import unicode_literals
from MediaTracker.flask_app_and_db import flask_app as app
from MediaTracker import models
from flask import render_template, request
from MediaTracker.forms import MediaForm
from MediaTracker.controllers import media_controller, tag_controller

from urllib.parse import urlencode
from collections import OrderedDict


@app.route('/', methods=['GET', 'POST'])
def index():
    tag_id = request.args.get('filter_by_tag') or request.args.get('selected_tag')
    sortcode = request.args.get('do_sort') or request.args.get('selected_sort')
    media_list = media_controller.get_all_media(tag_id, sortcode)
    form = create_new_media_form()
    compressed = request.args.get('compressed')
    return render_template('index.html',
                           media_list=media_list,
                           mediaForm=form,
                           filter_tag=tag_controller.get_tag(tag_id) if tag_id else None,
                           sort=sortcode,
                           compressed=compressed,
                           query_string=create_query_string(tag_id, sortcode, compressed),
                           create_query_string=create_query_string,
                           create_episode_string=create_episode_string)


# Helper functions


def create_query_string(tag_id, sortcode, compressed):
    settings = {k: v for k, v in OrderedDict(selected_tag=tag_id,
                                             selected_sort=sortcode,
                                             compressed=compressed).items() if v}

    return urlencode(settings)


def create_episode_string(media):
    return 'Current episode: ' + ('%.12g' % media.current_episode.episode_number
                                  if media.current_episode else 'Not started')


def create_new_media_form(media=None):
    form = MediaForm()
    # Need to populate episode dropdown choices, otherwise null error during validation
    if media:
        form.current_episode_id.query = media_controller.get_episodes_for_media_query(media.id).order_by(
            models.Episode.episode_number)
        form.tags.choices = [(tag.id, tag.name) for tag in tag_controller.get_all_tags()]

        form.tags.data = [tag.id for tag in media.tags]

    return form


def read_media_form(media=None):
    form = MediaForm()
    # Need to populate episode dropdown choices, otherwise null error during validation
    if media:
        form.current_episode_id.query = media_controller.get_episodes_for_media_query(media.id).order_by(
            models.Episode.episode_number)
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
