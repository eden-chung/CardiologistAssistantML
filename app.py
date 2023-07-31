from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import csv

app = Flask(__name__)

app.use_static = True

@app.route('/submit', methods=['POST'])
def submit_form():
    connection_string = "mongodb+srv://eden:cardioassist1@cluster0.x6cubkp.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(connection_string, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    db = client['CardiologistAssistant']
    collection = db['FormData']

    if request.method == 'POST':
        form_data = {
            'name': request.form.get('name'),
            'age': request.form.get('age'),
            'sex': request.form.get('sex'),
            'length_of_pain': request.form.get('lengthpain'),
            'pressure': request.form.get('pressure') == 'on',
            'crushing': request.form.get('crushing') == 'on',
            'squeezing': request.form.get('squeezing') == 'on',
            'tightness': request.form.get('tightness') == 'on',
            'dull_ache': request.form.get('dull ache') == 'on',
            'burning': request.form.get('burning') == 'on',
            'sharp': request.form.get('sharp') == 'on',
            'pins_and_needles': request.form.get('pins and needles') == 'on',
            'other_description (quality_of_pain)': request.form.get('otherpain'),
            'middle_of_chest': request.form.get('middle of chest') == 'on',
            'left_side_of_chest': request.form.get('left side of chest') == 'on',
            'neck': request.form.get('neck') == 'on',
            'jaw': request.form.get('jaw') == 'on',
            'left_shoulder/arm': request.form.get('left shoulder/arm') == 'on',
            'left_arm': request.form.get('left arm') == 'on',
            'stomach_area': request.form.get('stomach area') == 'on',
            'other_(location_of_pain)': request.form.get('otherlocation'),
            'rto_the_left_shoulder': request.form.get('rto the left shoulder') == 'on',
            'rup_the_neck': request.form.get('rup the neck') == 'on',
            'rto_the_jaw': request.form.get('rto the jaw') == 'on',
            'rdown_left_arm': request.form.get('rdown left arm') == 'on',
            'rto_the_back': request.form.get('rto the back') == 'on',
            'rother_(radiation_of_pain)': request.form.get('otherradiation'),
            'duration_of_pain': request.form.get('durationpain'),
            'frequency_of_pain': request.form.get('frequencypain'),
            'exertion': request.form.get('exertion') == 'on',
            'lifting_of_heavy_objects': request.form.get('lifting of heavy objects') == 'on',
            'emotional_stress': request.form.get('emotional stress') == 'on',
            'eating': request.form.get('eating') == 'on',
            'lying_down': request.form.get('lying down') == 'on',
            'taking_a_deep_breath': request.form.get('taking a deep breath') == 'on',
            'direct_palpation': request.form.get('direct palpation') == 'on',
            'at_rest': request.form.get('at rest') == 'on',
            'other_(precipitants_of_pain)': request.form.get('otherprecipitants'),
            'rest': request.form.get('rest') == 'on',
            'eating_food': request.form.get('eating food') == 'on',
            'other_(pain_relieved_by)': request.form.get('otherrelief'),
            'shortness_of_breath': request.form.get('shortness of breath') == 'on',
            'palpitations': request.form.get('palpitations') == 'on',
            'sweating': request.form.get('sweating') == 'on',
            'nausea': request.form.get('nausea') == 'on',
            'dizziness': request.form.get('dizziness') == 'on',
            'fainting': request.form.get('fainting') == 'on',
            'fever': request.form.get('fever') == 'on',
            'cough': request.form.get('cough') == 'on',
            'other_(associated_symptoms)': request.form.get('othersymptoms'),
            'high_blood_pressure': request.form.get('high blood pressure') == 'on',
            'diabetes': request.form.get('diabetes') == 'on',
            'high_cholesterol': request.form.get('high cholesterol') == 'on',
            'smoking': request.form.get('smoking') == 'on',
            'family_history': request.form.get('familyhist') == 'on',
            'prior_history': request.form.get('priorhistory') == 'on',
            'other_(risk_factors)': request.form.get('otherrisks')
        }

        collection.insert_one(form_data) 

    client.close()

    return 'Form submitted successfully'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()