from flask import Blueprint, request

from services.ASWService import uploadFiles, extract_recognized_text
from services.user import login, register, revisePassword
from services.OCRService import uploadFile1, convertToText
from flask import jsonify

asw = Blueprint('ASWService', __name__)


@asw.route('/aswUpload', methods=['POST'])
def uploadFile():
    data = request.args
    path = data.get('path')  # 使用 get 方法来避免 KeyError

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


    return jsonify({
        "code":0,
        "message":"转换成功",
        "data":voice_text
    })


@asw.route('/ocrConvert', methods=['POST'])
def registerUI():
    data = request.args
    account = data['account']
    password = data['password']
    rePassword = data['rePassword']
#    vCode = data['vCode']
    phoneNumber = data['phoneNumber']
    gender = data['gender']
    userName = data['userName']
    data = register(account, password, rePassword, phoneNumber, gender, userName)
    return data


