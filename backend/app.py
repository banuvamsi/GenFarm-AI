from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to GenFarm AI Backend!'

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    possible_diseases = ["Leaf Blight", "Powdery Mildew", "Rust", "Bacterial Spot", "Healthy"]
    suggestions = {
        "Leaf Blight": "Use organic fungicide and remove affected leaves.",
        "Powdery Mildew": "Apply sulfur-based spray and avoid overhead watering.",
        "Rust": "Remove infected leaves and use neem oil.",
        "Bacterial Spot": "Use copper-based spray and improve air circulation.",
        "Healthy": "No issues detected. Keep monitoring your crop."
    }

    disease = random.choice(possible_diseases)
    return jsonify({
        'disease': disease,
        'suggestion': suggestions[disease]
    })
