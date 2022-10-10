from flask import Flask
import requests
from helpers import get_pokemon_by_name

app = Flask(__name__)

#the lines below are v2 until I highlight that v2 is ending, commenting out to implemnet
# pokemon_creatures = {
#     "bilbasaur": "dinosaur",
#     "charmander": "reptile",
#     "pikachu": "rodent",
#     "eevee": "fox",
#     "diglett": "mole"
# }
# </v2>


# <v1> and <v2>
@app.get("/") # / is the root of our app this means if someone visits my app using a get reuqest and teh specific location they visit is the http://12223>>/, then we're gonna give them this recipe
def pokemon_list():
    return "Charmander, pikachu, eevee, bilbasaur, diglett"

# </v1> and </v2>

 #the lines below are v1 until I highlight that v1 is ending, commenting out to implemnet

# @app.get("/bulbasaur")
# def bulbasaur_data():
#     return "this is bulbasaur generation 1 pokemon who looks like a little dinosaur"
#
# @app.get("/charmander")
# def charmander_data():
#     return "this is charmander generation 1 pokemon who looks like a little reptile"
#
# @app.get("/pikachu")
# def pikachu_data():
#     return "this is pikachu generation 1 pokemon who looks like a little rodent"
#
# @app.get("/eevee")
# def eevee_data():
#     return "this is eevee generation 1 pokemon who looks like a little fox"
#
# @app.get("/diglett")
# def diglett_data():
#     return "this is diglett generation 1 pokemon who looks like a little mole"
#
# end of v1


# <v2>
# @app.get("/<pokemon_name>") # <> means that in the browser whatever I type after / it's gonna recognise as a name
# def pokemon_data(pokemon_name):
#     creature = pokemon_creatures.get(pokemon_name)
#     return f"this is {pokemon_name}, a generation 1 pokemon who looks like a little {creature}"
# </v2>

#<v3>
@app.get("/<pokemon_name>") # <> means that in the browser whatever I type after / it's gonna recognise as a name
def pokemon_data(pokemon_name):
    pokemon = get_pokemon_by_name(pokemon_name)
    return f"This is {pokemon['name']}. \n" \
           f"Height: {pokemon['height']}.\n" \
           f"Weight: {pokemon['weight']}. \n" \
           f"Base experience: {pokemon['base_experience']}.\n" \
           f"Type(s): {'and'.join(type_info['type']['name'] for type_info in pokemon['types'])}"

#</v2>


if __name__ == "__main__": # if app is the current one running then run my app
    app.run()


# my server is like a resturant at the corner of my laptop, but its closed now
