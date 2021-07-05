from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='RPS')

@app.route ('/rules')
def rules():
    return render_template('rules.html')

@app.route('/play', methods=["POST"])
def play():
    player_1_name = request.form['player_1_name']
    player_1_choice = request.form['player_1_choice']
    player_2_name = request.form['player_2_name']
    player_2_choice = request.form['player_2_choice']
    player_1 = Player(name=player_1_name, choice=player_1_choice)
    player_2 = Player(name=player_2_name, choice=player_2_choice)
    game = Game(player_1, player_2)
    result = game.winner()
    return render_template('result.html', player_1 = player_1, player_2 = player_2, game = game)


# @app.route('/<choice_1>/<choice_2>')
# def play_game(choice_1, choice_2):
#     player_1 = Player("Player 1", choice_1)
#     player_2 = Player("Player 2", choice_2)
#     game = Game()
#     winner = Game.play(player_1, player_2)
#     return render_template("result.html", winner = winner, player_1=player_1, player_2=player_2, game=game)
