from flask import Flask, jsonify, request
from model import User # User.addUser(usr,email,pwd) ad esempio aggiunge un utente al DB 
import json

# Metodo	Endpoint	Descrizione

# GET	/utenti	Ottenere la lista degli utenti
# POST	/utenti	Creare un nuovo utente (ricercatore o valutatore o blank)
# GET	/utenti/{id}	Ottenere i dettagli di un utente
# PUT	/utenti/{id}	Aggiornare i dettagli di un utente
# DELETE	/utenti/{id}	Eliminare un utente

# GET	/ricercatori	Ottenere la lista dei ricercatori
# GET	/ricercatori/{id}	Ottenere i dettagli di un ricercatore
# PUT	/ricercatori/{id}	Aggiornare i dettagli di un ricercatore
# GET   /ricercatori/{id}/progetti  Ottenere la lista dei progetti di un ricercatore
# POST  /ricercatori/{id}/progetti  Creare un nuovo progetto a nome del ricercatore {id}
# GET   /ricercatori/{id}/progetti/{projectId}/messaggi Ottenere la lista dei messaggi del progetto {projectId} di uno specifico ricercatore {id}
# POST  /ricercatori/{id}/progetti/{projectId}/valutatori/{valutatoreId}/messaggi Inviare un messaggio nella chat del progetto {projectId} di uno specifico ricercatore {id}

# GET   /ricercatori/{id}/progetti/{projectId}/report Ottiene tutti i report di uno specifico progetto
# GET   /ricercatori/{id}/progetti/{projectId}/valutatori Ottiene tutti i valutatori di uno specifico progetto 

# GET	/valutatori	Ottenere la lista dei valutatori
# GET	/valutatori/{id}	Ottenere i dettagli di un valutatore
# PUT	/valutatori/{id}	Aggiornare i dettagli di un valutatore
# GET   /valutatori/{id}/report Ottenere la lista di report di un valutatore
# POST  /valutatori/{id}/progetti/{projectId}/report Creare un nuovo report di un progetto {projectId} a nome del valutatore {id}
# GET   /valutatori/{id}/progetti/{projectId}/report Ottenere tutti i report di uno specifico progetto {projectId} a nome del valutatore {id}
# GET   /valutatori/{id}/report     Ottenere tutti i report del valutatore {id}

# 

# -----------------------------------------------------

# POST	/messaggi	Creare un nuovo messaggio
# GET	/messaggi/{id}	Ottenere i dettagli di un messaggio
# PUT	/messaggi/{id}	Aggiornare i dettagli di un messaggio
# DELETE	/messaggi/{id}	Eliminare un messaggio

# GET	/progetti	Ottenere la lista dei progetti
# POST	/progetti	Creare un nuovo progetto
# GET	/progetti/{id}	Ottenere i dettagli di un progetto
# PUT	/progetti/{id}	Aggiornare i dettagli di un progetto
# DELETE	/progetti/{id}	Eliminare un progetto

# GET	/report-valutazioni	Ottenere la lista dei report di valutazione
# POST	/report-valutazioni	Creare un nuovo report di valutazione
# GET	/report-valutazioni/{id}	Ottenere i dettagli di un report di valutazione
# PUT	/report-valutazioni/{id}	Aggiornare i dettagli di un report di valutazione
# DELETE	/report-valutazioni/{id}	Eliminare un report di valutazione
# GET	/versioni-progetto	Ottenere la lista delle versioni di un progetto
# POST	/versioni-progetto	Creare una nuova versione di un progetto
# GET	/versioni-progetto/{id}	Ottenere i dettagli di una versione di un progetto
# PUT	/versioni-progetto/{id}	Aggiornare i dettagli di una versione di un progetto
# DELETE	/versioni-progetto/{id}	Eliminare una versione di un progetto
# GET	/documenti-progetto	Ottenere la lista dei documenti di un progetto
# POST	/documenti-progetto	Caricare un nuovo documento per un progetto
# GET	/documenti-progetto/{id}	Ottenere i dettagli di un documento di un progetto
# DELETE	/documenti-progetto/{id}	Eliminare un documento di un progetto
# GET	/finestre-valutazione	Ottenere la lista delle finestre di valutazione
# POST	/finestre-valutazione	Creare una nuova finestra di valutazione
# GET	/finestre-valutazione/{id}	Ottenere i dettagli di una finestra di valutazione
# PUT	/finestre-valutazione/{id}	Aggiornare i dettagli di una finestra di valutazione
# DELETE	/finestre-valutazione/{id}	Eliminare una finestra di valutazione


app = Flask(__name__)

# Route that returns a list of every endpoint
@app.route('/', methods=['GET'])
def getAllEndpoints():
    return jsonify({'/': 'Route that returns a list of every endpoint ',
                    '/register': 'Route that registers a user'})

# Inserisce un utente nel DB 
# type: POST
# body: {"username":"xxxxx", "email": "xxxxx", "password": "xxxxx"}
@app.route('/register', methods=['POST'])
def register():
    # procedure alla password qui
    try:
        User.add_user(request.json["username"], request.json["email"], request.json["password"])
        # response = json.loads(request.json)
        return jsonify(request.json)
    except Exception as e:
        return jsonify({"error":e.args})

if __name__ == '__main__':
    app.run(debug=True)

