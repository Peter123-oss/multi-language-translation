from config import db_init as db

class TransBySentenceHistory(db.Model):
    __tablename__ = 'transbysentence_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sentenceLink = db.Column(db.String(255), nullable=False, default=None)
    sentenceResult = db.Column(db.String(255), nullable=False, default=None)
    textInputID = db.Column(db.Integer, db.ForeignKey('textinput_history.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'userID': self.userID,
            'sentenceLink': self.sentenceLink,
            'sentenceResult': self.sentenceResult,
            'textInputID': self.textInputID
        }