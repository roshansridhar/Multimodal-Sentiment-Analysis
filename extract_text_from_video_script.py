# Convert video to audio

# vpath = r"C:\Datasets\MOUD\VideoReviews\178_makeup.mp4"

# from video-converter import Converter

apath = "C:\Users\Roshan Sridhar\Google Drive\Documents\NYU\GILAB\Python\MOUD\Text_Video\178_makeup.wav"

# TRANSLATION
# https://github.com/watson-developer-cloud/python-sdk/blob/f81bea7a44b83bd0d0ee080af66ad90baa3c0a23/examples/speech_to_text_v1.py
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='',
    password='',
    x_watson_learning_opt_out=False
)

# print(json.dumps(speech_to_text.models(), indent=2))

# print(json.dumps(speech_to_text.get_model('es-ES_BroadbandModel'), indent=2))

with open(apath,
          'rb') as audio_file:
    tran = speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=False, model='es-ES_BroadbandModel',
        word_confidence=False)

df_t = pd.DataFrame(columns = ['Speech','sentimentAnnotation'])

for i in range(len(tran['results'])):
    df_t.loc[len(df_t)]=[tran['results'][i]['alternatives'][0]['transcript'],np.NaN]

print(df_t)