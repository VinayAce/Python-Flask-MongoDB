from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://vinay:vinay123@ds215822.mlab.com:15822/connect_to_mongo'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({
        'name' : 'testing'
    })
    return 'Added User!'

if __name__ == '__main__':
        app.run(debug=True)