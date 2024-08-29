from models.transbysentence_history import TransBySentenceHistory
from flask import jsonify

#语句翻译
def translate(userID, sentence, textInputID, sentenceLink):
    #result = translate(sentence)
    result = ""
    TransBySentenceHistory.add(TransBySentenceHistory(userID=userID, sentenceLink=sentenceLink, sentenceResult=result, textInputID=textInputID))
    return jsonify({
        'code': 0,
        "message": "翻译完成",
        "data": result
    })