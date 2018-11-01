import os
import speech_recognition as sr
from tqdm import tqdm
from multiprocessing.dummy import Pool
pool = Pool(8) 

with open("api-key.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

r = sr.Recognizer()
files = sorted(os.listdir('/home/nikhil/Nefarians/UI/Res/split/'))

def transcribe(data):
    idx, file = data
    name = "/home/nikhil/Nefarians/UI/Res/split/" + file
    print(name + " started")
    
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
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