from models.manager import Manager
from models.user import User
from flask import jsonify
import random


def login(account, password):
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
    return jsonify({
            'code': 0,
            "message": "登录成功",
            "data": mDict
        })


def register(account, password, rePassword, vCode, phoneNumber, gender, status, userName):
    m = Manager.query.filter_by(account=account).first()
    if rePassword is not password:
        return jsonify({
            'code': -2,
            "message": "两次密码输入不一致",
            "data":""
        })
    if m is not None:
        return jsonify({
            'code': -1,
            "message": "用户名已存在",
            "data":""
        })
    newManager = Manager(account=account, password=password, userName=userName, phoneNumber=phoneNumber,
                   status='正常', gender=gender)
    Manager.session.add(newManager)
    Manager.session.commit()
    if not verifyCode(vCode, phoneNumber):
        return jsonify({
            'code': -3,
            "message": "验证码错误",
            "data":""
        })
    return jsonify({
        'code': 0,
        "message": "注册成功",
        "data": ""
    })


def revisePassword(account, password, rePassword, vCode, phoneNumber):
    m = Manager.query.filter_by(account=account).first()
    if m is None:
        return jsonify({
            'code': -1,
            "message": "用户不存在",
            "data": ""
        })
    if rePassword is not password:
        return jsonify({
            'code': -2,
            "message": "两次密码输入不一致",
            "data": ""
        })
    if not verifyCode(vCode, phoneNumber):
        return jsonify({
            'code': -3,
            "message": "验证码错误",
            "data": ""
        })
    m.password = password
    Manager.session.commit()
    return jsonify({
        'code': 0,
        "message": "密码修改成功",
        "data": ""
    })


def verifyCode(vCode, phoneNumber):
    ret = ""
    for i in range(6):
        num = random.randint(0, 9)  # 生成数字
        lowercase = chr(random.randint(97, 122))  # 生成小写字母
        capital = chr(random.randint(65, 90))  # 生成大写字母
        s = str(random.choice([num, lowercase, capital]))  # 随机挑选数字字母
        ret += s
    if vCode == ret:
        return True
    else:
        return False


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


