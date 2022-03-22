import click
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db
from App.main import app, migrate
from App.controllers import ( 
    create_user,
    get_all_users, 
    get_all_users_json, 
    get_all_games, 
    create_game, 
    get_user_listings, 
    list_game 
)

# This commands file allow you to create convenient CLI commands
# for testing controllers

# This command creates and intializes the database
@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <commmand>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Game Commands
'''

game_cli = AppGroup('game', help='Game object commands') 

@game_cli.command("list", help="Lists the games in the database")
def get_games():
    print(get_all_games())

@game_cli.command("create", help="Creates a game")
@click.argument("title") #can be customized to accept genre, platform etc
def make_game(title):
    create_game(title)
    print('Game Created')

app.cli.add_command(game_cli)

'''
Generic Commands
'''

@app.cli.command("list-game", help="Lets a user list a game for rental")
def list_game_command():
    print(get_all_users_json())
    userId = input('Enter a userId: ')
    print(get_all_games())
    gameId = input('Enter a gameId: ')
    res = list_game(userId, gameId)
    if res:
        print('Game added to user!')
    else :
        print("error add game to user")
