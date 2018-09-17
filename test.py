import unogs_wrapper as unw
from unogs_query import UnogsQuery
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

#print(unw.get_unogs_json(unw.create_query_dict(inner, ["46"], "Title", 1, "and")))
#print(unw.get_unogs_json(unw.create_query_dict(inner, ["46","78"], "Title", 1, "and")))

first_query = UnogsQuery(search_string="Breaking Bad", year_range=["1900", "2018"], nf_rating_range=["0", "5"], 
                        imdb_rating_range=["0", "10"], genre_id="0", vid_type="Any", audio="Any", subtitle="Any", 
                        imdb_votes="gt100", downloadable="", country_list=["46"], sort_by="Title", pages=1, andor="and",
                        elastic=es)

print(first_query.query_count)
print(first_query.nfobjects)

#first_query.es_ingest_objects()
