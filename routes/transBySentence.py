from flask import Blueprint, request
from services.transBySentence import translate

transBySentence = Blueprint('transBySentence', __name__)

@transBySentence.route('/translateUI', methods=['POST'])
def translateUI():
    i = request.args
    userID = i['userID']
    sentence = i['sentence']
    data = translate(userID, sentence, 0, sentence)
    return data