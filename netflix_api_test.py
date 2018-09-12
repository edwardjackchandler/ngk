import requests

url = "https://unogs-unogs-v1.p.mashape.com/aaapi.cgi"

querystring = {"q":"-!1900,2018-!0,5-!0,10-!0-!Any-!Any-!Any-!gt100-!","t":"ns","cl":"46,78","st":"adv","ob":"Title","p":"1","sa":"and"}

headers = {
    'x-mashape-key': "WwhkdSlflnmsh5zyLzm2gI0AyBrHp1DIWznjsnBSVWeL0TkpPG",
    'accept': "application/json"
    }

response = requests.get(url, headers=headers, params=querystring)

print(response.text)