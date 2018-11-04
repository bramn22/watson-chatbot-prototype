
'''https://stream.watsonplatform.net/text-to-speech/api'''

from watson_developer_cloud import TextToSpeechV1
import json


text_to_speech = TextToSpeechV1(
    username="f54ecc2e-4f64-43c2-8940-6b1cc3a16dba",
    password="O2M4KYuNal4e"
)
print(json.dumps(text_to_speech.list_voices(), indent=2))
def speak(txt):
    mp3 = text_to_speech.synthesize(txt, accept='audio/mp3',
                                      voice="en-US_AllisonVoice").content

    with open('output.mp3', 'wb') as file:
        file.write(mp3)

