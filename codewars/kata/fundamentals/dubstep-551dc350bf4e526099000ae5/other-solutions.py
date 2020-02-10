# -------------------------------------------------------------------------------------------------

def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

# -------------------------------------------------------------------------------------------------

def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()

# -------------------------------------------------------------------------------------------------

def song_decoder(song):
    return ' '.join([a for a in song.split('WUB') if a])

# -------------------------------------------------------------------------------------------------

import re

def song_decoder(song):
    return re.sub(r'(WUB)+', ' ', song).strip()

# -------------------------------------------------------------------------------------------------
