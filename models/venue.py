from app import db
from genre import venue_genre_table

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    genres=db.relationship('Genre', secondary=venue_genre_table, backref=db.backref('venues'))

    web_url=db.Column(db.String(120))
    seeking_talent=db.Column(db.Boolean, default=False)
    talent_description=db.Column(db.String(240))

    shows=db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self):
        return f'<Venue {self.id} {self.name}>'