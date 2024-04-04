import pickle
import numpy as np

from flask import Flask, request, jsonify

abs_path = './models/model.pkl'

# Зloading the model from the file
with open(abs_path, 'rb') as pkl_file:
    model = pickle.load(pkl_file)


# Creating an application
app = Flask(__name__)


@app.route('/')
def index():
    msg = "Test message. The server is running"
    return msg


@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json)
    features = np.array(features).reshape(1, len(features))
    
    prediction = model.predict(features)
    
    return jsonify({
        'prediction': prediction[0]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 