from flask import Flask, render_template, request, jsonify
from PIL import Image
import io
import requests

app = Flask(__name__)

API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "image/png",
    "Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_comic', methods=['POST'])
def generate_comic():
    try:
        inputs = request.json['inputs']

        # Generate images using the provided text inputs
        images = []
        for text_input in inputs:
            image_bytes = query({"inputs": text_input})
            images.append(image_bytes.decode('utf-8'))

        return jsonify(images)
    except Exception as e:
        print(f"Error generating comic: {str(e)}")
        return jsonify({"error": "Failed to generate comic"}), 500

if __name__ == '__main__':
    app.run(debug=True)
