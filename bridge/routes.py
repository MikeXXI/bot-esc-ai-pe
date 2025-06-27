from flask import Blueprint, request, jsonify
from services.openai_service import send_message_to_openai

# Création du blueprint pour les routes de l'API
api_bp = Blueprint('api', __name__)
@api_bp.route('/ask', methods=['POST'])
def ask_openai():
    """
    Route pour envoyer une question à OpenAI et obtenir une réponse.
    """
    data = request.get_json()
    
    # Vérification des données reçues
    if not data or 'question' not in data or 'environment' not in data or 'room' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    question = data['question']
    environment = data['environment']
    room = data['room']
    
    # Appel au service OpenAI
    response = send_message_to_openai(question, environment, room)
    
    return jsonify(response)