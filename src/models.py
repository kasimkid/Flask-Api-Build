from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Favorite (db.Model):
    __tablename__ = 'favorite'
    favoriteID = db.Column(db.Integer, primary_key=True)
    characterID = db.Column(db.Integer, db.ForeignKey('character.characterID'))
    nicknameID = db.Column(db.Integer, db.ForeignKey('register.registerID'))

class Register (db.Model):
    __tablename__ = 'register'
    registerID = db.Column(db.Integer,primary_key=True) 
    name = db.Column(db.tring(50),nullable=False)
    password = db.Column(db.String(12),nullable=False)
    email = db.Column(db.String(50), nullable=True, unique=True)
    register = db.relationship('Favorite')

    def serialize(self):
        return {
            "id": self.registerID,
            "name": self.name,
            "mail": self.email
        }
    
class Character(db.Model):
    __tablename__ = 'character'
    characterID = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    status = db.Column(db.String(50),nullable=False)
    episode = db.Column(db.String(50),nullable=False)
    location = db.Column(db.String(50),nullable=False)
    favoriteID = db.relationship('Favorite')
    Dimension = db.relationship ('Dimension')

    def serialize(self):
        return {
            "id": self.characterID,
            "name": self.name,
            "status":self.status,
            "episode": self.episode,
            "location":self.location
        }

class Episode(db.Model):
    __tablename__ = 'episode'
    episodeID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    episode = db.Column(db.String(700),nullable=False)
    character = db.Column(db.Integer, db.ForeignKey('character.characterID'))
    favoriteID = db.relationship('Favorite')

    def serialize(self):
        return {
            "id": self.episodeID,
            "name": self.name,
            "episode": self.episode,
            "character":self.character
        }
    
class Dimension (db.Model):
    __tablename__ = 'dimension'
    dimensionID = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(50),nullable=False)
    favoriteID = db.relationship('Favorite')

    def serialize(self):
        return{
            "id":self.dimensionID,
            "character":self.character
        }
##================================================================##
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }