from flask import Flask, request, send_file, jsonify, render_template
import os
import zipfile
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
COMPRESSED_FOLDER = 'compressed'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

# Serve the welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Serve the main tool page
@app.route('/tools')
def tools():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    original_filename = secure_filename(uploaded_file.filename)
    original_path = os.path.join(UPLOAD_FOLDER, original_filename)
    uploaded_file.save(original_path)

    compressed_filename = f"{original_filename}.zip"
    compressed_path = os.path.join(COMPRESSED_FOLDER, compressed_filename)

    with zipfile.ZipFile(compressed_path, 'w') as zipf:
        zipf.write(original_path, arcname=original_filename)

    return send_file(compressed_path, as_attachment=True)

@app.route('/decompress', methods=['POST'])
def decompress_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    compressed_file = request.files['file']
    if compressed_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    compressed_filename = secure_filename(compressed_file.filename)
    compressed_path = os.path.join(UPLOAD_FOLDER, compressed_filename)
    compressed_file.save(compressed_path)

    with zipfile.ZipFile(compressed_path, 'r') as zipf:
        zipf.extractall(UPLOAD_FOLDER)
        original_filename = zipf.namelist()[0]
    
    original_path = os.path.join(UPLOAD_FOLDER, original_filename)
    return send_file(original_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
