from flask import Blueprint, render_template
from blask import db
from blask.main.models import Post

blueprint = Blueprint('views', __name__)

@blueprint.route("/")
def all_posts():
    posts = Post.query.all()
    posts.reverse()
    return render_template("all_posts.html", posts=posts)

@blueprint.route("/post/<int:id>")
def post(id):
    return render_template("post.html", post=Post.query.get_or_404(id))