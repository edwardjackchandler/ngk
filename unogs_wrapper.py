import requests
import json

#{query}-!{syear},{eyear}-!{snfrate},{enfrate}-!{simdbrate},{eimdbrate}-!{genreid}-!{vtype}-!{audio}-!{subtitle}-!{imdbvotes}-!{downloadable}&t=ns&cl={clist}&st=adv&ob={sortby}&p={page}&sa={andor}
#create_query_dict(inner, ["46", "78"], "Title", 1, "andor")

def read_config(config_location):
    """convert config file into dictionary
    
    Arguments:
        config_location {string} -- location of config file
    
    Returns:
        dictionary -- config settings
    """

    with open(config_location, "r") as f:
        config_dict = json.load(f)
        return config_dict


def get_nfapi_details(param):
    config_dict = read_config("C:/Users/jchandler/Documents/Website/ngk/ngk/config.json")
    return config_dict["nfapi"][param]


def get_elastic_details():
    config_dict = read_config("C:/Users/jchandler/Documents/Website/ngk/ngk/config.json")
    return config_dict["elastic"]


def create_inner_string(inner_params):
    """convert parameters to correct string format for api
    
    Arguments:
        inner_params {dictionary} -- inner parameters
    
    Returns:
        string -- parameters in string form 
    """
    #print("inner_params", inner_params)
    inner = inner_params.copy()

    inner["year_range"] = ",".join(inner["year_range"])
    inner["nf_rating_range"] = ",".join(inner["nf_rating_range"])
    inner["imdb_rating_range"] = ",".join(inner["imdb_rating_range"])
    
    inner_string = "-!".join(list(inner.values()))

    return inner_string


def create_query_dict(inner_params, country_list, sort_by, pages, andor):
    #TODO
    """simpler way of creating api parameter dictionary
    
    Arguments:
        inner_params {dictionary} -- [description]
        country_list {list} -- [description]
        sort_by {string} -- [description]
        pages {int} -- [description]
        andor {string} -- [description]
    
    Returns:
        [type] -- [description]
    """

    params = {
        "q": create_inner_string(inner_params),
        "t":"ns",
        "cl": ",".join(country_list),
        "st":"adv",
        "ob": sort_by,
        "p": str(pages),
        "sa": andor
    }

    #print(params)

    return params


def get_unogs_json(params):
    response = requests.get(get_nfapi_details("url"), headers=get_nfapi_details("headers"), params=params)
    return response.json()

'''
def parse_unogs_json(unogs_json):
    unogs_dict = json.load(unogs_json)
    
    nfobject_list

    return nfobject_list
'''