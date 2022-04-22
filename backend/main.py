from flask import Flask, jsonify, request, request
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
# CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello World!")

@app.route('/shark', methods=['GET'])
def shark():
    return("Shark!")

GAMES = [
    {
        'title': '2k21',
        'genre': 'sports',
        'played': True,
    },
    {
        'title': 'Evil Within',
        'genre': 'horror',
        'played': False,
    },
    {
        'title': 'The Last of Us',
        'genre': 'survival',
        'played': True,
    },
    {
        'title': 'Days Gone',
        'genre': 'horror/survival',
        'played': False,
    },
    {
        'title': 'Mario',
        'genre': 'retro',
        'played': True,
    }
]

@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game Added!'
    else:
        response_object['games'] = GAMES
    
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)

