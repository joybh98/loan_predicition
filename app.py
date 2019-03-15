from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p 
import json
import os 

app = Flask(__name__)

@app.route('/api/',methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    
    return jsonify(prediction)

# Create pickle file to be used below
filename = 'models/final_prediction.pickle'
os.makedirs(os.path.dirname(filename),exist_ok=True)


if __name__ == '__main__':
    
    modelfile = 'models/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')