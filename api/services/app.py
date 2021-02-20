from flask import Flask, jsonify, request
from tone_analyzer_service import ToneAnalyzerService

app = Flask(__name__)


# create new tone from dream journal entry text
@app.route('/microservice/api/v1.0/tones', methods=['POST'])
def get_tones():

    dream_text = str(request.data)

    tone_analysis = ToneAnalyzerService.get_tones(dream_text)

    return jsonify({'tone_analysis': tone_analysis})


if __name__ == '__main__':
    app.run(debug=True)


# get tone by id ? Might not be needed...

# @app.route('/microservice/api/v1.0/tones/<tone_id>', methods=['GET'])
# def find_single_tone(tone_id):
#     if tone_id not in tones:
#         return '', 404
#     return jsonify(tones[tone_id])
