from models.user import User
from flask import jsonify
import random

def login(account, password, phoneNumber):
    u = User.query.filter_by(account=account).first()
    if u is None:
        # 用户不存在
        return jsonify({
            'code': -1,
            "message": "用户不存在",
            "data":""
        })
    uDict = u.toDict()
    if uDict['password'] != password:
        # 用户存在 密码错误
        return jsonify({
            'code': -2,
            "message": "密码错误",
            "data":""
        })
    if uDict['phoneNumber'] != phoneNumber:
        return jsonify({
            'code': -3,
            "message": "手机号错误",
            "data":""
        })
    if not verifyCode(phoneNumber):
        return jsonify({
            'code': -4,
            "message":"验证码错误",
            "data":""
        })
    return jsonify({
            'code': 0,
            "message": "登录成功",
            "data": uDict
        })


def register(account, password, rePassword, phoneNumber, gender, userName):
    u = User.query.filter_by(account=account).first()
    if u is not None:
        return jsonify({
            'code': -1,
            "message": "用户名已存在",
            "data":""
        })
    if password != rePassword:
        return jsonify({
            'code': -2,
            "message": "两次密码输入不一致",
            "data":""
        })
    if not verifyCode(phoneNumber):
        return jsonify({
            'code': -3,
            "message": "验证码错误",
            "data":""
        })
    newUser = User(account=account, password=password, userName=userName, isVIP=False, phoneNumber=phoneNumber,
                   status='正常', gender=gender)
    User.add(newUser)
    return jsonify({
        'code': 0,
        "message": "注册成功",
        "data":""
    })


def revisePassword(account, newPassword, rePassword, phoneNumber):
    u = User.query.filter_by(account=account).first()
    if u is None:
        return jsonify({
            'code': -1,
            "message": "用户不存在",
            "data":""
        })
    if newPassword != rePassword:
        return jsonify({
            'code': -2,
            "message": "两次密码输入不一致",
            "data":""
        })
    uDict = u.toDict()
    if uDict['phoneNumber'] != phoneNumber:
        return jsonify({
            'code': -3,
            "message": "手机号错误",
            "data":""
        })
    if not verifyCode(phoneNumber):
        return jsonify({
            'code': -4,
            "message": "验证码错误",
            "data":""
        })
    User.update(uDict['id'], newPassword)
    return jsonify({
        'code': 0,
        "message": "密码修改成功",
        "data": ""
    })


def verifyCode(phoneNumber):
    ret = ""
    for i in range(6):
        num = random.randint(0, 9)  # 生成数字
        lowercase = chr(random.randint(97, 122))  # 生成小写字母
        capital = chr(random.randint(65, 90))  # 生成大写字母
        s = str(random.choice([num, lowercase, capital]))  # 随机挑选数字字母
        ret += s
    vCode = 123456
    if ret == ret:
        return True
    else:
        return False


def isVIP(account):
    uDict = User.query.filter_by(account=account).first().toDict()
    if uDict["isVIP"] == '1':
        return True
    else:
        return False