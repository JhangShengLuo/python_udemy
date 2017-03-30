# -*- coding: utf-8 -*-

from gtts import gTTS
from pygame import mixer
mixer.init()
import speech_recognition
import tempfile as tp
r= speech_recognition.Recognizer()
def google_repeater(say_again):
    with tp.NamedTemporaryFile(delete = True) as tfp: 
        tts = gTTS(text=say_again, lang='zh-tw')
        tts.save(tfp.name+".mp3")
        mixer.music.load(tfp.name+".mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            pass
# google_repeater("成功")
try :
    print "進入try"
    with speech_recognition.Microphone() as source:
        print "進入source"
        audio = r.listen(source)
    print "出來source"
    myword=r.recognize_google(audio,language='zh-TW')
    print "repeat之前"
    google_repeater(myword)
    print "try"
except:
    google_repeater("錄音失敗")
    print "except"