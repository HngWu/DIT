from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields import EmailField


class CreateUserForm(Form):
    name = StringField(
        "Name", [validators.Length(min=1, max=150), validators.DataRequired()]
    )
    email = EmailField("Email", [validators.Email(), validators.DataRequired()])
    subject = StringField(
        "Subject", [validators.Length(min=1, max=150), validators.DataRequired()]
    )
    remarks = TextAreaField("Remarks", [validators.Optional()])
