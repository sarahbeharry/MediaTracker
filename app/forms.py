from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, TextAreaField, widgets, RadioField
from wtforms.validators import DataRequired, Length, Regexp, Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import DecimalField as _DecimalField
from wtforms.fields import IntegerField
from wtforms.widgets import TextArea

class DecimalField(_DecimalField):
  def _value(self):
    try:
      float(self.data) #check whether you have a 'number'
      return super(DecimalField, self)._value()
    except (TypeError, ValueError): #self.data is 'None', 'asdf' ...
      return text_type(self.data) if self.data else ''

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class MediaForm(Form):
	name = StringField('name', validators=[Length(min=1, max=256), DataRequired()])
	notes = StringField('notes', validators=[Length(min=0, max=256)])
	current_episode_id = QuerySelectField(get_label=lambda e: '%.12g' % e.episode_number, allow_blank=True, blank_text='None')
	tags = MultiCheckboxField('tags', coerce=int)

class EpisodeForm(Form):
	number = DecimalField('episode_number', validators=[DataRequired()])

class EpisodeGenerationForm(Form):
	number = IntegerField('number', validators=[DataRequired()])
	
class TagEditForm(Form):
    name = StringField('name', validators=[Length(min=1, max=256), DataRequired()])
    description = StringField('description', validators=[Length(min=0, max=256)])
    colour = StringField('colour', validators=[Regexp('^#[A-Fa-f0-9]{6}$', flags=0, message='Invalid colour hex code.'), DataRequired()])
    style = RadioField('style',choices=[('stop','stop'),('asterisk','asterisk'), ('heart', 'heart'),('star','star'),('user','user'),('cog','cog'),('bookmark','bookmark'),('tint','tint'),('flash','flash'),('record','record'),('music','music'),('tower','tower'),('tree-deciduous','tree-deciduous'),('globe', 'globe'),('glass', 'glass')], validators=[Required(message="Please select a tag style")])
    
class BugEditForm(Form):
    title = StringField('title', validators=[Length(min=1, max=256), DataRequired()])
    description = StringField('description', widget=TextArea(), validators=[Length(min=1, max=1024), DataRequired()])
