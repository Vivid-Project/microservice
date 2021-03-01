import unittest
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from api.services.tone_analyzer_service import ToneAnalyzerService


class ToneAnalyzerServiceTest(unittest.TestCase):
    def test_get_tone(self):
        dream_text = "It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad? It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad? It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad?"
        dream_text_2 = "Je m'baladais sur l'avenue le cœur ouvert à l'inconnu. J'avais envie de dire bonjour à n'importe qui. N'importe qui et ce fut toi, je t'ai dit n'importe quoi. Il suffisait de te parler, pour t'apprivoiser."

        tone_analysis = ToneAnalyzerService.get_tones(dream_text)

        self.assertIsNotNone(tone_analysis)
        self.assertIsNotNone(tone_analysis["document_tone"])
        self.assertIsNotNone(tone_analysis["document_tone"]["tones"])

        tone_analysis_2 = ToneAnalyzerService.get_tones(dream_text_2)

        self.assertIsNotNone(tone_analysis_2)
        self.assertIsNotNone(tone_analysis_2["document_tone"])
        self.assertIsNotNone(tone_analysis_2["document_tone"]["tones"])


if __name__ == "__main__":
    unittest.main()
