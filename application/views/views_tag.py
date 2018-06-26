from __future__ import unicode_literals
from application.flask_app_and_db import app
from application import models
from flask import render_template, redirect, flash, url_for
from ..forms import TagEditForm
from ..controllers import tag_controller


@app.route('/tags', methods=['GET'])
def view_tags():
    tag_list = tag_controller.get_all_tags()
    return render_template('tags.html',
                           tag_list=tag_list)


@app.route('/tag/<tag_id>', methods=['GET'])
def tag_details(tag_id):
    tag_edit_form = TagEditForm()

    tag = tag_controller.get_tag(tag_id)
    if tag:
        tag_edit_form.name.data = tag.name
        tag_edit_form.colour.data = tag.colour
        tag_edit_form.style.data = tag.style
        tag_edit_form.description.data = tag.description
        return render_template('tag_edit.html',
                               tag=tag,
                               tagEditForm=tag_edit_form,
                               edit=True)
    else:
        flash('I couldn''t find any tags with ID {0}: sadface.'.format(tag_id))
        return redirect(url_for('view_tags'))


@app.route('/tag/<tag_id>', methods=['POST'])
def edit_tag(tag_id):
    form = TagEditForm()
    if form.validate_on_submit():
        tag_controller.edit_tag(tag_id,
                                form.name.data,
                                form.colour.data,
                                form.style.data,
                                form.description.data)
        flash('Tag changes saved.')
    else:
        flash('Some of your fields need fixing!')
        tag = tag_controller.get_tag(tag_id)
        return render_template('tag_edit.html',
                               tag=tag,
                               tagEditForm=form,
                               edit=True)
    return redirect(url_for('view_tags'))


@app.route('/tag/<tag_id>/delete', methods=['GET'])
def delete_tag(tag_id):
    tag_name = tag_controller.get_tag(tag_id).name
    if tag_controller.delete_tag(tag_id):
        flash('{0} is gone now. Forever...'.format(tag_name))
        return redirect(url_for('view_tags'))
    else:
        flash('Something went wrong when deleting {0}.'.format(tag_name))
        return redirect(url_for('tag_details', tag_id=tag_id))


@app.route('/tag', methods=['GET'])
def new_tag_form():
    tag_edit_form = TagEditForm()
    return render_template('tag_edit.html',
                           tagEditForm=tag_edit_form,
                           edit=False)


@app.route('/tag', methods=['POST'])
def add_tag():
    form = TagEditForm()
    if form.validate_on_submit():
        tag = models.Tag(name=form.name.data,
                         colour=form.colour.data,
                         description=form.description.data,
                         style=form.style.data)
        tag_controller.add_tag(tag)
        flash('New tag changes added.')
    else:
        flash('Some of your fields need fixing!')
        return render_template('tag_edit.html',
                               tagEditForm=form,
                               edit=False)
    return redirect(url_for('view_tags'))
