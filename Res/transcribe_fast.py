import os
# import speech_recognition as sr
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
from tqdm import tqdm
from multiprocessing.dummy import Pool
pool = Pool(8) 

files = sorted(os.listdir('C:/Users/nikhi/Downloads/The-Synogence/Res/split/'))

def transcribe(data):
    text=""
    idx, file = data
    name = "C:/Users/nikhi/Downloads/The-Synogence/Res/split/" + file
    print(name + " started")
    client = speech_v1.SpeechClient()
    language_code = "en-US"

    sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "audio_channel_count":2,
    }
    with io.open(name, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    print(response.results)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        # print(u"Transcript: {}".format(alternative.transcript))
        text=text+alternative.transcript
    
    print(name + " done")
    return {
        "idx": idx,
        "text": text
    }
    
all_text = pool.map(transcribe, enumerate(files))
pool.close()
pool.join()


transcript = ""
for t in sorted(all_text, key=lambda x: x['idx']):
    total_seconds = t['idx'] * 30
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)
    transcript = transcript + "{}{} \n".format(t['text'],".")

print(transcript)

with open("transcript.txt", "w") as f:
    f.write(transcript)