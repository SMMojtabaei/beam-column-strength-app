
# Paste the Flask application code here
from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import joblib
import os

app = Flask(__name__)

# Load model and scaler
model = tf.keras.models.load_model('beam_column_model.keras')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            inputs = [
                float(request.form['h_t']),
                float(request.form['b_t']),
                float(request.form['c_t']),
                float(request.form['kL_ry']),
                float(request.form['SlenC_SlenF']),
                float(request.form['Ex']),
                float(request.form['Ey']),
                float(request.form['rx_ry']),
            ]
            inputs_scaled = scaler.transform([inputs])
            prediction = model.predict(inputs_scaled)[0][0]
        except:
            prediction = "Error in input. Please check values."

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)