from model import db, Post, Comment

##Sección de Post
def create_post(title, content):
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_all_posts():
    return Post.query.all()

def get_post_by_id(post_id):
    return Post.query.get(post_id)

##Sección de Comentarios
def create_comment(content, post):
    new_comment = Comment(content=content, post=post)
    db.session.add(new_comment)
    db.session.commit()