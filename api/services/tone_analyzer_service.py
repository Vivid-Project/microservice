import os

import langid
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ToneAnalyzerV3
from ibm_watson.tone_analyzer_v3 import ToneInput


class ToneAnalyzerService:
    @classmethod
    def get_tones(self, dream_text):

        # Authentication via IAM
        authenticator = IAMAuthenticator(os.getenv("TONE_ANALYZER_API_KEY"))

        service = ToneAnalyzerV3(version="2017-09-21", authenticator=authenticator)

        service.set_service_url(
            "https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/35694f05-d1b2-4c03-9773-721372d1daf0"
        )

        def french_or_english(dream_text):
            lang = langid.classify(dream_text)
            if lang[0] == "fr":
                return "fr"
            else:
                return "en"

        language = french_or_english(dream_text)

        tone_input = ToneInput(dream_text)

        tone_analysis = service.tone(
            tone_input=tone_input,
            content_type="application/json",
            content_language=language,
            accept_language=language,
        ).get_result()

        return tone_analysis
