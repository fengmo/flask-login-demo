# coding: utf-8
from . import auth
from .. import db
from ..models import User
from ..mail import send_mail
from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from forms import LoginForm, RegisterForm, ChangepwForm

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(u'登陆失败，用户名或密码错误，请重新登陆。')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
	user = User.query.filter_by(username=form.username.data).first()
	email = User.query.filter_by(email=form.email.data).first()
	if user is None and email is None:
	    user = User(
		username = form.username.data, 
		password = form.password_one.data, 
		email = form.email.data)
	    db.session.add(user)
	    db.session.commit()
            token = user.generate_confirmation_token()
	    send_mail(user.email, u'欢迎注册成为本博客用户', 'mail/confirm', user=user, token=token)
	    return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
	return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirm your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))

@auth.route('/changepw', methods = ['GET', 'POST'])
@login_required
def changepw():
    form = ChangepwForm()
    if form.validate_on_submit():
	password_old = current_user.verify_password(form.password_old.data)
	if password_old:
	    current_user.password = form.password_one.data
	    db.session.commit()
	    return redirect(url_for('main.index'))
	flash(u'修改密码失败，原密码不对')
    return render_template('auth/changepw.html', form=form)
