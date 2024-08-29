from flask import Blueprint, request
from services.transBySentence import translate
from services.OCRService import uploadFile1, convertToText, extract_text
from models.textinput_history import TextInputHistory
from flask import jsonify

ocr = Blueprint('ocrService', __name__)


@ocr.route('/ocrUpload', methods=['POST'])
def uploadFile():
    data = request.args
    path = data.get('path')  # 使用 get 方法来避免 KeyError
    userID = data.get('userID')

    if not path:
        return jsonify({"code": -1, "message": "路径缺失"})

    # 调用 uploadFile1 获取文件的 base64 编码
    upload_result = uploadFile1(path)

    if upload_result["code"] != 0:
        # 如果上传失败，直接返回失败信息
        return jsonify(upload_result)

    # 如果上传成功，继续调用 OCR 服务
    image_text = upload_result["data"]
    ocr_result = convertToText(image_text)

    if ocr_result["code"] != 0:
        # 如果上传失败，直接返回失败信息
        return jsonify(ocr_result)

    full_text=extract_text(ocr_result)

    TextInputHistory.add(TextInputHistory(inputPath=path, inputType=2, identifyResult=full_text, userID=userID))

    return full_text




@ocr.route('/ocrTranslate', methods=['POST'])
def ocrTranslate():
    data = request.args
    path = data.get('path')
    userID = data.get('userID')
    identifyResult = data.get('identifyResult')
    data = translate(userID, identifyResult, 2, path)
    return data