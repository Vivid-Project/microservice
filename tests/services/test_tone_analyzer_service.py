import unittest

from api.services.tone_analyzer_service import ToneAnalyzerService


class ToneAnalyzerServiceTest(unittest.TestCase):
    def test_get_english_tone(self):

        """
        Test Tone Analyzer Service can analyze text in English
        """

        dream_text = "It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad?"

        tone_analysis = ToneAnalyzerService.get_tones(dream_text)
        # self.assertEqual(response.get_status_code, 200)

        self.assertIsNotNone(tone_analysis)
        self.assertIsNotNone(tone_analysis["document_tone"])
        self.assertIsNotNone(tone_analysis["document_tone"]["tones"])

    def test_get_french_tone(self):

        """
        Test Tone Analyzer Service can analyze text in French
        """

        dream_text = "Je m'baladais sur l'avenue le cœur ouvert à l'inconnu. J'avais envie de dire bonjour à n'importe qui."

        tone_analysis = ToneAnalyzerService.get_tones(dream_text)
        # self.assertEqual(response.get_status_code, 200)

        self.assertIsNotNone(tone_analysis)
        self.assertIsNotNone(tone_analysis["document_tone"])
        self.assertIsNotNone(tone_analysis["document_tone"]["tones"])


if __name__ == '__main__':
    unittest.main()
