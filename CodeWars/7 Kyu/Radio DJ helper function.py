def to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds


def longest_possible(playback):
    longest_song = 0
    song_title = ''
    for song in songs:
        song_length = to_seconds(song['playback'])
        if longest_song < song_length <= playback:
            longest_song = song_length
            song_title = song['title']
    return song_title or False