import datetime
from unittest.mock import patch

from raindropio import *


raindrop = {
    "_id": 2000,
    "collection": {"$db": "", "$id": -1, "$ref": "collections"},
    "collectionId": -1,
    "cover": "",
    "created": "2020-01-01T00:00:00.000Z",
    "creatorRef": {"_id": 3000, "fullName": "user name"},
    "domain": "www.example.com",
    "excerpt": "excerpt text",
    "lastUpdate": "2020-01-01T01:01:01Z",
    "link": "https://www.example.com/",
    "media": [],
    "pleaseParse": {"weight": 1},
    "removed": False,
    "sort": 3333333,
    "tags": ["abc", "def"],
    "title": "title",
    "type": "link",
    "user": {"$id": 3000, "$ref": "users"},
}


def test_get():
    api = API("dummy")
    with patch("raindropio.api.requests") as m:
        m.get().json.return_value = {"item": raindrop}

        c = Raindrop.get(api, 2000)

        assert c.id == 2000
        assert c.collection.id == -1
        assert c.cover == ""
        assert c.created == datetime.datetime(
            2020, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
        )
        assert c.domain == "www.example.com"
        assert c.excerpt == "excerpt text"
        assert c.lastUpdate == datetime.datetime(
            2020, 1, 1, 1, 1, 1, tzinfo=datetime.timezone.utc
        )
        assert c.link == "https://www.example.com/"
        assert c.media == []
        assert c.tags == ["abc", "def"]
        assert c.title == "title"
        assert c.type == RaindropType.link
        assert c.user.id == 3000


def test_search():
    api = API("dummy")
    with patch("raindropio.api.requests") as m:
        m.get().json.return_value = {"items": [raindrop]}

        found = Raindrop.search(api)
        assert found[0].id == 2000


def test_create():
    api = API("dummy")
    with patch("raindropio.api.requests") as m:
        m.post().json.return_value = {"item": raindrop}
        item = Raindrop.create(api, link="https://example.com")
        assert item.id == 2000


def test_update():
    api = API("dummy")
    with patch("raindropio.api.requests") as m:
        m.put().json.return_value = {"item": raindrop}
        item = Raindrop.update(api, id=2000, link="https://example.com")
        assert item.id == 2000


def test_remove():
    api = API("dummy")
    with patch("raindropio.api.requests") as m:
        Raindrop.remove(api, id=2000)
        assert m.delete.call_args[0] == (
            "https://api.raindrop.io/rest/v1/raindrop/2000",
        )
