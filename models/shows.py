from app import db
from datetime import datetime

class Show(db.Model):
    __tablename__ ='Show'

    id=db.Column(db.Integer, primary_key=True)
    show_time=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)    
    artist_id=db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)   
    venue_id=db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)

    def __repr__(self):
        return f'<Show {self.id} {self.show_time} artist-id={self.artist_id} venue-id={self.venue_id}>'