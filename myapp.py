from urllib.parse import urlencode

from flask import Flask, request

from routes.ASWServiceRoute import asw
from routes.DocTransServiceRoute import doc
from routes.OCRServiceRoute import ocr
from routes.user import user
from config import app

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(ocr , url_prefix="/OCRService")
app.register_blueprint(asw , url_prefix="/ASWService")
app.register_blueprint(doc,url_prefix="/DocService")

@app.route('/')
def ping():
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
