import unittest
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from api.services.tone_analyzer_service import ToneAnalyzerService

class ToneAnalyzerServiceTest(unittest.TestCase):
    def test_get_english_tone(self):

        """
        Test for getting an English tone from Tone Analyzer Service
        """

        dream_text = "It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad?"

        tone_analysis = ToneAnalyzerService.get_tones(dream_text)
        # self.assertEqual(response.get_status_code, 200)

        self.assertIsNotNone(tone_analysis)
        self.assertIsNotNone(tone_analysis["document_tone"])
        self.assertIsNotNone(tone_analysis["document_tone"]["tones"])

    def test_get_french_tone(self):

        """
        Test for getting a French tone from Tone Analyzer Service
        """

        dream_text = "Je m'baladais sur l'avenue le cœur ouvert à l'inconnu. J'avais envie de dire bonjour à n'importe qui."

        tone_analysis = ToneAnalyzerService.get_tones(dream_text)
        # self.assertEqual(response.get_status_code, 200)

        self.assertIsNotNone(tone_analysis)
        self.assertIsNotNone(tone_analysis["document_tone"])
        self.assertIsNotNone(tone_analysis["document_tone"]["tones"])

if __name__ == '__main__':
    unittest.main()
