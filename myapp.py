from flask import Flask, request
from routes.user import user
from routes.manager import manager
from routes.vipActivation import vipActivation
from routes.ASWServiceRoute import asw
from routes.OCRServiceRoute import ocr
from routes.transByWord import transByWord
from routes.transBySentence import transBySentence
from routes.historyQuery import historyQuery

from config import app

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(manager, url_prefix="/manager")
app.register_blueprint(vipActivation, url_prefix="/vipActivation")
app.register_blueprint(asw, url_prefix="/aswService")
app.register_blueprint(ocr, url_prefix="/ocrService")
app.register_blueprint(transByWord, url_prefix="/transByWord")
app.register_blueprint(transBySentence, url_prefix="/transBySentence")
app.register_blueprint(historyQuery, url_prefix="/historyQuery")

@app.route('/')
def ping():
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
