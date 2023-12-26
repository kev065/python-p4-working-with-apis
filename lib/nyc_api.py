import requests
from bs4 import BeautifulSoup
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://web.archive.org/web/20180303155827/https://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    data = response.json()

    # soup = BeautifulSoup(response.content, 'html.parser')

    # Print the prettified soup object
    # print(soup.prettify())

    # Parse the prettified soup object as JSON
    # data = json.loads(soup.prettify())

    return data

    # Find the script tag containing the JSON data
    # script_tag = soup.find('script', {'type': 'application/json'})

    # Extract and parse the JSON data
    # json_data = json.loads(script_tag.string)

    # return json_data
  
  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = self.get_programs()
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

# programs = GetPrograms().get_programs()
# print(programs)

programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
    print(agency)

