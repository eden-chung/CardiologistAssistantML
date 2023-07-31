from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import csv

connection_string = "mongodb+srv://eden:cardioassist1@cluster0.x6cubkp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client['CardiologistAssistant']  # Replace 'mydatabase' with your database name
collection = db['FormData']  # Replace 'mycollection' with your collection name

result = collection.delete_many({})

# Check the deletion result
print(f"Deleted {result.deleted_count} documents.")
