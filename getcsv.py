from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import csv

app = Flask(__name__)


connection_string = "mongodb+srv://eden:cardioassist1@cluster0.x6cubkp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client['CardiologistAssistant']  # Replace 'mydatabase' with your database name
collection = db['FormData']  # Replace 'mycollection' with your collection name


documents = collection.find()
fieldnames = [
    '_id',
    'name',
    'age',
    'sex',
    'length_of_pain',
    'pressure',
    'crushing',
    'squeezing',
    'tightness',
    'dull_ache',
    'burning',
    'sharp',
    'pins_and_needles',
    'other_description (quality_of_pain)',
    'middle_of_chest',
    'left_side_of_chest',
    'neck',
    'jaw',
    'left_shoulder/arm',
    'left_arm',
    'stomach_area',
    'other_(location_of_pain)',
    'rto_the_left_shoulder',
    'rup_the_neck',
    'rto_the_jaw',
    'rdown_left_arm',
    'rto_the_back',
    'rother_(radiation_of_pain)',
    'duration_of_pain',
    'frequency_of_pain',
    'exertion',
    'lifting_of_heavy_objects',
    'emotional_stress',
    'eating',
    'lying_down',
    'taking_a_deep_breath',
    'direct_palpation',
    'at_rest',
    'other_(precipitants_of_pain)',
    'rest',
    'eating_food',
    'other_(pain_relieved_by)',
    'shortness_of_breath',
    'palpitations',
    'sweating',
    'nausea',
    'dizziness',
    'fainting',
    'fever',
    'cough',
    'other_(associated_symptoms)',
    'high_blood_pressure',
    'diabetes',
    'high_cholesterol',
    'smoking',
    'family_history',
    'prior_history',
    'other_(risk_factors)'
]


csv_file_name = "output.csv"

with open(csv_file_name, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    documents.rewind()

    # Write the data rows
    for document in documents:
        writer.writerow(document)