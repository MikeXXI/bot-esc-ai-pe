from flask import jsonify
import requests

BOTPRESS_URL = "https://cdn.botpress.cloud/webchat/v3.0/shareable.html?configUrl=https://files.bpcontent.cloud/2025/06/26/12/20250626121926-NTXOTQA0.json"
BOTPRESS_API_KEY = "bp_pat_zl0eJm62jqPJJZhdRqovwVh7NXkoUMYr45ns"

def send_message_to_botpress(question, environment, room):
    # Préparer le contexte
    context = f"Environnement : {environment}. Salle : {room}."
    message = f"{context} Question : {question}"

    payload = {
        "messages": [
            {"type": "text", "text": message}
        ],
        "sessionId": "user-session-1"  # À personnaliser si besoin
    }

    headers = {
        "Authorization": f"Bearer {BOTPRESS_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(BOTPRESS_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        # Adapter selon la structure de la réponse Botpress
        return {"response": response.json()["responses"][0]["payload"]["text"]}
    else:
        return {"error": "Botpress error", "details": response.text}