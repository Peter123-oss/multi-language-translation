from flask import Blueprint, request
from services.manager import login, register, revisePassword, showUserList, showVIPUserList, changeStatus

manager = Blueprint('manager', __name__)

@manager.route('/loginUI', methods=['POST'])
def loginUI():
    data = request.args
    account = data['account']
    password = data['password']
    phoneNumber = data['phoneNumber']
#    vCode = data['vCode']
    data = login(account, password, phoneNumber)
    return data


@manager.route('/registerUI', methods=['POST'])
def registerUI():
    data = request.args
    account = data['account']
    password = data['password']
    rePassword = data['rePassword']
#    vCode = data['vCode']
    phoneNumber = data['phoneNumber']
    gender = data['gender']
    managerName = data['managerName']
    data = register(account, password, rePassword, phoneNumber, gender, managerName)
    return data


@manager.route('/revisePasswordUI', methods=['POST'])
def revisePasswordUI():
    data = request.args
    account = data['account']
    password = data['password']
    rePassword = data['rePassword']
    phoneNumber = data['phoneNumber']
    data = revisePassword(account, password, rePassword, phoneNumber)
    return data


@manager.route('/showUserListUI', methods=['POST'])
def showUserListUI():
    showUserList()


@manager.route('/showVIPUserListUI', methods=['POST'])
def showVIPUserListUI():
    showVIPUserList()


@manager.route('/accountManagementUI', methods=['POST'])
def accountManagementUI():
    am = request.args
    userID = am['userID']
    newStatus = am['status']
    data = changeStatus(userID, newStatus)
    return data


@manager.route('/vipAccountManagementUI', methods=['POST'])
def vipAccountManagementUI():
    vam = request.args
    vipUserID = vam['vipUserID']
    newStatus = vam['status']
    data = changeStatus(vipUserID, newStatus)
    return data


@manager.route('userFeedbackManagementUI', methods=['POST'])
def userFeedbackManagementUI():
    pass


@manager.route('/', methods=['POST'])
def mainWindowUI():
    data = request.args