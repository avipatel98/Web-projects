from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository

    album = repository.all() # Get all artists

    # Assert on the results
    assert album == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1)
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(2)
    assert album == Album(2, "Surfer Rosa", 1988, 1)

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    new_album = Album(None, "Whats going on", 1971, 5)
    repository.create(new_album)
    result = repository.all()
    assert result == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, 'Whats going on', 1971, 5)
        ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
        db_connection.seed("seeds/music_library.sql")
        repository = AlbumRepository(db_connection)
        assert repository.delete(2) == None
        result = repository.all()
        assert result == [
        Album(1, "Doolittle", 1989, 1)
        ]
