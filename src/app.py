from flask_sqlachemy import SQLalchemy
from flask import Flask
import requests

#configuring DB
app = Flask(__name__)
app.config['databae_uri'] = 'sqlite.//.db'
db.init_app(app)

class Users(db.Model):
  table_name ='Users'

  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String())

 def __init__(self,id,name):
    self.id = id
    self.name = name
   
class Projects(db.Model):
  table_name = 'Projects'

  id = db.Column(db.Integer,primary_key = True)
  project_name = db.Column(db.String())
  description= db.Column(db.String())

  def __init__(self,id,project_name,description):
    self.id = id
    self.project_name = project_name
    self.description = description


#creatting Views

@app.route('/data/create',methods=['GET','POST']
def create():
  if request.method =='GET':
    pass
  if request.method == 'POST':
    id = request.form['id']
    name = request.form['name']
  
    users = Users(id = id,name=name)
    db.session.add(users)

@app.route('/data/create',methods=['GET','POST']
def create():
  if request.method =='GET':
    pass
  if request.method == 'POST':
    id = request.form['id']
    project_name = request.form['project_name']
    description = request.form['description']

    project = Projects(id = id,project_name=project_name, description=description)
    db.session.add(project)
    





