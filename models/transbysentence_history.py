from config import db_init as db

class TransBySentenceHistory(db.Model):
    __tablename__ = 'transbysentence_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    sentenceLink = db.Column(db.String(255), nullable=True, default=None)
    sentenceResult = db.Column(db.String(255), nullable=True, default=None)
    textInputID = db.Column(db.Integer, db.ForeignKey('textinput_history.id'), nullable=True)

    def toDict(self):
        return {
            'id': self.id,
            'userID': self.userID,
            'sentenceLink': self.sentenceLink,
            'sentenceResult': self.sentenceResult,
            'textInputID': self.textInputID
        }


    def add(newHistory):
        db.session.add(newHistory)
        db.session.commit()