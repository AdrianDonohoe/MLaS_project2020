#!flask/bin/python
from flask import Flask
import tensorflow.keras as kr
from tensorflow.keras.models import load_model
import json

#load the model
model = load_model('wind_power.h5')

# define the flask app with static folder
app = Flask(__name__,static_url_path='', static_folder='static')

# add routes for /, /home and /index, with function that sends the index.html
@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

#route used to fetch the static image
@app.route('/images/<string:x>')
def image(x):
    return app.send_static_file(x)

# routes which serves the prediction requests
#function returns the model prediction
@app.route('/predict/<int:x>', methods=['GET'])
@app.route('/predict/<float:x>', methods=['GET'])
def predictor(x):
    prediction = model.predict([x])
    print(prediction[0][0])

    return str(prediction[0][0])



if __name__ == '__main__':
    app.run(debug= True)

