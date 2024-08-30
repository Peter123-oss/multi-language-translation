from config import db_init as db

class Dictionary(db.Model):
    __tablename__ = 'dictionary'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    en = db.Column(db.String(255), nullable=True, default=None)
    zh = db.Column(db.String(255), nullable=True, default=None)
    fr = db.Column(db.String(255), nullable=True, default=None)

    def to_dict(self):
        return {
            'id': self.id,
            'en': self.en,
            'zh': self.zh,
            'fr': self.fr
        }