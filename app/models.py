from app import db


class User(db.Model):
    """
    Класс для пользователей
    """
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(120), nullable=False)
    photo = db.Column(db.String(2000))

    def __repr__(self):
        return '<User {}>'.format(self.login)


class Playlist(db.Model):
    """
    Класс для плейлистов
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    about = db.Column(db.String(140))
    cover = db.Column(db.String(), default="")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # ссылается на пользователей из базы users

    def __repr__(self):
        return '<Playlist {}>'.format(self.body)
