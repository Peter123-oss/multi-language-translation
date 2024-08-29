from flask import Blueprint, request
from services.vipActivation import payForVIP

vipActivation = Blueprint('vipActivation', __name__)


@vipActivation.route('/payForVIPUI', methods=['POST'])
def payForVIPUI():
    pfv = request.args
    userID = pfv['userID']
    data = payForVIP(userID)
    return data
