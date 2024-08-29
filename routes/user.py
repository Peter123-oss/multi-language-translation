from flask import Blueprint, request
from services.user import login, register, revisePassword

user = Blueprint('user', __name__)

@user.route('/loginUI', methods=['POST'])
def loginUI():
    data = request.args
    account = data['account']
    password = data['password']
    phoneNumber = data['phoneNumber']
#    vCode = data['vCode']
    data = login(account, password, phoneNumber)
    return data


@user.route('/registerUI', methods=['POST'])
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


@user.route('/revisePasswordUI', methods=['POST'])
def revisePasswordUI():
    data = request.args
    account = data['account']
    password = data['password']
    rePassword = data['rePassword']
    phoneNumber = data['phoneNumber']
    data = revisePassword(account, password, rePassword, phoneNumber)
    return data


@user.route('/verifyCode', methods=['POST'])
def verifyCode():
    data = request.args
    vCode = data['vCode']


@user.route('/', methods=['POST'])
def mainWindowUI():
    data = request.args