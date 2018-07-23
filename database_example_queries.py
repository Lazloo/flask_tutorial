# http://flask-sqlalchemy.pocoo.org/2.3/

from app import db
from app.models import User, Post

# Add Users
u = User(username='john', email='john@example.com')
db.session.add(u)
u = User(username='susan', email='susan@example.com')
db.session.add(u)
db.session.commit()

# Add Post
u = User.query.get(1)
p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()

## Output
# get all posts written by a user
u = User.query.get(1)
print(u)
#<User john>
posts = u.posts.all()
print(posts)
#[<Post my first post!>]

# same, but with a user that has no posts
u = User.query.get(2)
print(u)
#<User susan>
print(u.posts.all())
#[]

# print post author and body for all posts
posts = Post.query.all()
for p in posts:
    print(p.id, p.author.username, p.body)

#1 john my first post!

# get all users in reverse alphabetical order
print(User.query.order_by(User.username.desc()).all())
#[<User susan>, <User john>]

users = User.query.all()
for u in users:
    db.session.delete(u)

posts = Post.query.all()
for p in posts:
    db.session.delete(p)

db.session.commit()

posts = Post.query.all()
for p in posts:
    print(u.id, u.username)
