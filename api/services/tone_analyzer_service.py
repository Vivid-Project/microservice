from ibm_watson import ToneAnalyzerV3
from api.services.config import TONE_ANALYZER_API_KEY
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class ToneAnalyzerService:
    @classmethod
    def get_tones(self, dream_text):

        # Authentication via IAM
        authenticator = IAMAuthenticator(TONE_ANALYZER_API_KEY)
        service = ToneAnalyzerV3(
            version='2017-09-21',
            authenticator=authenticator)

        service.set_service_url('https://gateway.watsonplatform.net/tone-analyzer/api')

        tone_analysis = service.tone(
            {'text': dream_text},
            content_type='application/json'
        ).get_result()

        return tone_analysis
