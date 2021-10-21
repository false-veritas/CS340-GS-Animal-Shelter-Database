from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37148/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        self.database = self.client['AAC']

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Read method to implement the R in CRUD. 
    def read(self,data):
        if data is not None:
            cursor = self.database.animals.find_one(data) 
            return cursor
        else:
            raise Exception("Data parameter is empty")
            return False
        
    def read_all(self,data): 
        cursor = self.database.animals.find(data, {'_id':False} )
        return cursor
        
# Update method to implement the U in CRUD.
    def update(self,data,newData):
        if data is not None:
            if newData is not None:
                self.database.animals.update_many(data, {"$set": newData})
                doc = self.database.animals.find(newData)
                return dumps(doc) ## return JSON
            else:
                raise Exception("New Data Parameter is empty")
                return False
                    
        else:
            raise Exception("Data parameter is empty")
            return False
        
# Delete method to implement the D in CRUD
    def delete(self,data):
        if data is not None:
            self.database.animals.remove(data)
            doc = self.database.animals.find(data)
            return dumps(doc) ## return JSON
        else:
            raise Exception("Data parameter is empty")
            return False