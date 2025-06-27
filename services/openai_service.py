from flask import jsonify
import requests
import openai

OPENAI_URL = "https://api.openai.com/v1/chat/completions"
# Charger la clé API OpenAI depuis un fichier
# Assurez-vous que le fichier API_KEY contient uniquement la clé API sans espaces ni nouvelles lignes
# Exemple de contenu du fichier API_KEY :
# sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
with open("API_KEY", "r") as f:
    OPENAI_API_KEY = f.read().strip()

def send_message_to_openai(question, environment, room):
    # Préparer le contexte
    context = f"Environnement : {environment}. Salle : {room}."
    message = f"{context} Question : {question}"

    payload = {
        "model": "gpt-4.1-nano",
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(OPENAI_URL, json=payload, headers=headers)
    if response.status_code == 200:
        # Adapter selon la structure de la réponse OpenAI
        return {"response": response.json()["choices"][0]["message"]["content"]}
    else:
        return {"error": "OpenAI error", "details": response.text}