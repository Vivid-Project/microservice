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

        
