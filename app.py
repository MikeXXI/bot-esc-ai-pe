from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello depuis Flask !"

@app.route('/aide', methods=['POST'])
def aide():
    question = request.json.get("question")
    return jsonify(reponse=f"Indice IA : {question}")

if __name__ == '__main__':
    app.run(debug=True)
