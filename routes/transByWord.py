from flask import Blueprint, request
from services.transByWord import offlineTrans

transByWord = Blueprint('transByWord', __name__)

@transByWord.route('/offlineTransUI', methods=['POST'])
def offlineTransUI():
    olt = request.args
    word = olt['word']
    sourceLanguage = olt['sourceLanguage']
    targetLanguage = olt['targetLanguage']
    userID = olt['userID']
    result = offlineTrans(word, sourceLanguage, targetLanguage, userID)
    return result


@transByWord.route('/onlineTransUI', methods=['POST'])
def onlineTransUI():
    pass