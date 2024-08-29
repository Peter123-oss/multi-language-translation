from config import db_init as db

class UserFeedbackHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False, default=None)
    content = db.Column(db.LongText, nullable=False, default=None)
    date = db.Column(db.Date, nullable=False, default=None)
    feedbackType = db.Column(db.Integer, nullable=False, default=None)

    def to_dict(self):
        return {
            'id': self.id,
            'userID': self.userID,
            'title': self.title,
            'content': self.content,
            'date': self.date,
            'feedbackType': self.feedbackType,
        }