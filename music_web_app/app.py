import os
from flask import Flask, request
from lib.album_repository import *
from lib.database_connection import *
from lib.artist_repository import *
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['POST'])
def post_album():
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    new_album = Album(None, title, release_year, artist_id)
    album_repository.create(new_album)
    return f"Album {title} has been added!"

@app.route('/albums', methods=['GET'])
def get_all_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    return [str(album) for album in albums]
    # Make sure to use str to return the repr function 

@app.route('/albums/<id>', methods=["GET"])
def get_specific_album(id):
    connection = get_flask_database_connection(app)
    album_Repository = AlbumRepository(connection)
    album = album_Repository.find(id)
    return album.title

@app.route('/artists', methods=["GET"])
def get_artist_names():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return ', '.join([artist.name for artist in artists])

@app.route('/artists', methods=['POST'])
def post_new_artist():
    name = request.form['name']
    genre = request.form['genre']
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    new_artist = Artist(None, name, genre)
    artist_repository.create(new_artist)
    return "The new artist has been added."

@app.route('/')
def home():
    return '<p>You are home</p>'
# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

