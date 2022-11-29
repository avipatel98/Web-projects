# Tests for your routes go here

def test_get_wave(web_client):
    response = web_client.get("/wave?name=leo") # Pass the path to the request including all paramaters to the .get method
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "I am waving at leo"

def test_post_submit(web_client):
    response = web_client.post("/submit", data={"name":"avi", "message" : "Hello world"}) #pass the path and then data to be sent as a dictionary with the key and values being passed
    assert response.status_code == 200
    assert response.data.decode("utf-8") == """Thanks avi, you sent this message: "Hello world" """

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'
"""
When: I make a POST request to POST http://localhost:5000/sort-names
And: I send names=Joe,Alice,Zoe,Julia,Kieran as the body parameter text
Then: I should get the names sorted alphabetically joined by commas
Alice,Joe,Julia,Kieran,Zoe
"""

def test_post_sort_names(web_client):
    response = web_client.post("/sort-names", data={'names':"Joe,Alice,Zoe,Julia,Kieran"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
When: I make a get request on /names?add=Eddie
I am expecting it to return the list of names with the new name at the end.
Testing for Expected response (2OO OK):
Julia, Alice, Karim, Eddie
"""

def test_get_add_name(web_client):
    response = web_client.get("/names?add=Eddie")
    #assert response.status_code == 200
    assert response.data.decode("utf-8") == "Julia, Alice, Karim, Eddie"

def test_get_add_empty_name(web_client):
    response = web_client.get("/names")
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "You did not try to add a new name!"

def test_get_add_name(web_client):
    response = web_client.get("/names?add=Eddie Avi")
    #assert response.status_code == 200
    assert response.data.decode("utf-8") == "Julia, Alice, Karim, Eddie Avi"
# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"


# # === End Example Code ===
