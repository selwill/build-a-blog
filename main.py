from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:root@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(600))

    def __init__(self, title, body):
        self.title = title
        self.body = body
        


@app.route('/blog', methods=['POST', 'GET'])
def index():



@app.route('/newpost', methods=['POST', 'GET'])
def add_blog():

    title_error = ""
    body_error = ""


    if request.method == 'POST':
        
        title = request.form['title']
        body = request.form['body']
        
        if len(title) == 0:
            title_error = "Title cannot be left blank!"

        if len(body) == 0:
            body_error = "The body cannot be left blank!"

        return render_template('newpost.html')

    



if __name__ == '__main__':
    app.run()