from flask import *
import random
from datetime import datetime
from . import main
from ..auth.forms import LoginForm
from .. import db
from ..models import User
from ..util import *


@main.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('auth.login'))


@main.route('/label', methods=['GET'])
def label():
    print "enter main.label"
    try:
        print "enter main.label try"
        print session.get('id')
        print getpic(session.get('id'))
        pic, idx, ttl, ques = getpic(session.get('id'))
    except IndexError:
        session.clear()
        form = LoginForm()
        print "enter main.label - except"
        return redirect(url_for('auth.login'))

    if pic is None:
        session.clear()
        return render_template('end.html')
    print 'start by', pic
    
    userid = session.get('id')[0]
    user = User.query.filter_by(id=userid)[0]
    quesNum = user.progress / 100 + 1
    question = Questions.query.filter_by(id=quesNum)[0].statement
    return render_template('label.html', pic=pic, idx=idx, ttl=ttl, question=question)


@main.route('/newpic', methods=['GET'])
def newpic():
    pic, idx, ttl, ques = getpic(session.get('id'))
    if pic is None:
        return render_template('end.html')
    print 'new', pic, '##', ques
    return jsonify({'pic': pic, 'idx': idx, 'ttl': ttl, 'ques': ques})


@main.route('/record/<pictureNum>/<duration>/<answer>', methods=['POST'])
def data(pictureNum, duration, answer):
    # session['id'] = random.randint(0, 50)
    print type(pictureNum), len(pictureNum)
    if len(pictureNum) < 13:
        print 'enter here'
        return render_template('end.html')

    now = datetime.now()
    labelTime = now.strftime("%Y%m%d-%H%M")
    
    userid = session.get('id')[0]
    user = User.query.filter_by(id=userid)[0]
    question = user.progress / 100 + 1
    user.progress += 1
    data = Data(labelTime=labelTime, question=question,
                pictureNum=pictureNum, userid=userid, duration=duration, answer=answer)
    db.session.add(data)
    db.session.commit()

    return redirect(url_for('main.newpic'))

@main.route('/testpage', methods=['GET'])
def testpage():
    return render_template('auth/test.html')

@main.route('/chat', methods=['GET'])
def chat():
    return render_template('index.html')
