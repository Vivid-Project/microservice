import json
from flask import Flask, jsonify, request
from api.resources.format import Format
from api.services.tone_analyzer_service import ToneAnalyzerService

def microservice():
    app = Flask(__name__)

    # create new tone from dream journal entry text
    @app.route('/microservice/api/v1.0/tones', methods=['POST'])
    def get_tones():

        dream_text = str(request.data)

        tone_analysis = ToneAnalyzerService.get_tones(dream_text)

        # Could be refactored
        tone_results = jsonify({'tone_analysis': tone_analysis}).json

        return Format.format_tone_results(tone_results)

    return app
