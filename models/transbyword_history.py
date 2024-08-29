from config import db_init as db

class TransByWordHistory(db.Model):
    __tablename__ = 'transbyword_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    wordContent = db.Column(db.String(255), nullable=False, default=None)
    sourceLanguage = db.Column(db.String(255), nullable=False, default=None)
    targetLanguage = db.Column(db.String(255), nullable=False, default=None)
    wordResult = db.Column(db.String(255), nullable=False, default=None)
    dicID = db.Column(db.Integer, db.ForeignKey('dictionary.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'userID': self.userID,
            'wordContent': self.wordContent,
            'sourceLanguage': self.sourceLanguage,
            'targetLanguage': self.targetLanguage,
            'wordResult': self.wordResult,
            'dicID': self.dicID,
        }