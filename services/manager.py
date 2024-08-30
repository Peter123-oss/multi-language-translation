from models.manager import Manager
from models.user import User
from services.verifyCode import verifyCode
from flask import jsonify
import random


def login(account, password, phoneNumber, vCode, veriCode):
    m = Manager.query.filter_by(account=account).first()
    if m is None:
        # 用户不存在
        return jsonify({
            'code': -1,
            "message": "用户不存在",
            "data":""
        })
    mDict = m.toDict()
    if mDict['password'] != password:
        # 用户存在 密码错误
        return jsonify({
            'code': -2,
            "message": "密码错误",
            "data":""
        })
    if mDict['phoneNumber'] != phoneNumber:
        return jsonify({
            'code': -3,
            "message": "手机号错误",
            "data":""
        })
    if veriCode != vCode:
        return jsonify({
            'code': -4,
            "message": "验证码错误",
            "data": ""
        })
    return jsonify({
            'code': 0,
            "message": "登录成功",
            "data": mDict
        })


def register(account, password, rePassword, phoneNumber, gender, managerName, vCode, veriCode):
    m = Manager.query.filter_by(account=account).first()
    if m is not None:
        return jsonify({
            'code': -1,
            "message": "用户名已存在",
            "data":""
        })
    if rePassword != password:
        return jsonify({
            'code': -2,
            "message": "两次密码输入不一致",
            "data":""
        })
    if veriCode != vCode:
        return jsonify({
            'code': -3,
            "message": "验证码错误",
            "data": ""
        })
    newManager = Manager(account=account, password=password, managerName=managerName, phoneNumber=phoneNumber,
                   status='正常', gender=gender)
    Manager.add(newManager)
    return jsonify({
        'code': 0,
        "message": "注册成功",
        "data": ""
    })


def revisePassword(account, newPassword, rePassword, phoneNumber, vCode, veriCode):
    m = Manager.query.filter_by(account=account).first()
    if m is None:
        return jsonify({
            'code': -1,
            "message": "用户不存在",
            "data": ""
        })
    if rePassword is not newPassword:
        return jsonify({
            'code': -2,
            "message": "两次密码输入不一致",
            "data": ""
        })
    mDict = m.toDict()
    if mDict['phoneNumber'] != phoneNumber:
        return jsonify({
            'code': -3,
            "message": "手机号错误",
            "data": ""
        })
    if vCode != veriCode:
        return jsonify({
            'code': -4,
            "message": "验证码错误",
            "data": ""
        })
    Manager.update(mDict['id'], newPassword)
    return jsonify({
        'code': 0,
        "message": "密码修改成功",
        "data": ""
    })


def veCode(phoneNumber):
    veriCode = verifyCode(phoneNumber)
    return jsonify({
        'code': 0,
        "message": "验证码发送成功",
        "data": veriCode
    })


def showUserList():
    users = User.query.filter(isVIP=False).all()
    for user in users:
        user = user.toDict()
        print(user)


def showVIPUserList():
    vipUsers = User.query.filter_by(isVIP=True).all()
    for vipUser in vipUsers:
        vipUser = vipUser.toDict()
        print(vipUser)


def changeStatus(userID, newStatus):
    User.changeStatus(userID, newStatus)
    return jsonify({
        'code': 0,
        "message": "状态更改成功",
        "data": ""
    })
