from models.user import User
from flask import jsonify

def payForVIP(userID):
    User.turnVIP(userID)
    return jsonify({
        'code': 0,
        "message": "支付成功",
        "data": ""
    })