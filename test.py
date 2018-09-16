import unogs_wrapper as nat

inner = {
    "search_string": "",
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

params = {
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

print(nat.call_api(nat.create_query_dict(inner, ["46","78"], "Title", 1, "and")))
