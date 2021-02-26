from wtforms import Form, validators, HiddenField
from models.user import User
from models.hotel import Hotel
from wtforms.fields.html5 import DateField


def user_list():
    return User.query


def hotel_list():
    return Hotel.query


class Add(Form):
    user_id = HiddenField('UserName')
    hotel_id = HiddenField('HotelName')
    check_in = DateField('チェックイン', [validators.DataRequired()])
    check_out = DateField('チェックアウト', [validators.DataRequired()])






