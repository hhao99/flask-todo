# -*- coding: utf-8 -*-
from microblog import db
import datetime

class Comment(db.EmbeddedDocument):
	created_at = db.DateTimeField(default=datetime.datetime.now,required=True)
	author = db.StringField(max_length=100,required=True)
	body = db.StringField(required=True)
	
class Post(db.Document):
	created_at = db.DateTimeField(default=datetime.datetime.now,required=True)
	title = db.StringField(max_length=200,required=True)
	body = db.StringField(required=True)
	comments = db.ListField(db.EmbeddedDocumentField('Comment'))
	
	meta = {
		'allow_inheritance' : True,
		'indexes': ['-created_at','title'],
		'ordering': ['-created_at']
	}



