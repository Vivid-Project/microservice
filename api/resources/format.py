from collections import Counter

def find_tone_names(data):
    counter = 0
    tone_names = []
    while counter != len(data):
        if not data[counter]["tones"]:  # If sentence has no tone, +1 to counter and continue
            counter += 1  # pragma: no cover
        else:
            tone_in_sentence_counter = 0
            while tone_in_sentence_counter != len(data[counter]["tones"]):  # If sentence has multiple tones, add each before continuing to next sentence
                tone_names.append(
                    data[counter]["tones"][tone_in_sentence_counter][
                        "tone_name"
                    ]
                )
                tone_in_sentence_counter += 1
            counter += 1
    return tone_names

def find_unique_tone_names(data):
    unique_list = []
    for tone in data:
        if tone not in unique_list:
            unique_list.append(f"{tone}")
    return ", ".join(unique_list)


def format_tone_results(data):
    # If there is no punctuation present, return error
    if len(data["tone_analysis"]) == 1:
        return "Error: Please add punctuation to your dream journal entry"
    else:
        sentences_tone_data = data["tone_analysis"]["sentences_tone"]

        all_tones = find_tone_names(sentences_tone_data)
        unique_tones = find_unique_tone_names(all_tones)
        strength_of_tone = Counter(all_tones)

        return {"unique_tones": unique_tones, "tone_strength": strength_of_tone}
