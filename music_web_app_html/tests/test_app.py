from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tag = page.locator("div")
    expect(div_tag).to_have_text([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa\nReleased: 1988"
    ])

def test_get_find_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(
        "Release year: 1988 Artist: Pixies"
    )

def test_get_album_click_to_specific_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Doolittle"')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text(
        "Doolittle"
    )
    paragraph_tag = page.locator("p")
    expect(paragraph_tag).to_have_text(
        "Release year: 1989 Artist: Pixies"
    )

"""Create a HTML page showing all artists at route /artists GET request"""

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    h1_tag = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(h1_tag).to_have_text("Artist library")
    expect(paragraph_tag).to_have_text([
        "Artist: Pixies Genre: Rock",
        "Artist: ABBA Genre: Pop",
        "Artist: Taylor Swift Genre: Pop",
        "Artist: Nina Simone Genre: Jazz"
    ])

"""Add a route GET /artists/<id> which returns an HTML page showing details for a single artist."""

def test_get_artist_from_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/3")
    h1_tag = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(h1_tag).to_have_text("Taylor Swift")
    expect(paragraph_tag).to_have_text("Genre: Pop")

"""Link with anchor tags to specifc artists at route /artists/<id> where <id> needs to be the corresponding artist id."""

def test_get_artists_then_check_info_of_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Taylor Swift'")
    h1_tag = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(h1_tag).to_have_text("Taylor Swift")
    expect(paragraph_tag).to_have_text("Genre: Pop")

# === Example Code Below ===


"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
