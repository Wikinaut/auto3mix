from glob import glob
from pydub import AudioSegment

# based on the example
# https://github.com/jiaaro/pydub#how-about-another-example
#
# 20200225


i = 0
for name in sorted(glob("*.mp3")):
    i = i+1
    print str(i)+" "+name

playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in sorted(glob("*.mp3"))]

print "Found "+str(len(playlist_songs))+" songs."

for i in range(0, len(playlist_songs)):

    songcut = playlist_songs.pop(0)

    # you can modify the code to add only the first 30 seconds of each song
    # comment the next two lines if you want the uncropped original full-length songs in the mix
    songx = songcut
    songcut = songx[:30*1000]

    print "Now mixing song "+str(i+1)

    if i == 0:
        playlist = songcut
    else:
        # We don't want an abrupt stop at the end, so let's do a 10 second crossfades
        playlist = playlist.append(songcut, crossfade=(10 * 1000))

# let's fade out the end of the last song
# playlist = playlist.fade_out(30)

# hmm I wonder how long it is... ( len(audio_segment) returns milliseconds )
playlist_length = len(playlist) / (1000*60)

print "The mix playtime is "+str(playlist_length)+" minutes."

# lets save it!
with open("%s_minutes-mix-192kbps.mp3" % playlist_length, 'wb') as out_f:
    playlist.export(out_f,format="mp3",bitrate="192k")
    # playlist.export(out_f,format="wav")
