from . import db

class propertyProfile(db.Model):
    __tablename__ = 'Property'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    num_bedroom = db.Column(db.Integer)
    num_bathroom = db.Column(db.Integer)
    location = db.Column(db.String(255))
    price = db.Column(db.Float)
    type = db.Column(db.String(80))
    description = db.Column(db.String(255))
    photo = db.Column(db.String(128), unique = True)
    
    
    def __init__(self, title, num_bedroom, num_bathroom, location, price, type, description, photo):
        self.title = title
        self.num_bedroom = num_bedroom
        self.num_bathroom = num_bathroom
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo
        
    def __repr__(self):
        return f"PropertyProfile(id={self.id}, title='{self.title}', num_bedroom='{self.num_bedroom}' num_bathroom={self.num_bathroom}, address='{self.location}', price={self.price}, type={self.type}, description={self.description}, photo={self.description})"