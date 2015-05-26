from flask import render_template, session
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    session.clear()
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    session.clear()
    return render_template('500.html'), 500
