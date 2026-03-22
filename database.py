from pymongo import MongoClient
from bson import ObjectId

# --- MongoDB Connection ---
# Connect to your MongoDB server
# Make sure your MongoDB server is running on localhost:27017
client = MongoClient('mongodb://localhost:27017/')

# --- Select your database and collection ---
# Replace 'your_database_name' with the name of your database
db = client['your_database_name']
# Replace 'your_collection_name' with the name of your collection
collection = db['your_collection_name']

# Helper to convert ObjectId to string
def serialize_doc(doc):
    doc['_id'] = str(doc['_id'])
    return doc

def get_all_data():
    """
    Retrieves all documents from the specified collection.
    """
    try:
        # Find all documents in the collection
        data = [serialize_doc(doc) for doc in collection.find()]
        return data
    except Exception as e:
        # You might want to log the error here
        return {'error': str(e)}
