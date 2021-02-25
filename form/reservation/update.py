from wtforms import Form, validators, HiddenField, DateField


class Update(Form):
    id = HiddenField('ID')
    user_id = HiddenField('UserName')
    hotel_id = HiddenField('HotelName')
    check_in = DateField('チェックイン', [validators.DataRequired()])
    check_out = DateField('チェックアウト', [validators.DataRequired()])


