from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokemons = db.collection.find(
    {"spawn_chance": {"$gt":1}},
    {"name": 1, "_id":0}
) 
writeAJson(pokemons,"pokemons") 

tipos = ["Fire", "Ground"]
pokemons = db.executeQuery({"$or": [{"type":tipos},{"weaknesses": "Bug"}] })
writeAJson(pokemons,"pokemons")

fraquezas = ["Water", "Ground"]
pokemons = db.executeQuery({"$or":[{"weaknesses":{"$in":fraquezas}},{"type":"Fire"}]})
writeAJson(pokemons,"pokemons")

pokemons = db.executeQuery({"next_evolution": {"$exists": False}})
writeAJson(pokemons,"pokemons")
pokemons = db.executeQuery({"$and":[{"next_evolution": {"$exists": False}},{"pre_evolution": {"$exists": False}}]})
writeAJson(pokemons,"pokemons")
pokemons = db.executeQuery({"$and":[{"name": "Pikachu"}, {"next_evolution": {"$exists": True}}]})
writeAJson(pokemons,"pokemons")

