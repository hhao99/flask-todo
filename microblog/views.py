# -*- coding: utf-8 -*-
from flask import render_template,url_for,redirect
from flask import request
from microblog.models import Post,Comment
from microblog import app

@app.route('/')
def post_index():
	posts = Post.objects.all()
	return render_template('posts/list.html',posts=posts)
@app.route('/post/<id>')
def post_detail(id):
	post = Post.objects.get_or_404(id=id)
	return render_template('posts/detail.html',post=post)
@app.route('/post/new',methods=['GET','POST'])
def post_new():
	if (request.method == "POST"):
		post = Post()
		post.title = request.form['title']
		post.body = request.form['body']
		post.save()
		return redirect(url_for('post_index'))
	else:
		return render_template('posts/new.html')

@app.route('/post/edit/<id>',methods=['GET','POST'])
def post_edit(id):
	if  id:
		post = Post.objects.get(id=id)
	else:
		post = Post()

	if(request.method=='POST'):
		post.id = request.form['id']
		post.title = request.form['title']
		post.body = request.form['body']
		post.save()
		return	redirect(url_for('post_index'))
	else:
		return render_template('posts/edit.html',post=post)
@app.route('/post/comment',methods=['POST'])
def post_add_comment():
	if request.method == 'POST':
		post = Post.objects.get(id=request.form['id'])
		comment = Comment()
		comment.author = request.form['author']
		comment.body = request.form['body']
		post.comments.append(comment)
		post.save()
	return redirect(url_for('post_index'))
@app.route('/post/delete/<id>')
def post_delete(id):
	Post.objects.get(id=id).delete()
	return redirect(url_for('post_index'))
	
