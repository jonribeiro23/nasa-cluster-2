import requests
from pprint import pprint
KEY = 'ZMi4iht5duGBNLBuR5Xma791U83KCvsVikdWeLka'

class GeneLab:
    def search(self, term):
        r = requests.get(f'https://genelab-data.ndc.nasa.gov/genelab/data/search?term={term}')
        return r.json()


class ImagesVideos:
    def search(self, term):
        r = requests.get(f'https://images-api.nasa.gov/search?q={term}')
        return r.json()


class TechPort:
    # from api_key import KEY
    def search(self):
        r = requests.get(f'https://api.nasa.gov/techport/api/projects?api_key={KEY}')
        return r.json()

    def search_project(self, _id):
        r = requests.get(f'https://api.nasa.gov/techport/api/projects/{_id}?api_key={KEY}')
        return r.json()


class CatalogData:
    def search(self, term):
        r = requests.get(f'https://catalog.data.gov/api/3/action/package_search?q={term}')
        return r.json()
