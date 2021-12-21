#!/usr/bin/env python3
from glob import glob
import sox

def sox_length(path):

    try:
        length = sox.file_info.duration(path)
        return length
    except:
        return None

def minsec(sec):
    return str(int(sec/60)) + ":" + format(int(sec%60),"02d")


i = 0
total = 0

for name in sorted(glob("*.mp3")):
    i = i+1
    length = sox_length(name)
    total += length
    print(name.replace(".mp3", "") + " (" + minsec(length) + "/" + minsec(total) + ")" )
