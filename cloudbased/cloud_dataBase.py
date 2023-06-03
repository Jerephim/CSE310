import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate('C:\\Users\\Jordan\\Desktop\\cloud based\\cloudjson.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://correctcloudproject-default-rtdb.firebaseio.com/'
})

# Get a reference to the Firebase Realtime Database root
ref = db.reference('/')

# Function to increment the number in the database
def increment_number():
    number = ref.child('number').get()
    ref.child('number').set(number + 1)

# Route to increment the number when the button is pressed
@app.route('/increment', methods=['GET','POST'])
def increment():
    increment_number()
    number = ref.child('number').get()  # Get the updated number value
    return f'This site has been visited {number} times.'  # Return the number value as the response

# Route to display the current number on the website
@app.route('/number', methods=['GET'])
def show_number():
    number = ref.child('number').get()  # Get the current number value
    return f'Current Number: {number}'  # Return the current number value as the response

# Run the Flask app
if __name__ == '__main__':
    app.run()
