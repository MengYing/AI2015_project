import random
from flask import *
from flask.ext.login import login_user, logout_user, \
    login_required, current_user
from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User
from ..util import *


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('auth/login.html', form=form)

    user = User.query.filter_by(email=form.email.data).first()
    if user is None or not user.verify_password(form.password.data):
        flash('Invalid username or password.')
        print "not pass"
        return render_template('auth/login.html', form=form)

    print "already pass"
    login_user(user, form.remember_me.data)
    sessionid = db.session.query(User.id).\
        filter_by(email=form.email.data).one()
    session.permanent = True
    session['id'] = sessionid
    return redirect(url_for('main.chat'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if not form.validate_on_submit():
        return render_template('auth/register.html', form=form)

    user = User(email=form.email.data,
                username=form.username.data,
                password=form.password.data,
                status=0)
    db.session.add(user)
    db.session.commit()
    flash('You can now login.')
    return redirect(url_for('auth.login'))

@auth.route('/testajax', methods=['GET', 'POST'])
def testajax():
    return jsonify({"str":"hahahaha"})
