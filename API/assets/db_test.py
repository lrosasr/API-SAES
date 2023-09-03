from pysondb import getDb
db = getDb("API/materias.json")
#print(db.getByQuery({"codigo":"M312"}))
print(db.get(1)[0]["creditos"])