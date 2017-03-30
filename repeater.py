from gtts import gTTS
from pygame import mixer
import speech_recognition
import tempfile as tp
r= speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = r.listen(source)
mixer.init()
def google_repeater(say_again):
    with tp.NamedTemporaryFile(delete = True) as tfp: 
        tts = gTTS(text=say_again, lang='zh')
        tts.save(tfp.name+".mp3")
        mixer.music.load(tfp.name+".mp3")
        mixer.music.play()

myword=r.recognize_google(audio,language='zh-TW')
google_repeater(myword)       
