from flask import Flask

app = Flask(__name__)

pokemon_creatures = {
    "bilbasaur": "dinosaur",
    "charmander": "reptile",
    "pikachu": "rodent",
    "eevee": "fox",
    "diglett": "mole"
}

@app.get("/") # / is the root of our app this means if someone visits my app using a get reuqest and teh specific location they visit is the http://12223>>/, then we're gonna give them this recipe
def pokemon_list():
    return "Charmander, pikachu, eevee, bilbasaur, diglett"

 #the lines below are v1 until I highlight that v1 is ending, commenting out to implemnet

#
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



@app.get("/<pokemon_name>") # <> means that in the browser whatever I type after / it's gonna recognise as a name
def pokemon_data(pokemon_name):
    creature = pokemon_creatures.get(pokemon_name)
    return f"this is {pokemon_name}, a generation 1 pokemon who looks like a little {creature}"



if __name__ == "__main__": # if app is the current one running then run my app
    app.run()


# my server is like a resturant at the corner of my laptop, but its closed now
