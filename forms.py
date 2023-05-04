from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class CoffeeForm(FlaskForm):
    name = StringField(label='Name', validators = [DataRequired()])
    location = StringField(label='Location', validators = [DataRequired()])
    openTime = StringField(label='Open Time', validators = [DataRequired()])
    closeTime = StringField(label='Close Time', validators=[DataRequired()])
    coffee = SelectField(label='Coffee', choices=['☕','☕☕','☕☕☕','☕☕☕☕'])
    wifi = SelectField(label='Wifi', choices=['💪','💪💪','💪💪💪','💪💪💪💪','✘'])
    power = SelectField(label='Power',choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌'])
    submit = SubmitField(label='Submit')