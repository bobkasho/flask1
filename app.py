from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article $r>' % self.id

@app.route('/')
@app.route('/home')
def index():
    return "Hello World"


@app.route('/about')
def about():
    return "About page"


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + str.title(name) + " - " + str(id)

if __name__ == "__main__":
    app.run(debug=True)