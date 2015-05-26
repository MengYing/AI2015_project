import random
from sqlalchemy import func
from . import db
from models import *


def get_shuffled_id():
    print Pictures.query.count()
    num = db.session.query(func.max(Pictures.id))[0][0]
    print num
    # num = 10000
    piclist = [str(i+1) for i in range(num)]
    random.shuffle(piclist)
    # print piclist
    return ','.join(piclist)

'''
def getpic(userid):
    user = User.query.filter_by(id=userid)[0]
    pool = str(user.picturepool).split(',')
    try:
        newidx = int(pool.pop(0))
        user.picturepool = ','.join(pool)
    except ValueError:
        return None
    # db.session.commit()
    # print 'the first is', newidx
    try:
        nextpic = Pictures.query.filter_by(id=newidx)[0].pic
        return nextpic
    except IndexError:
        return getpic(userid)
'''
def getpic(userid):
    user = User.query.filter_by(id=userid)[0]
    progress = user.progress
    start = user.start
    total = user.total
    picNum = (progress+start) % 800+1
    # print "progress:"+str(progress)+" start:"+str(start)+" total:"+str(total)+" picNum:"+str(picNum)
    # if progress % 100 == 0:
        # user.question += 1
    if progress < total:
        nextpic = Pictures.query.filter_by(id=picNum)[0].pic
        # print "nextpic:"+str(nextpic)
        quesNum = progress / 100 + 1
        question = Questions.query.filter_by(id=quesNum)[0].statement
        return nextpic, progress+1, total, question
    else:
        return None, None, None, None

if __name__ == '__main__':
    for i in range(50):
        print getpic()
