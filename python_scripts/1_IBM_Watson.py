from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

#Connect to IBM Watson
authenticator = IAMAuthenticator('...')
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/...')


#Select the data path
speech = '/Users/tim/Desktop/comparison_data/stop/45_no_hash_1.wav'


#Use the IBM Watson Speech to Text
with open(speech, 'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav',
        timestamps=True,
        word_confidence=True,
        model='en-US_NarrowbandModel',
        continuous = True,
        indent=3
    ).get_result()
print(json.dumps(speech_recognition_results))

