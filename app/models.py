from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """
    Класс для пользователей
    """
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(120), nullable=False)
    photo = db.Column(db.String(2000))
    about = db.Column(db.String(500), default='https://data.whicdn.com/images/239575122/original.jpg')

    def __repr__(self):
        return '<User {}, {}>'.format(self.login, self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Playlist(db.Model):
    """
    Класс для плейлистов
    """
    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    about = db.Column(db.String(240))
    cover = db.Column(db.String(), default="")
    user_id = db.Column(db.Integer, db.ForeignKey('users_data.id'))  # ссылается на пользователей из базы users_data
    name = db.Column(db.String(120), db.ForeignKey('users_data.name'))
    hashtags = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Playlist {}>'.format(self.body)
