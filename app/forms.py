from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DecimalField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class propertyForm(FlaskForm):
    title = StringField('Title', validators = [InputRequired()])
    num_bedroom = IntegerField('No. of Bedrooms', validators = [InputRequired()])
    num_bathroom = IntegerField('No. Of Bathroom', validators = [InputRequired()])
    location = TextAreaField('Location', validators = [InputRequired()])
    price = DecimalField('Price', validators = [InputRequired()])
    type = SelectField(u'Type of House', choices = [('Apartment'),('House')])
    description = TextAreaField('Description', validators = [InputRequired()])
    photo = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], "Images ONLY!")])
