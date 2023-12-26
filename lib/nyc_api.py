import requests
from bs4 import BeautifulSoup
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://web.archive.org/web/20180303155827/https://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print the prettified soup object
    print(soup.prettify())

    # Find the script tag containing the JSON data
    # script_tag = soup.find('script', {'type': 'application/json'})

    # Extract and parse the JSON data
    # json_data = json.loads(script_tag.string)

    # return json_data

programs = GetPrograms().get_programs()
# print(programs)

