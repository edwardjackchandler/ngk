from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

nfobject_mappings = {
    "mappings": {
        "nfobject": {
            "properties": {
                "netflixid": {
                    "type": "keyword"
                },
                "title": {
                    "type": "text"
                },
                "image": {
                    "type": "text"
                },
                "synopsis": {
                    "type": "text"
                },
                "rating": {
                    "type": "float"
                },
                "type": {
                    "type": "keyword"
                },
                "released": {
                    "type": "keyword"
                },
                "runtime": {
                    "type": "keyword"
                },
                "largeimage": {
                    "type": "text"
                },
                "date": {
                    "type": "keyword"
                },
                "imdbid": {
                    "type": "keyword"
                },
                "download": {
                    "type": "boolean"
                }
            }
        }
    }
}

es.indices.create(index="netflix_crossing", body=nfobject_mappings)
