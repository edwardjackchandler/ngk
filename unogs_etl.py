import unogs_wrapper as unw
from unogs_query import UnogsQuery
from time import sleep

total_searches = 3783

print(unw.get_elastic_details())

for page_num in range(0, total_searches//100 + 1):
    print("page_num", page_num)

    all_uk_nf = UnogsQuery(search_string="", year_range=["1900", "2018"], nf_rating_range=["0", "5"], 
                            imdb_rating_range=["0", "10"], genre_id="0", vid_type="Any", audio="Any", subtitle="Any", 
                            imdb_votes="gt100", downloadable="", country_list=["46"], sort_by="Title", pages=page_num + 1, andor="and")
    
    all_uk_nf.es_ingest_objects()

    sleep(5)

#all_nf

#total_searches = all_nf.query_count
#print(total_searches)
#print(all_nf.nfobjects)

