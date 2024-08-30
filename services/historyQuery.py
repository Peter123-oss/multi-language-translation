from models.textinput_history import TextInputHistory
from models.transbyword_history import TransByWordHistory
from models.transbysentence_history import TransBySentenceHistory
from models.userfeedback_history import UserFeedbackHistory
from flask import jsonify

def querySenTrans():
    qsts = TransBySentenceHistory.query.filter_by(textInputID=0).all()
    if qsts is None:
        return jsonify({
            'code': -1,
            "message": "暂无语句翻译记录",
            "data": ""
        })
    qstDicts = [qst.toDict() for qst in qsts]
    return jsonify({
        'code': 0,
        "message": "语句翻译历史记录查询成功",
        "data": qstDicts
    })


def queryWordTrans():
    qwts = TransByWordHistory.query.all()
    if qwts is None:
        return jsonify({
            'code': -1,
            "message": "暂无单词翻译记录",
            "data": ""
        })
    qwtDicts = [qwt.toDict() for qwt in qwts]
    return jsonify({
        'code': 0,
        "message": "单词翻译历史记录查询成功",
        "data": qwtDicts
    })


def queryOCR():
    qOCRs = TransBySentenceHistory.query.filter(textInputID=2).all()
    if qOCRs is None:
        return jsonify({
            'code': -1,
            "message": "暂无语音翻译记录",
            "data": ""
        })
    qOCRDicts = [qOCR.toDict() for qOCR in qOCRs]
    qOCRInputs = TextInputHistory.query.filter(inputType=2).all()
    qOCRInputDicts = [qOCRInput.toDict() for qOCRInput in qOCRInputs]
    mergedDicts = []
    for inputDict in qOCRInputDicts:
        matchingQOCRDict = next((d for d in qOCRDicts if d["userID"] == inputDict["userID"]), None)
        if matchingQOCRDict is not None:
            mergedDict = {
                "userID": inputDict["userID"],
                "inputType": "语音",
                "inputPath": inputDict["inputPath"],
                "identifyResult": inputDict["identifyResult"],
                "sentenceResult": matchingQOCRDict["sentenceResult"]
            }
            mergedDicts.append(mergedDict)
    return jsonify({
        'code': 0,
        "message": "语音翻译历史记录查询成功",
        "data": mergedDicts
    })


def queryASW():
    qASWs = TransBySentenceHistory.query.filter(textInputID=1).all()
    if qASWs is None:
        return jsonify({
            'code': -1,
            "message": "暂无图片翻译记录",
            "data": ""
        })
    qASWDicts = [qASW.toDict() for qASW in qASWs]
    qASWInputs = TextInputHistory.query.filter(inputType=1).all()
    qASWInputDicts = [qASWInput.toDict() for qASWInput in qASWInputs]
    mergedDicts = []
    for inputDict in qASWInputDicts:
        matchingQASWDict = next((d for d in qASWDicts if d["userID"] == inputDict["userID"]), None)
        if matchingQASWDict is not None:
            mergedDict = {
                "userID": inputDict["userID"],
                "inputType": "图片",
                "inputPath": inputDict["inputPath"],
                "identifyResult": inputDict["identifyResult"],
                "sentenceResult": matchingQASWDict["sentenceResult"]
            }
            mergedDicts.append(mergedDict)
    return jsonify({
        'code': 0,
        "message": "图片翻译历史记录查询成功",
        "data": mergedDicts
    })


def queryDocTrans():
    qDocs = TransBySentenceHistory.query.filter(textInputID=3).all()
    if qDocs is None:
        return jsonify({
            'code': -1,
            "message": "暂无文档翻译记录",
            "data": ""
        })
    qDocDicts = [qDoc.toDict() for qDoc in qDocs]
    qDocInputs = TextInputHistory.query.filter(inputType=3).all()
    qDocInputDicts = [qDocInput.toDict() for qDocInput in qDocInputs]
    mergedDicts = []
    for inputDict in qDocInputDicts:
        matchingQDocDict = next((d for d in qDocDicts if d["userID"] == inputDict["userID"]), None)
        if matchingQDocDict is not None:
            mergedDict = {
                "userID": inputDict["userID"],
                "inputType": "文档",
                "inputPath": inputDict["inputPath"],
                "identifyResult": inputDict["identifyResult"],
                "sentenceResult": matchingQDocDict["sentenceResult"],
                "downloadURL": inputDict["downloadURL"]
            }
            mergedDicts.append(mergedDict)
    return jsonify({
        'code': 0,
        "message": "文档翻译历史记录查询成功",
        "data": mergedDicts
    })


def userFeedback():
    ufs = UserFeedbackHistory.query.all()
    if ufs is None:
        return jsonify({
            'code': -1,
            "message": "暂无用户反馈记录",
            "data": ""
        })
    ufsDicts = [uf.toDict() for uf in ufs]
    return jsonify({
        'code': 0,
        "message": "用户反馈记录查询成功",
        "data": ufsDicts
    })
