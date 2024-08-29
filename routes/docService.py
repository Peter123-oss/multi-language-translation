from flask import Blueprint, request
from models.textinput_history import TextInputHistory
from services.transBySentence import translate
from services.docTransService import uploadFile1, convertToText, extract_text, get_pdf_page_count
from flask import jsonify

doc = Blueprint('docService', __name__)


@doc.route('/docUpload', methods=['POST'])
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

    # 如果上传成功，继续调用 Doc 服务
    pdf_text = upload_result["data"]
    count=get_pdf_page_count(path)
    doc_result = convertToText(pdf_text,page_count=count)

    if doc_result["code"] != 0:
        # 如果上传失败，直接返回失败信息
        return jsonify(doc_result)

    TextInputHistory.add(TextInputHistory(inputPath=path, inputType=3, identifyResult=doc_result, userID=userID))

    return doc_result




@doc.route('/docTranslate', methods=['POST'])
def docTranslate():
    data = request.args
    path = data.get('path')
    userID = data.get('userID')
    identifyResult = data.get('identifyResult')
    data = translate(userID, identifyResult, 3, path)
    return data

