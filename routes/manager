from flask import Blueprint, request
from services.historyQuery import queryOCR, queryASW, queryWordTrans, queryDocTrans, querySenTrans, userFeedback

historyQuery = Blueprint('historyQuery', __name__)

@historyQuery.route('/querySenTransUI', methods=['POST'])
def querySenTransUI():
    return querySenTrans()


@historyQuery.route('/queryOCRUI', methods=['POST'])
def queryOCRUI():
    return queryOCR()


@historyQuery.route('/queryASWUI', methods=['POST'])
def queryASWUI():
    return queryASW()


@historyQuery.route('/queryWordTransUI', methods=['POST'])
def queryWordTransUI():
    return queryWordTrans()


@historyQuery.route('/queryDocTransUI', methods=['POST'])
def queryDocTransUI():
    return queryDocTrans()


@historyQuery.route('/userFeedbackUI', methods=['POST'])
def userFeedbackUI():
    return userFeedback()
