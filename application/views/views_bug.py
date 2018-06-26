from __future__ import unicode_literals
from application import app, models
from flask import render_template, redirect, flash, url_for
from ..forms import BugEditForm
from ..controllers import bug_controller


@app.route('/bugs', methods=['GET'])
def view_bugs():
    return render_template('bugs.html',
                           bug_form=BugEditForm(),
                           bug_list=bug_controller.get_all_bugs())


@app.route('/bugs', methods=['POST'])
def add_bug():
    form = BugEditForm()
    if form.validate_on_submit():
        bug = models.Bug(title=form.title.data,
                         description=form.description.data)
        bug_controller.add_bug(bug)
        flash('New bug added!')
    else:
        flash('Some of your fields need fixing!')
        return render_template('bugs.html',
                               bug_form=form,
                               bug_list=bug_controller.get_all_bugs())
                    
    return redirect(url_for('view_bugs'))


@app.route('/bug/<bug_id>/delete', methods=['GET'])
def delete_bug(bug_id):

    if bug_controller.delete_bug(bug_id):
        flash('You deleted a bug!')
    else:
        flash('Something went wrong when deleting that bug.')
    
    return redirect(url_for('view_bugs'))
