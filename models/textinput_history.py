from config import db_init as db

class TextInputHistory(db.Model):
    __tablename__ = 'textinput_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    inputPath = db.Column(db.String(255), nullable=True, default=None)
    inputType = db.Column(db.Integer, nullable=True, default=None)
    identifyResult = db.Column(db.String(255), nullable=True, default=None)
    downloadURL = db.Column(db.String(255), nullable=True, default=None)

    def toDict(self):
        return {
            'id': self.id,
            'userID': self.userID,
            'inputPath': self.inputPath,
            'inputType': self.inputType,
            'identifyResult': self.identifyResult,
            'downloadURL': self.downloadURL
        }


    def add(newInput):
        db.session.add(newInput)
        db.session.commit()