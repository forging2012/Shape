#-*-coding:utf-8-*-

from . import blog_blueprint
from flask import render_template
from main.forms import CommentForm
from main.models import Post

"""
主要展示好评、推荐文章
"""
@blog_blueprint.route("/")
def blog_index():
    return render_template("blog.html")

"""
主要展示所有文章，只按发表时间顺序
"""
@blog_blueprint.route("/post_list")
def post_list():
    post_list = Post.query.order_by(Post.publish_date.desc()).all()
    return render_template("blog/post.html",post=post)

"""
显示单个文章
"""
@blog_blueprint.route("/post_list/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("blog/post.html", post=post)

"""
显示单个文章的用户操作
"""
@blog_blueprint.route("/post_list/<int:post_id>/<string:control>")
def post_id_control():
    pass