from wtforms import Form
from wtforms import  StringField
from wtforms import TextField


class CommentForm(Form):
    username=StringField('username')
    
    comment=TextField("Comentario")