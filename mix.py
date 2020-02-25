from glob import glob
from pydub import AudioSegment

i = 0
for name in sorted(glob("*.mp3")):
    i = i+1
    print str(i)+name

playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in sorted(glob("*.mp3"))]

print "Number of songs. "+str(len(playlist_songs))

for i in range(0, len(playlist_songs)):

    songcut = playlist_songs.pop(0)
    # songcut = songx[:30*1000]
    print i

    if i == 0:
        playlist = songcut
    else:
        # We don't want an abrupt stop at the end, so let's do a 10 second crossfades
        playlist = playlist.append(songcut, crossfade=(10 * 1000))

# let's fade out the end of the last song
# playlist = playlist.fade_out(30)

# hmm I wonder how long it is... ( len(audio_segment) returns milliseconds )
playlist_length = len(playlist) / (1000*60)

# lets save it!
with open("%s_minutes-mix-192kbps.mp3" % playlist_length, 'wb') as out_f:
    playlist.export(out_f,format="mp3",bitrate="192k")
    # playlist.export(out_f,format="wav")
