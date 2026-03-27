from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

# Replace with your IBM Watson credentials
authenticator = IAMAuthenticator('YOUR_API_KEY')
nlp = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
nlp.set_service_url('YOUR_SERVICE_URL')

def detect_emotion(text):
    response = nlp.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()
    return response['emotion']['document']['emotion']

def format_output(emotions):
    return {k: f"{v*100:.2f}%" for k, v in emotions.items()}
