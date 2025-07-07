from flask import Flask
from bridge.routes import api_bp
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Bot Escape AI API!"

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint to check the health of the API.
    Returns a simple JSON response indicating the API is running.
    """
    return {"status": "API is running"}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
