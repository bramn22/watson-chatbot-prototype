
'''url: https://stream.watsonplatform.net/speech-to-text/api'''
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username="4ecded31-4973-4b3f-b6cd-c8567dcb4819",
    password="tDnjcZHLkpkc",
    url="https://stream.watsonplatform.net/speech-to-text/api"
)

def listen(path):
    with open(path, 'rb') as file:
        speech_recognition_results = speech_to_text.recognize(
            audio=file,
            content_type='audio/wav',
            timestamps=True)
    return speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
