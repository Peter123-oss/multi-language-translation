from flask import Blueprint, request
from services.user import login, register, revisePassword
from services.DocTransService import uploadFile1, convertToText, extract_text, get_pdf_page_count
from flask import jsonify

doc = Blueprint('DocService', __name__)


@doc.route('/docUpload', methods=['POST'])
def uploadFile():
    data = request.args
    path = data.get('path')  # 使用 get 方法来避免 KeyError

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


    return doc_result




@doc.route('/docConvert', methods=['POST'])
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


