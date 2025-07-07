from flask import Blueprint, request, jsonify
from services.openai_service import send_message_to_openai
from services.vector_service import get_vector_context  # Ajout

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

    # 1. Recherche contextuelle dans la base vectorielle
    vector_context = get_vector_context(question)

    # 2. Ajoute le contexte à la question pour OpenAI
    response = send_message_to_openai(
        question=f"{vector_context}\n\n{question}" if vector_context else question,
        environment=environment,
        room=room
    )
    
    return jsonify(response)