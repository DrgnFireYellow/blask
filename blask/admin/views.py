from flask import Blueprint, render_template, request, redirect
from blask.main.models import Post
from blask import auth, db

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route("/admin/create-post/", methods=["GET", "POST"])
@auth.required
def create_post():
    if request.method == "POST":
        post = Post(request.form["title"], request.form["contents"])
        db.session.add(post)
        db.session.commit()
        return redirect("/")
    return render_template("create_post.html")

@admin_blueprint.route("/admin/delete-post/")
@admin_blueprint.route('/admin/delete-post/<int:id>')
@auth.required
def delete_post(id=None):
    if id == None:
        posts = Post.query.all()
        posts.reverse()
        return render_template("delete_post.html", posts=posts)
    else:
        db.session.delete(Post.query.get_or_404(id))
        db.session.commit()
        return redirect("/")