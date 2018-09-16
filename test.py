import unogs_wrapper as unw
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

us_uk_params = {
    "q":"-!1900,2018-!0,5-!0,10-!0-!Any-!Any-!Any-!gt100-!",
    "t":"ns",
    "cl":"46,78",
    "st":"adv",
    "ob":"Title",
    "p":"1",
    "sa":"and"
}


inner = {
    "search_string": "Breaking Bad",
    "year_range": ["1900", "2018"],
    "nf_rating_range": ["0", "5"],
    "imdb_rating_range": ["0", "10"],
    "genre_id": "0",
    "vid_type": "Any",
    "audio": "Any",
    "subtitle": "Any",
    "imdb_votes": "gt100",
    "downloadable": ""
}

uk_params = {
    "q":"-!1900,2018-!0,5-!0,10-!0-!Any-!Any-!Any-!gt100-!",
    "t":"ns",
    "cl":"46,78",
    "st":"adv",
    "ob":"Title",
    "p":"1",
    "sa":"and"
}

headers = {
    'x-mashape-key': "WwhkdSlflnmsh5zyLzm2gI0AyBrHp1DIWznjsnBSVWeL0TkpPG",
    'accept': "application/json"
}

print(unw.call_api(unw.create_query_dict(inner, ["46"], "Title", 1, "and")))
#print(unw.call_api(unw.create_query_dict(inner, ["46","78"], "Title", 1, "and")))
