from db.run_sql import run_sql
from model.album import Album
from model.artist import Artist

def save(album):
    sql = 'INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *'
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql = 'SELECT * FROM albums'
    results = run_sql(sql)
    for row in results:
        album = Album(row['title'],row['genre'],row['artist_id'],row['id'])
        albums.append(album)
    return albums

def albums_by_artist(artist):
    albums = []
    sql = 'SELECT * FROM albums WHERE artist_id = %s'
    values = [artist.id]
    results = run_sql(sql,values)
    for row in results:
        album = Album(row['title'], row['genre'], row['artist_id'], row['id'])
        albums.append(album)
    return albums

def artist_by_album(album):
    sql = 'SELECT * FROM artists WHERE id = %s'
    values = [album.artist.id]
    results = run_sql(sql,values)
    return results
