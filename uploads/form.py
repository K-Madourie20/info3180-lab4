from flak_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    picture = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'],'Image Only')])
