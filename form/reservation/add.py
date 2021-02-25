from wtforms import Form, validators, HiddenField, DateField


class Add(Form):
    user_id = HiddenField('UserName')
    hotel_id = HiddenField('HotelName')
    check_in = DateField('チェックイン',[validators.DataRequired()])
    check_out = DateField('チェックアウト', [validators.DataRequired()])



