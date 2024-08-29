from models.dictionary import Dictionary
from flask import jsonify

from models.transbyword_history import TransByWordHistory


def onlineTrans():
    pass


def offlineTrans(word, sourceLanguage, targetLanguage, userID):
    if word is None:
        return jsonify({
            'code': -1,
            "message": "未输入单词",
            "data": ""
        })
    if sourceLanguage is None:
        return jsonify({
            'code': -2,
            "message": "未输入单词语言",
            "data": ""
        })
    if targetLanguage is None:
        return jsonify({
            'code': -3,
            "message": "未输入翻译语言",
            "data": ""
        })
    if sourceLanguage == 'en':
        ws = Dictionary.query.filter_by(en=word).all()
        wf = Dictionary.query.filter_by(en=word).first().toDict()
        if targetLanguage == 'zh':
            addToHistory(userID, word, 'en', 'zh', wf['zh'], wf['id'])
            return jsonify({
                'code': 0,
                "message": "英转中查询成功",
                "data": [w.toDict()['zh'] for w in ws]
            })
        else :
            addToHistory(userID, word, 'en', 'fr', wf['fr'], wf['id'])
            return jsonify({
                'code': 1,
                "message": "英转法查询成功",
                "data": [w.toDict()['fr'] for w in ws]
            })
    if sourceLanguage == 'zh':
        ws = Dictionary.query.filter_by(zh=word).all()
        wf = Dictionary.query.filter_by(zh=word).first().toDict()
        if targetLanguage == 'en':
            addToHistory(userID, word, 'zh', 'en', wf['en'], wf['id'])
            return jsonify({
                'code': 2,
                "message": "中转英查询成功",
                "data": [w.toDict()['en'] for w in ws]
            })
        else :
            addToHistory(userID, word, 'zh', 'fr', wf['fr'], wf['id'])
            return jsonify({
                'code': 3,
                "message": "中转法查询成功",
                "data": [w.toDict()['fr'] for w in ws]
            })
    if sourceLanguage == 'fr':
        ws = Dictionary.query.filter_by(fr=word).all()
        wf = Dictionary.query.filter_by(fr=word).first().toDict()
        if targetLanguage == 'en':
            addToHistory(userID, word, 'fr', 'en', wf['en'], wf['id'])
            return jsonify({
                'code': 4,
                "message": "法转英查询成功",
                "data": [w.toDict()['en'] for w in ws]
            })
        else :
            addToHistory(userID, word, 'fr', 'zh', wf['zh'], wf['id'])
            return jsonify({
                'code': 5,
                "message": "法转中查询成功",
                "data": [w.toDict()['zh'] for w in ws]
            })


def addToHistory(userID, word, sourceLanguage, targetLanguage, result, dicID):
    TransByWordHistory.add(TransByWordHistory(userID=userID, wordContent=word, sourceLanguage=sourceLanguage,
                                              targetLanguage=targetLanguage, wordResult=result, dicID=dicID))