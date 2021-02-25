from wtforms import Form, StringField, validators, PasswordField
from wtforms.fields.html5 import EmailField


class Add(Form):
    name = StringField('名前', [validators.DataRequired(message='名前を入力してください')])
    katakana_name = StringField('カタカナ', [validators.DataRequired(message='カタカナを入力してください。')])
    mail = EmailField('メール',[validators.DataRequired(), validators.Email()])
    password = PasswordField('パスワード', [validators.DataRequired(), validators.EqualTo('confirm', message='パスワードは一致しません')])
    confirm = PasswordField('パスワード確認')
    telephone = StringField('電話番号', [validators.DataRequired(message='電話番号を入力してください。')])


