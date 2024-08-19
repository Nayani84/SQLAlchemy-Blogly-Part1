"""Seed file to make sample data for blogly db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
spider_man = User(
    first_name="Peter", 
    last_name="Parker", 
    image_url="https://siyahfilmizle.pro/wp-content/uploads/2021/06/Inanilmaz-Orumcek-Adam-2-The-Amazing-Spiderman-2-izle.jpg"
    )
superman = User(
    first_name="Clark",
    last_name="Kent",
    image_url="https://upload.wikimedia.org/wikipedia/en/d/d6/Superman_Man_of_Steel.jpg"
)
batman = User(
    first_name="Bruce",
    last_name="Wayne",
    image_url="https://www.hollywoodreporter.com/wp-content/uploads/2024/05/CAPC_S1_FG_104_00184209_Still300-H-2024.jpg?w=1296&h=730&crop=1"
)
ant_man = User(
    first_name="Scott",
    last_name="Lang",
    image_url="https://tamashiiweb.com/images/item/item_0000014317_qWyNyjX7_01.jpg"
)
wonder_woman = User(
    first_name="Princess",
    last_name="Diana",
    image_url="https://m.media-amazon.com/images/M/MV5BMTYzODQzYjQtNTczNC00MzZhLTg1ZWYtZDUxYmQ3ZTY4NzA1XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg"
)


# Add new objects to session, so they'll persist
db.session.add(spider_man)
db.session.add(superman)
db.session.add(batman)
db.session.add(ant_man)
db.session.add(wonder_woman)

# Commit--otherwise, this never gets saved!
db.session.commit()
