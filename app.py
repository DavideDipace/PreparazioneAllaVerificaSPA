from flask import Flask, request, jsonify, session, render_template, send_from_directory
import mysql.connector

app = Flask(__name__)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Definisci una rotta per ricevere il messaggio
@app.route('/saluto', methods=['POST'])
def saluto():
    # Ottieni il testo inviato nella richiesta
    data = request.get_json()
    messaggio = data.get('messaggio', '').lower()

    # Se il messaggio è "ciao", rispondi con "Ciao"
    if messaggio == "ciao":
        return jsonify({"risposta": "Ciao!"})
    else:
        return jsonify({"risposta": "Non ho capito, prova a scrivere 'ciao'."})

# Esegui l'app
if __name__ == '__main__':
    app.run(debug=True)