from flask_blog_main.models import User, Post
from flask_blog_main.__init__ import db, password_checker
from flask_sqlalchemy import SQLAlchemy

User.__table__.create(db.session.bind)
Post.__table__.create(db.session.bind)
pw = input("Enter admin password:")
user1 = User(username='admin', email='admin@admin.com', password =password_checker.generate_password_hash(pw).decode('utf-8'), admin='admin')
db.session.add(user1)
db.session.commit()