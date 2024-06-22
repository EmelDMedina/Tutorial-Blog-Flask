from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from model import db, Post, Comment
import controller

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = controller.get_post_by_id(post_id)
    return render_template('post.html', post=post)

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    controller.create_post(title=title, content=content)
    flash('Post creado con éxito!')
    return redirect(url_for('index'))

@app.route('/add_comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    post = controller.get_post_by_id(post_id) ##Post.query.get_or_404(post_id)
    content = request.form['comment']
    controller.create_comment(content=content, post=post)
    flash('Comentario agregado con éxito!')
    return redirect(url_for('post', post_id=post.id))

if __name__ == '__main__':
    app.run(debug=True)
