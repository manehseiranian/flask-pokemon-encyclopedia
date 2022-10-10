from flask import Flask

app = Flask(__name__)

@app.get("/")# / is the root of our app this means if someone visits my app using a get reuqest and teh specific location they visit is the http://12223>>/, then we're gonna give them this recipe
def pokemon_list():
    return "Charmander, pikachu, eevee, bilbasaur, diglett"

@app.get("/bulbasaur")
def bulbasaur_data():
    return "this is bulbasaur generation 1 pokemon who looks like a little dinosaur"

@app.get("/charmander")
def charmander_data():
    return "this is charmander generation 1 pokemon who looks like a little reptile"

@app.get("/pikachu")
def pikachu_data():
    return "this is pikachu generation 1 pokemon who looks like a little rodent"

@app.get("/eevee")
def eevee_data():
    return "this is eevee generation 1 pokemon who looks like a little fox"

@app.get("/diglett")
def diglett_data():
    return "this is diglett generation 1 pokemon who looks like a little mole"



#Menu item carbonara:
# Beat the eggs
# Chop the pancetta
# Grate the cheese
# Boil the pasta
# Add everything to the pan
#



if __name__ == "__main__": # if app is the current one running then run my app
    app.run()


# my server is like a resturant at the corner of my laptop, but its closed now
