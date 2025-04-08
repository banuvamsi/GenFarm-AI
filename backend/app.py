# Placeholder Flask backend (for simulation purposes only)
from flask import Flask
app = Flask(__name__)

@app.route("/predict")
def predict():
    return {"result": "Healthy crop (simulated response)"}

if __name__ == "__main__":
    app.run(debug=True)
