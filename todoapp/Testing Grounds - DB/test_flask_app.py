from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Application settings:
webserver = Flask(__name__)

webserver.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:cyberfalcon@localhost:5432/table_db'
webserver.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(webserver)
#####################################


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person: {self.id},{self.name}>'


db.create_all()


# Routes:
@webserver.route("/")
def index():
    user = Person.query.first()
    return "Hello! " + user.name


# Development Settings:
if __name__ == '__main__':
    webserver.run(host="localhost", port=8000, debug=True)
