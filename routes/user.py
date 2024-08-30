from flask import Blueprint, request
from services.user import login, register, revisePassword, veCode

user = Blueprint('user', __name__)

@user.route('/loginUI', methods=['POST'])
def loginUI():
    data = request.args
    account = data['account']
    password = data['password']
    phoneNumber = data['phoneNumber']
    vCode = data['vCode']
    veriCode = data['veriCode']
    data = login(account, password, phoneNumber, vCode, veriCode)
    return data


@user.route('/registerUI', methods=['POST'])
def registerUI():
    data = request.args
    account = data['account']
    password = data['password']
    rePassword = data['rePassword']
    vCode = data['vCode']
    phoneNumber = data['phoneNumber']
    gender = data['gender']
    userName = data['userName']
    veriCode = data['veriCode']
    data = register(account, password, rePassword, phoneNumber, gender, userName, vCode, veriCode)
    return data


@user.route('/revisePasswordUI', methods=['POST'])
def revisePasswordUI():
    data = request.args
    account = data['account']
    password = data['password']
    rePassword = data['rePassword']
    veriCode = data['verifyCode']
    vCode = data['vCode']
    phoneNumber = data['phoneNumber']
    data = revisePassword(account, password, rePassword, phoneNumber, vCode, veriCode)
    return data


@user.route('/verifyCodeUI', methods=['POST'])
def verifyCodeUI():
    data = request.args
    phoneNumber = data['phoneNumber']
    data = veCode(phoneNumber)
    return data


@user.route('/', methods=['POST'])
def mainWindowUI():
    data = request.args
