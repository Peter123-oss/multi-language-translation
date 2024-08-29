from flask import Flask, request
from routes.user import user
from config import app

app.register_blueprint(user, url_prefix="/user")


@app.route('/')
def ping():
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
