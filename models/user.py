from config import db_init as db

class User(db.Model):
    __tablename__ = 'user'  # 指定表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(255), nullable=True, default=None)
    password = db.Column(db.String(255), nullable=True, default=None)
    userName = db.Column(db.String(255), nullable=True, default=None)
    isVIP = db.Column(db.Boolean, nullable=True, default=False)
    phoneNumber = db.Column(db.String(255), nullable=True, default=None)
    status = db.Column(db.String(255), nullable=True, default=None)
    gender = db.Column(db.String(255), nullable=True, default=None)


    def toDict(self):
        return {
            'id': self.id,
            'account': self.account,
            'password': self.password,  # 注意：在实际应用中，出于安全考虑，不应该直接返回密码
            'userName': self.userName,
            'isVIP': self.isVIP,
            'phoneNumber': self.phoneNumber,
            'status': self.status,
            'gender': self.gender
        }


    def add(newUser):
        db.session.add(newUser)
        db.session.commit()


    def update(id, user):
        db.session.query(User).filter_by(id=id).update(user)
        db.session.commit()