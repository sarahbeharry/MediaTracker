from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import DecimalField as _DecimalField
from wtforms.fields import IntegerField

class DecimalField(_DecimalField):
  def _value(self):
    try:
      float(self.data) #check whether you have a 'number'
      return super(DeciamlField, self)._value()
    except (TypeError, ValueError): #self.data is 'None', 'asdf' ...
      return text_type(self.data) if self.data else ''

class MediaForm(Form):
	name = StringField('name', validators=[Length(min=1, max=256), DataRequired()])
	notes = StringField('notes', validators=[Length(min=0, max=256)])
	current_episode_id = QuerySelectField(get_label=lambda e: '%.12g' % e.episode_number, allow_blank=True, blank_text='None')

class EpisodeForm(Form):
	number = DecimalField('episode_number', validators=[DataRequired()])

class EpisodeGenerationForm(Form):
	number = IntegerField('number', validators=[DataRequired()])
