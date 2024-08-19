from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = 'https://cdn-icons-png.flaticon.com/512/10453/10453654.png'

"""Models for Blogly."""
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    image_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)



    def __repr__(self):
        u = self
        return f"<user id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"
    
  