import os
from flask import Flask, request, redirect, render_template
from lib.album_repository import *
from lib.database_connection import *
from lib.artist_repository import *
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection()
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    return render_template('/albums/index.html', albums=albums)

@app.route('/albums/<id>')
def get_album(id):
    connection = get_flask_database_connection()
    album_repository = AlbumRepository(connection)
    album = album_repository.find(id)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(album.artist_id)
    return render_template('/albums/album_id.html', album=album, artist=artist)

@app.route('/albums/new', methods=['GET'])
def get_album_new():
    connection = get_flask_database_connection()
    return render_template('/albums/new.html')

@app.route('/albums', methods=['POST'])
def post_album_new():
    connection = get_flask_database_connection()
    album_repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    album_repository.create(album)
    return redirect(f'/albums/{album.id}')

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection()
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('/artists/index.html', artists=artists)

@app.route('/artists/<id>')
def get_artists_from_id(id):
    connection = get_flask_database_connection()
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(id)
    return render_template('artists/artist_id.html', artist=artist)


@app.route('/artists/new', methods=['GET'])
def get_artist_new():
    get_flask_database_connection()
    return render_template('/artists/new.html')

@app.route('/artists', methods=['POST'])
def post_artist_new():
    connection = get_flask_database_connection()
    artist_repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    artist_repository.create(artist)
    return redirect(f'/artists/{artist.id}')

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
