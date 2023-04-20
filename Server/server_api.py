from flask import Flask, jsonify, request
from model import User # User.addUser(usr,email,pwd) ad esempio aggiunge un utente al DB 

app = Flask(__name__)

# Route that returns a list of every endpoint
@app.route('/', methods=['GET'])
def getAllEndpoints():
    return jsonify({'/': 'Route that returns a list of every endpoint ',
                    '/hello': 'Route that returns a JSON response'})

# Route that returns a JSON response
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello!'})


# non sono sicuro sull' async ma l'ho messo per poter aspettare la risposta della add_user 
@app.route('/register', methods=['POST'])
async def register():
    # procedure alla password qui

    # await User.add_user(request.json)
    return jsonify(request.json)

if __name__ == '__main__':
    app.run(debug=True)