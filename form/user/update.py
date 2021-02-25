from wtforms import Form, StringField, validators, HiddenField
from wtforms.fields.html5 import EmailField


class Update(Form):
    id = HiddenField('ID')
    name = StringField('名前', [validators.DataRequired(message='名前を入力してください')])
    katakana_name = StringField('カタカナ', [validators.DataRequired(message='カタカナを入力してください。')])
    mail = EmailField('メール',[validators.DataRequired(), validators.Email()])
    password = StringField('パスワード', [validators.DataRequired(message='パスワードを入力してください')])
    telephone = StringField('電話番号', [validators.DataRequired(message='電話番号を入力してください。')])

