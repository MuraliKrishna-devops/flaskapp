from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Define the path for the JSON file
json_file_path = 'data.json'

# Helper function to load data from the JSON file
def load_data():
    if os.path.exists(json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

# Helper function to save data to the JSON file
def save_data(data):
    try:
        with open(json_file_path, 'w') as file:
            json.dump(data, file)
    except IOError:
        return {"message": "Error saving data!"}

# Welcome route
@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

# Route to generate and save data
@app.route('/generate_data', methods=['POST'])
def generate_data():
    username = request.form.get('username')
    password = request.form.get('password')
    location = request.form.get('location')

    if not username or not password or not location:
        return jsonify({"message": "Missing fields!"}), 400

    new_data = {
        username: {
            'password': password,
            'location': location
        }
    }

    data = load_data()
    data.update(new_data)
    save_data(data)
    return jsonify({"message": "Data saved successfully!"})

# Route to show data based on a name
@app.route('/show_data', methods=['GET'])
def show_data():
    name = request.args.get('name')
    if not name:
        return jsonify({"message": "Name parameter is required!"}), 400

    data = load_data()
    if name in data:
        return jsonify({name: data[name]})
    else:
        return jsonify({"message": "Name not found!"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
