import math
import tidalapi

def duplichecker():
    session = tidalapi.Session()
    session.login('max-mustermann545@gmx.de', 'PTmk29cKQdaCApQbz62T')
    tracks = session.user.favorites.tracks()
    checked = []
    for track in tracks:
        if (track.artist, track.name, track.duration) in [(t.artist, t.name, t.duration) for t in checked]:
            print(track.name)
        else:
            checked.append(track)


def checkquality():
    session = tidalapi.Session()
    session.login('max-mustermann545@gmx.de', 'PTmk29cKQdaCApQbz62T')
    session._config.quality = tidalapi.Quality.lossless
    favtracks = session.user.favorites.tracks()
    nothehighq = []

    for track in favtracks:
        searchresults = session.search('track', track).tracks
        if track.name in (trackcheck.name for trackcheck in searchresults):
            if track.id not in (trackcheck2.id for trackcheck2 in searchresults):
                nothehighq.append(track)
        else:
            continue

    print(f'These Tracks are available in Higher Quality: \n')
    for i in range(len(nothehighq)):
        print('\n'.join(nothehighq[i]))

if __name__ == '__main__':
    print("hello")