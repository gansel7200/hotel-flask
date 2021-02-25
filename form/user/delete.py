from wtforms import Form, HiddenField


class Delete(Form):
    id = HiddenField('ID')


