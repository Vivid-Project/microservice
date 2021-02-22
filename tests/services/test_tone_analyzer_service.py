import unittest
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from api.services.tone_analyzer_service import ToneAnalyzerService


class ToneAnalyzerServiceTest(unittest.TestCase):

    def test_get_tone(self):
        dream_text = "It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad? It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad? It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad?"

        tone = ToneAnalyzerService.get_tones(dream_text)

        print(tone)

        # Make assertions
