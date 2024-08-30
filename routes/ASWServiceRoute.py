from flask import Blueprint, request
from models.textinput_history import TextInputHistory
from services.transBySentence import translate
from services.ASWService import uploadFiles, extract_recognized_text
from flask import jsonify

asw = Blueprint('aswService', __name__)


@asw.route('/aswUpload', methods=['POST'])
def uploadFile():
    data = request.args
    path = data.get('path')  # 使用 get 方法来避免 KeyError
    userID = data.get('userID')

    if not path:
        return jsonify({"code": -1, "message": "路径缺失"})

    # 调用 uploadFile1 获取文件的 base64 编码
    upload_result = uploadFiles(path)

    if upload_result["code"] != 0:
        # 如果上传失败，直接返回失败信息
        return jsonify(upload_result)

    # 如果上传成功，继续调用 OCR 服务
    voice_json = upload_result["data"]
    voice_text=extract_recognized_text(voice_json)

    TextInputHistory.add(TextInputHistory(inputPath=path, inputType=1, identifyResult=voice_text, userID=userID))

    return jsonify({
        "code":0,
        "message":"转换成功",
        "data":voice_text
    })


@asw.route('/aswtranslate', methods=['POST'])
def aswtranslate():
    data = request.args
    path = data.get('path')
    userID = data.get('userID')
    identifyResult = data.get('identifyResult')
    data = translate(userID, identifyResult, 1, path)
    return data
