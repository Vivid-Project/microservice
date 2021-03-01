import json
import unittest
from copy import deepcopy
from api import microservice


class CreateToneTest(unittest.TestCase):
    def setUp(self):
        dream_text = "It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad? It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad? It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad?"

        self.app = microservice()
        self.client = self.app.test_client()
        self.payload = dream_text

    def test_endpoint_microservice_api_v1_tones(self):

        payload = deepcopy(self.payload)

        response = self.client.post(
            "/microservice/api/v1.0/tones",
            json=payload,
            content_type="application/json",
        )
        self.assertEqual(200, response.status_code)

        data = json.loads(response.data.decode("utf-8"))

        self.assertIsNotNone(data["tone_strength"])
        self.assertIsNotNone(data["unique_tones"])


if __name__ == "__main__":
    unittest.main()
