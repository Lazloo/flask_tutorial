from app import db
from datetime import datetime

# The User class created above inherits from db.Model, a base class for all models from Flask-SQLAlchemy. This class
# defines several fields as class variables. Fields are created as instances of the db.Column class, which takes the
# field type as an argument, plus other optional arguments that, for example, allow me to indicate which fields are
# unique and indexed, which is important so that database searches are efficient.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # -> Use the author argument to assign the posts to the foreign key dfined in the class Post
    # e.g.
    # >>> u = User.query.get(1)
    # >>> p = Post(body='my first post!', author=u)
    # >>> db.session.add(p)
    # >>> db.session.commit()
    # This will a the post 'my first post!' to the table POSt and fill the user_id with given User.id
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging.
    def __repr__(self):
        return '<User {}>'.format(self.username)


# The new Post class will represent blog posts written by users. The timestamp field is going to be indexed,
# which is useful if you want to retrieve posts in chronological order. I have also added a default argument,
# and passed the datetime.utcnow function. When you pass a function as a default, SQLAlchemy will set the field to
# the value of calling that function (note that I did not include the () after utcnow, so I'm passing the function
# itself, and not the result of calling it). In general, you will want to work with UTC dates and times in a server
# application. This ensures that you are using uniform timestamps regardless of where the users are located. These
# timestamps will be converted to the user's local time when they are displayed.
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)