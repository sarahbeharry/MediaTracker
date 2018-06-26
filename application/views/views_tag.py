from __future__ import unicode_literals
from application import app, models
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
    tagEditForm = TagEditForm()
    
    tag = tag_controller.get_tag(tag_id)
    if tag:
        tagEditForm.name.data = tag.name
        tagEditForm.colour.data = tag.colour
        tagEditForm.style.data = tag.style
        tagEditForm.description.data = tag.description
        return render_template('tag_edit.html',
                               tag=tag,
                               tagEditForm=tagEditForm,
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
    return redirect(url_for('view_tags'))


@app.route('/tag', methods=['GET'])
def new_tag_form():
    tagEditForm = TagEditForm()
    return render_template('tag_edit.html',
                           tagEditForm=tagEditForm,
                           edit=False)
    

@app.route('/tag', methods=['POST'])
def add_tag():
    form = TagEditForm()
    if form.validate_on_submit():
        tag = models.Tag(name = form.name.data,
                         colour = form.colour.data,
                         description = form.description.data,
                         style = form.style.data)
        tag_controller.add_tag(tag)
        flash('New tag changes added.')
    else:
        flash('Some of your fields need fixing!')
        return render_template('tag_edit.html',
                               tagEditForm=form,
                               edit=False)
    return redirect(url_for('view_tags'))
