from config import db_init as db

class Dictionary(db.Model):
    __tablename__ = 'dictionary'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    en = db.Column(db.String(255), nullable=True, default=None)
    zh = db.Column(db.String(255), nullable=True, default=None)
    fr = db.Column(db.String(255), nullable=True, default=None)

    def toDict(self):
        return {
            'id': self.id,
            'en': self.en,
            'zh': self.zh,
            'fr': self.fr
        }


    def add(newWord):
        db.session.add(newWord)
        db.session.commit()


    def update(id, newParaphrase, language):
        d = db.session.query(Dictionary).filter_by(id=id).first()
        if language == 'en':
            d.en = newParaphrase
        if language == 'zh':
            d.zh = newParaphrase
        if language == 'fr':
            d.fr = newParaphrase
        db.session.commit()