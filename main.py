import json
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog

f = open(r'files\catalog.json')
data_json = json.load(f)

books = []
magazines = []

for item in data_json:
    if item['source'] == 'book':
        books.append(
            Book(
                title=item['title'],
                subject=item['title'],
                upc=item['title'],
                issbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )
    elif item['source'] == 'magazine':
        magazines.append(
            Magazine(
                title=item['title'],
                subject=item['title'],
                upc=item['title'],
                volume=item['volume'],
                issue=item['issue'],
            )
        )
catalog_all = [books, magazines]
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result}')
