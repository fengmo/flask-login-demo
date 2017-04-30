# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms.fields.html5 import EmailField
from ..models import User

class LoginForm(FlaskForm):
    username = StringField(u'用户', validators=[DataRequired(), Length(5, 15), Regexp('[A-Za-z][A-Za-z0-9_]*$')])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(8, 30)])
    rememer_me = BooleanField(u'记住我')
    submit = SubmitField(u'提交')

class RegisterForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired(), Length(5, 15), Regexp('[A-Za-z][A-Za-z0-9_]*$')])
    password_one = PasswordField(u'密 码', validators=[DataRequired(), Length(8, 30), 
			EqualTo('password_two', message=u'你输入的密码不正确')])
    password_two = PasswordField(u'确认密码', validators=[DataRequired(), Length(8, 30)])
    email = EmailField(u'邮箱', validators=[DataRequired(), Length(5, 30)])
    submit = SubmitField(u'提交')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已存在')

class ChangepwForm(FlaskForm):
    password_old = PasswordField(u'原密码', validators=[DataRequired(), Length(8, 30)])
    password_one = PasswordField(u'新密码', validators=[DataRequired(), Length(8, 30), EqualTo('password_two', message=u'你输入的密码不正确')])
    password_two = PasswordField(u'确认密码', validators=[DataRequired(), Length(8, 30)])
    submit = SubmitField(u'提交')
