from glob import glob
from pydub import AudioSegment

i = 0
for name in sorted(glob("*.mp3")):
    i = i+1
    print name
