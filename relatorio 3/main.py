from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokemons = db.collection.find(
	{"spawn_chance": {"$gt":1}},
	{"name": 1, "_id": 0,"spawn_chance": 1}
)



pokemons = db.executeQuery({"$or": [{"type":"water"},{"weaknesses": "grass"}]})
pokemons = db.getPokemonEvolutionsByName("Charmander")
pokemons = db.executeQuery({"next_evolution": {"$exists": True} })  
pokemons = db.executeQuery({"spawn_chance": {"$gt": 0.3}})