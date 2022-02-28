from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class ChooseType(FlaskForm):
    type = SelectField(u'انواع لباس', choices=[('تی‌شرت', 'تی‌شرت')])
    submit = SubmitField("ادامه")

class tshirtForm(FlaskForm):
    tshirt_type = SelectField('آستین بلند یا کوتاه', choices=[('آستین بلند','آستین بلند'),('آستین کوتاه','آستین کوتاه')])
    neck_type = SelectField('نوع یقه',choices=[('یقه حلقه','یقه حلقه'),('یقه وی','یقه وی')])
    size_kamar = StringField('دور کمر', validators=[DataRequired()])
    dore_sine = StringField('دور سینه', validators=[DataRequired()])
    submit = SubmitField("ادامه")

