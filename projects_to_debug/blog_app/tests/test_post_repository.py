import pytest
from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get an empty list
"""
def test_get_all_records():
    repository = PostRepository()
    posts = repository.all()

    assert posts == []

"""
When we call PostRepository#create
We see the post reflected in #all
"""
def test_create_record():
    repository = PostRepository()
    post = Post(None, "Test Title", "Test Content")
    created_post = repository.create(post)
    assert created_post == Post(1, "Test Title", "Test Content")

    result = repository.all()
    assert result == [
        Post(1, "Test Title", "Test Content", [])
    ]

def test_create_multiple_records():
    repository = PostRepository()
    post1 = Post(None, "Test Title", "Test Content")
    post2 = Post(None, "Test Title", "Test Content")
    post3 = Post(None, "Test Title", "Test Content")
    created_post1 = repository.create(post1)
    created_post2 = repository.create(post2)
    created_post3 = repository.create(post3)
    assert created_post1 == Post(1, "Test Title", "Test Content")
    assert created_post2 == Post(2, "Test Title", "Test Content")
    assert created_post3 == Post(3, "Test Title", "Test Content")

    result = repository.all()
    assert result == [
        Post(1, "Test Title", "Test Content", []),
        Post(2, "Test Title", "Test Content", []),
        Post(3, "Test Title", "Test Content", [])
    ]
