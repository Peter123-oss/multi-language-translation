from models.textinput_history import TextInputHistory
from models.transbyword_history import TransByWordHistory
from models.transbysentence_history import TransBySentenceHistory
from models.userfeedback_history import UserFeedbackHistory
from flask import jsonify

def querySenTrans():
    qsts = TransBySentenceHistory.query.all()
    return qsts


def queryWordTrans():
    qwts = TransByWordHistory.query.all()
    for qwt in qwts:
        qwtDict = qwt.toDict()
        print(qwtDict)


def queryOCR():
    qOCRs = TransBySentenceHistory.query.filter(textInputID=2).all()
    return qOCRs


def queryASW():
    qASWs = TransBySentenceHistory.query.filter(textInputID=1).all()
    for qASW in qASWs:
        qASWDict = qASW.toDict()
        print(qASWDict)


def queryDocTrans():
    qDocs = TransBySentenceHistory.query.filter(textInputID=3).all()
    for qDoc in qDocs:
        qDocDict = qDoc.toDict()
        print(qDocDict)


def userFeedback():
    ufs = UserFeedbackHistory.query.all()
    for uf in ufs:
        ufDict = uf.toDict()
        print(ufDict)