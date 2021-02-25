from wtforms import Form, StringField, TextAreaField, validators, IntegerField, HiddenField
from models.district import District
from wtforms.ext.sqlalchemy.fields import QuerySelectField


def district_list():
    return District.query


class Update(Form):
    id = HiddenField('ID')
    name = StringField('ホテル名前', [validators.DataRequired(message='名前を入力してください')])
    name_en = StringField('NAME', [validators.DataRequired(message='英語名前を入力してください。')])
    img_src = StringField('写真', [validators.DataRequired(message='写真のファイル名を入力してください。')])
    district = QuerySelectField('地域', query_factory=district_list, allow_blank=True)
    address = StringField('住所', [validators.DataRequired(message='住所を入力してください。')])
    price = IntegerField(
        '値段',
        [
            validators.DataRequired(message='値段を入力してください。'),
            validators.NumberRange(min=1, max=50000, message="1円以上５万円以内の値段を入力してください。")
        ]
    )
    station = StringField('最寄り駅', [validators.DataRequired(message='最寄り駅を入力してください。')])
    summary = TextAreaField('ホテル紹介', [validators.DataRequired(message='短いの紹介を入力してください。')])
    introduction = TextAreaField('ホテル情報', [validators.DataRequired(message='ホテルの情報を入力してください。')])
    room_size = IntegerField('部屋広さ', [validators.DataRequired(message='部屋サイズを０以上に設定してください。')])
    max_ppl = IntegerField('最大人数', [validators.DataRequired(message='人数設定は０人以上にしてください。')])
    equipments = StringField('施設 ', [validators.DataRequired(message='施設を入力してください。')])
