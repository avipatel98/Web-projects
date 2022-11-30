# Tests for your routes go here
"""
With: POST Request '/albums' 
Using: data={title:voyage, release_year:2022, artist_id:2}
Expected response (200 OK)
"""

def test_post_album(web_client, db_connection):
    connection = db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/albums', data={'title':'voyage', 'release_year':'2022', 'artist_id':'2'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album voyage has been added!"
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == '["Album(1, Doolittle, 1989, 1)","Album(2, Surfer Rosa, 1988, 1)","Album(3, Waterloo, 1974, 2)","Album(4, Super Trouper, 1980, 2)","Album(5, Bossanova, 1990, 1)","Album(6, Lover, 2019, 3)","Album(7, Folklore, 2020, 3)","Album(8, I Put a Spell on You, 1965, 4)","Album(9, Baltimore, 1978, 4)","Album(10, Here Comes the Sun, 1971, 4)","Album(11, Fodder on My Wings, 1982, 4)","Album(12, Ring Ring, 1973, 2)","Album(13, voyage, 2022, 2)"]\n'

def test_get_specific_album(web_client, db_connection):
    connection = db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/albums/2')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Surfer Rosa"

"""
With: GET request on the path '/artists'
Return: all artist names which is the name value stored in the artist object
Expects: 200 OK, Pixies, ABBA, Taylor Swift, Nina Simone
"""

def test_get_all_artist_names(web_client, db_connection):
    connection = db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
# Request:
POST /artists
With: POST request pass in a new artist to be added to the database, using the body parameters data={name:Wild nothing, genre:Indie}
Returning: A string confirming the addition of the new artist, and 200 OK
WITH: GET request 
Return: a list of artists containin the new artist added
Expected response (200 OK), Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""

def test_post_create_new_artist_and_confirm_with_get_all(web_client, db_connection):
    connection = db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/artists', data={'name':'Wild nothing', 'genre':'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "The new artist has been added."
    response = web_client.get('artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"
# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
