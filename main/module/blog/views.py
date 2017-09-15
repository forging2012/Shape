#-*-coding:utf-8-*-

from . import blog_blueprint
from flask import render_template
from main.forms import CommentForm
from main.models import Post

@blog_blueprint.route("/")
def blog_index():
    return render_template("blog.html")

@blog_blueprint.route("/<int:post_id>")
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template("blog/post.html",post=post)