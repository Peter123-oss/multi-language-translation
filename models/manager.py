from config import db_init as db

class Manager(db.Model):
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(255), nullable=True, default=None)
    password = db.Column(db.String(255), nullable=True, default=None)
    managerName = db.Column(db.String(255), nullable=True, default=None)
    phoneNumber = db.Column(db.String(255), nullable=True, default=None)
    status = db.Column(db.String(255), nullable=True, default=None)
    gender = db.Column(db.String(255), nullable=True, default=None)

    def toDict(self):
        return {
            'id': self.id,
            'account': self.account,
            'password': self.password,
            'managerName': self.managerName,
            'phoneNumber': self.phoneNumber,
            'status': self.status,
            'gender': self.gender
        }
