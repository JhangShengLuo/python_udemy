#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import mixer
mixer.init()
mixer.music.load("/Users/Jackie/Desktop/python_course/audio.mp3")
# mixer.music.set_volume(1)
mixer.music.play()

while mixer.music.get_busy():
    pass
        # check if playback has finished
        