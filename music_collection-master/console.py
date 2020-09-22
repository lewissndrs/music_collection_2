import pdb
from model.album import Album
from model.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("Adele")
artist_repository.save(artist_1)
artist_2 = Artist("The Beatles")
artist_repository.save(artist_2)

album_1 = Album("21","Pop",artist_1)
album_repository.save(album_1)
album_2 = Album("Sgt Pepper", "Pop", artist_2)
album_repository.save(album_2)
album_3 = Album("19","Pop",artist_1)
album_repository.save(album_3)
album_4 = Album("25","Pop",artist_1)
album_repository.save(album_4)

results = album_repository.albums_by_artist(artist_1)

for result in results:
    print(result.__dict__)

artist = album_repository.artist_by_album(album_1)

print(artist)

pdb.set_trace()