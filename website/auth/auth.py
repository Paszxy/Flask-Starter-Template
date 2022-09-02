from flask import Blueprint, render_template, flash, redirect, url_for
from website.models import User
from flask_login import login_required, current_user, login_user, logout_user
from website import db
from werkzeug.security import check_password_hash, generate_password_hash
from website.forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login erfolgreich', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', category='error')
    return render_template("auth/login.html", form=form, user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Username already exists', category='error')
        elif form.password.data != form.confirm_password.data:
            flash('Password don\'t match', category='error')
        else:
            new_user = User(username=form.username.data, password=generate_password_hash(form.password.data, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=False)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    return render_template("auth/register.html", form=form, user=current_user)

@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    pass