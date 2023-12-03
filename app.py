from flask import Flask, render_template, request, jsonify, send_from_directory
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulating a server delay
    time.sleep(1)
    return jsonify(message='Data loaded successfully!')


@app.route('/api/update', methods=['POST'])
def update_data():
    data = request.form.get('data')
    # Simulating a server delay
    time.sleep(2)
    return jsonify(message=f'Data updated: {data}')


# search api for the search bar
@app.route('/api/search', methods=['POST'])
def search_data():
    data = request.form.get('search')
    # Simulating a server delay
    time.sleep(2)
    return jsonify(message=f'Searching for: {data}')


# Serve static files (for demonstration purposes)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)



if __name__ == '__main__':
    app.run(debug=True)
