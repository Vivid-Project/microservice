import json
from collections import Counter

class Format:
    def format_tone_results(data):

        new = data["tone_analysis"]["sentences_tone"]

        def find_tone_names(data):
            counter = 0
            tone_names = []
            while counter != len(data):
                if not data[counter]["tones"]:
                    counter += 1
                else:
                    tone_names.append(data[counter]["tones"][0]["tone_name"])
                    counter += 1
            return tone_names

        def find_unique_tone_names(data):
            unique_list = []
            for x in data:
                if x not in unique_list:
                    unique_list.append(f'{x}')
            return ", ".join(unique_list)

        all_tones = find_tone_names(new)
        unique_tones = find_unique_tone_names(all_tones)
        strength_of_tone = Counter(all_tones)

        return {
            "unique_tones": unique_tones,
            "tone_strength": strength_of_tone
        }

        # "It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad? It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad? It's too bad. When did it get cool to be so sad? We're spinnin' backwards, did we all go mad?"

        # "Let the kick drum kick one time. Breathe out let your mind unwind. Eyes on the ceiling. Looking for the feeling. Wide open let your own eyes shine"


        # "Starlight. I will be chasing a starlight. Until the end of my life. I don't know if it's worth it anymore. Hold you in my arms. I just wanted to hold. You in my arms. My life. You electrify my life. Let's conspire to ignite. All the souls that would die just to feel alive"
