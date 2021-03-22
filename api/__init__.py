import json
from flask import Flask, render_template, jsonify, request
from api.resources import format
from api.services.tone_analyzer_service import ToneAnalyzerService

def microservice():
    app = Flask(__name__)

    # create new tone from dream journal entry text
    @app.route('/microservice/api/v1.0/tones', methods=['POST'])
    def get_tones():

        dream_text = str(request.data)

        tone_analysis = ToneAnalyzerService.get_tones(dream_text)

        tone_results = jsonify({'tone_analysis': tone_analysis}).json

        return format.format_tone_results(tone_results)

    @app.route('/')
    def home_page():
        return render_template('index.html')

    return app
