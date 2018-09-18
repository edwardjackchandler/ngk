import unogs_wrapper as unw
from elasticsearch import Elasticsearch, helpers
import html.parser as htmlparser


class NfObject:

    def __init__(self, params):
        self.netflixid = params["netflixid"]
        self.title = params["title"]
        self.image = params["image"]
        self.synopsis = params["synopsis"]
        self.rating = params["rating"]
        self.type = params["type"]
        self.released = params["released"]
        self.runtime = params["runtime"]
        self.largeimage = params["largeimage"]
        self.date = params["date"]
        self.imdbid = params["imdbid"]
        self.download = params["download"]


class UnogsQuery:

    def __init__(self, search_string, year_range, nf_rating_range, imdb_rating_range, genre_id, 
               vid_type, audio, subtitle, imdb_votes, downloadable, country_list, sort_by, pages, 
               andor, elastic=None, es_dict_template=None):
        """Represents a query with all the different parameters involved.
        
        Arguments:
            search_string {string} -- [description]
            year_range {list} -- [description]
            nf_rating_range {list} -- [description]
            imdb_rating_range {list} -- [description]
            genre_id {string} -- [description]
            vid_type {string} -- [description]
            audio {string} -- [description]
            subtitle {string}} -- [description]
            imdb_votes {string} -- [description]
            downloadable {int} -- [description]
            country_list {list} -- [description]
            sort_by {string} -- [description]
            pages {int} -- [description]
            andor {string} -- [description]
        
        Keyword Arguments:
            elastic {[type]} -- [description] (default: {None})
            es_dict_template {[type]} -- [description] (default: {None})
        """

        

        inner_params = {
            "search_string": search_string,
            "year_range": year_range,
            "nf_rating_range": nf_rating_range,
            "imdb_rating_range": imdb_rating_range,
            "genre_id": genre_id,
            "vid_type": vid_type,
            "audio": audio,
            "subtitle": subtitle,
            "imdb_votes": imdb_votes,
            "downloadable": downloadable
        }

        params_dict = unw.create_query_dict(inner_params, country_list, sort_by, pages, andor)

        self.query_json = unw.get_unogs_json(params_dict)
        self.query_count = self.query_json["COUNT"]
        self.nfobjects = self.query_json["ITEMS"]

        if len(country_list) == 1:
            print(type(country_list))

            for nfobject_dict in self.nfobjects:
                nfobject_dict["country_code"] = country_list[0]
                
                if country_list[0] == "46":
                    nfobject_dict["country"] = "uk"
                elif country_list[0] == "78":
                    nfobject_dict["country"] = "usa"

        #self.nfobjects = parse_nfobjects(self.query_json["ITEMS"])

        if unw.get_elastic_details:
            self.es = Elasticsearch([unw.get_elastic_details()])
            # self.es_dict_template = es_dict_template


    def es_ingest_objects(self):
        ingest_list = []
        parser = htmlparser.HTMLParser()

        es_dict_template = {
            "_index": "netflix_crossing",
            "_type": "nfobject"
        }

        title_list = []

        for nfobject in self.nfobjects:
            ingest_dict = es_dict_template.copy()


            nfobject["title"] = parser.unescape(nfobject["title"])
            nfobject["synopsis"] = parser.unescape(nfobject["synopsis"])

            title_list.append(nfobject["title"])

            ingest_dict.update(nfobject)

            ingest_list.append(ingest_dict)

        helpers.bulk(self.es, ingest_list)

        print("Objects ingested")
        print("Title list")
        print(title_list)

    '''
    def parse_nfobjects(object_list):
        [NfObject(json_object) for json_object in ]


        return nfobjects
    '''

    '''
    def gendata():


        mywords = ['foo', 'bar', 'baz']
        for word in mywords:
            yield {
                "_index": "mywords",
                "_type": "document",
                "doc": {"word": word},
            }

    bulk(self.es, gendata())
    '''